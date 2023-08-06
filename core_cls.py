import threading
import socket
import datetime
import sys

import chat_util_cls
import chat_settings_cls


class MsgServer():
    """
    Message and file exchange server.
    Usage:
        init MsgServer class
        call start_server() method
    Example:
        my_server = MsgServer()
        my_server.start_server()
    """

    HEADER = 64
    PORT = 2909
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)
    FORMAT = "utf-8"
    DISCONNECT_MESSAGE = "!DISCONNECT"

    def __init__(self,
                 date_format: str = "%d.%m.%Y.", 
                 time_format: str ="%H:%M:%S"
                 ):
        # Variables
        self.date_format = date_format
        self.time_format = time_format

        # Help functions
        self._util = chat_util_cls.Utilities(
            date_format=self.date_format,
            time_format=self.time_format
        )

        self._is_running = False  # True if server is started
        self._connections_dict = {}  # All active connections, key is client addres

    def start_server(self):
        # Record server start time
        self._connections_dict["server"] = {}
        self._connections_dict["server"]["start"] = self._util.get_current_date_and_time()

        # Bind server
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind(self.ADDR)
        self._start_listening()

    def stop_server(self):
        self._is_running = False
        self._server.close()
        sys.exit("Server stoped !")

    def _start_listening(self) -> None:
        self._is_running = True
        self._server.listen()

        while self._is_running:
            conn, addr = self._server.accept()
            thread = threading.Thread(target=self._handle_client, args=(conn, addr))
            thread.start()

    def _handle_client(self, conn: socket.socket, addr) -> None:
        """ self._connection_dict = dict{addr}
        addr{}:
            messages (list): all messages [ type, message, time ]
                type (int): 1=lenght_recived, 2=lenght_send, 10=recived, 20=send
                message (str): message body
                time (str): time of event
            errors (list): list of all errors [ message, error, time ]
                message (str): message body
                error (str): error description
                time (str): time of event
            start (str): time - connection established
            end (str): time - connection terminated
        """
        # Create dictionary for new client
        if addr not in self._connections_dict:
            self._connections_dict[addr] = {
                "messages": [],
                "errors": [],
                "start": "",
                "end": ""
            }

        connected = True
        # Record start of connection
        self._connections_dict[addr]["start"] = self._util.get_current_date_and_time()
        
        # Start loop
        while connected:
            # Recive lenght of incoming message
            msg_len = conn.recv(self.HEADER).decode(self.FORMAT)
            # print (f"RECIVED HEADER: {msg_len}")
            if msg_len:
                msg_length = self._util.string_to_integer(msg_len)
                
                # Record error if msg is not integer
                if msg_length is None:
                    self._connections_dict[addr]["errors"].append([msg_len, "Expected message lenght !", self._util.get_current_date_and_time()])
                    continue
                
                # Record message with incoming message lenght information
                self._connections_dict[addr]["messages"].append([1, msg_len, self._util.get_current_date_and_time()])
                
                # Recive message
                msg = conn.recv(msg_length).decode(self.FORMAT)
                self._process_new_message(msg, addr)
                print (f"RECIVED BODY: {msg}")


                # Check if this is Disconect message
                if msg == self.DISCONNECT_MESSAGE:
                    conn.send("Disconected !".encode(self.FORMAT))
                    self._connections_dict[addr]["messages"].append([20, "Disconnected !", self._util.get_current_date_and_time()])
                    self._connections_dict[addr]["end"] = self._util.get_current_date_and_time()
                    connected = False
                else:
                    conn.send("OK.".encode(self.FORMAT))
                    self._connections_dict[addr]["messages"].append([20, "OK.", self._util.get_current_date_and_time()])
                
        conn.close()

    def _process_new_message(self, message_text: str, client_addr):
        # Record message
        self._connections_dict[client_addr]["messages"].append([10, message_text, self._util.get_current_date_and_time()])

        # Check commands
        # if len(message_text) > 
        # commands = 


    @property
    def server_port(self) -> int:
        return self.PORT

    @server_port.setter
    def server_port(self, value: int) -> None:
        if self._is_running:
            raise RuntimeWarning("Setting like PORT or IP cannot be changed if server is running !")
        
        if not isinstance(value, int):
            raise TypeError(f"Port number must be integer value not {type(value)}")
        
        if value < 1025 or value > 65535:
            raise ValueError("Port number must be integer value 1025 - 65535")
        
        self.PORT = value
        self.ADDR = (self.SERVER, self.PORT)

    @property
    def server_ip(self) -> str:
        return self.SERVER

    @server_ip.setter
    def server_ip(self, value: str) -> None:
        if self._is_running:
            raise RuntimeWarning("Setting like PORT or IP cannot be changed if server is running !")
        
        if not isinstance(value, str):
            raise TypeError(f"Server IP must be string value (xxx.xxx.xxx.xxx) not {type(value)}")
        
        ip_l = [x for x in value.split(".") if x != ""]
        
        val_ok = True
        
        if len(ip_l) != 4:
            val_ok = False
        
        try:
            for i in ip_l:
                if int(i) < 0 or int(i) > 255:
                    val_ok = False
        except ValueError:
            val_ok = False
        
        if not val_ok:
            raise ValueError("Incorrect server IP address.")
        
        self.SERVER = ".".join(ip_l)
        self.ADDR = (self.SERVER, self.PORT)

    @property
    def server_disconnect_message(self) -> str:
        return self.DISCONNECT_MESSAGE
    
    @server_disconnect_message.setter
    def server_disconnect_message(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f"Disconnect message must be string value not {type(value)}")
        
        if not value:
            raise ValueError("Disconnect message canot be empty string.")
        
        self.DISCONNECT_MESSAGE = value


class MsgClient(QObject):
    """
    Makes a connection to the server.
    Usage: 
        Init class and call 'connect_to_server' method
        Use 'send' to send message
        Use event 'signal_message_recived' to recive messages
        
        If non fatal error occurres signal 'signal_error_occurred' will be emited
    """
    def __init__(self,
                 settings: chat_settings_cls.Settings,
                 *args, **kwargs
                 ):
        
        super().__init__(*args, *kwargs)
        # Define settings class and methods
        self._stt = settings
        self.getv = self._stt.get_setting_value
        self.setv = self._stt.set_setting_value
        self.getl = self._stt.lang
        self.get_appv = self._stt.app_setting_get_value
        self.set_appv = self._stt.app_setting_set_value

        # Variables
        self.HEADER = 64
        self.PORT = 2909
        self.SERVER = "192.168.1.3"
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = "utf-8"

        self.date_format = self.getv("date_format")
        self.time_format = self.getv("time_format")
        
        # Help functions
        self._util = chat_util_cls.Utilities(self._stt)

        self._is_running = False  # True if client is started
        
        self._connection_dict = {
            "start": None,
            "messages": [],
            "errors": [],
            "end": None
        }  # Active connection

    def is_running(self) -> bool:
        return self._is_running

    def connect_to_server(self):
        # Record client start time
        self._connection_dict["start"] = self._util.get_current_date_and_time()

        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect(self.ADDR)

        self.thread_recive = threading.Thread(target=self._recive)
        self.thread_recive.start()

    def send(self, message: str) -> None:
        msg = message.encode(self.FORMAT)
        msg_lenght = len(msg)
        send_lenght = str(msg_lenght).encode(self.FORMAT)
        send_lenght += b" " * (self.HEADER - len(send_lenght))
        
        self._client.send(send_lenght)
        self._connection_dict["messages"].append([2, send_lenght, self._util.get_current_date_and_time()])
        
        self._client.send(msg)
        self._connection_dict["messages"].append([20, msg, self._util.get_current_date_and_time()])

    def _recive(self):
        """
        Recives mesesages from server
        """
    
        while self._is_running:
            # Get lenght of message
            msg_header = self._client.recv(self.HEADER).decode(self.FORMAT)
            self._connection_dict["messages"].append([1, msg_header, self._util.get_current_date_and_time()])
            msg_len = self._util.string_to_integer(msg_header)
            
            if msg_len is None:
                self._connection_dict["errors"].append([msg_header, "Expected message lenght !", self._util.get_current_date_and_time()])
                self.signal_error_occurred_send(f"Expected message lenght, recived:{msg_header}")
                continue
            
            msg_text = self._client.recv(msg_len).decode(self.FORMAT)
            self._connection_dict["messages"].append([10, msg_text, self._util.get_current_date_and_time()])

            commands, msg_text = self._util.parse_message(msg_text)
            
            if msg_text:
                self.message_queue.append([msg_text, self._util.get_current_date_and_time()])
                self.signal_incoming_messages_send(self.message_queue)
            
            if "disconnect" in self._util.commands_only_list(commands):
                self._is_running = False


    def get_server_port(self) -> int:
        return self.PORT

    def set_server_port(self, value: int) -> bool:
        if self._is_running:
            print("Setting like PORT or IP cannot be changed if client is running !")
            return False
        
        if not isinstance(value, int):
            print(f"Port number must be integer value not {type(value)}")
            return False
        
        if value < 1025 or value > 65535:
            print("Port number must be integer value 1025 - 65535")
            return False
        
        self.PORT = value
        self.ADDR = (self.SERVER, self.PORT)
        return True

    def get_server_ip(self) -> str:
        return self.SERVER

    def set_server_ip(self, value: str) -> bool:
        if self._is_running:
            print("Setting like PORT or IP cannot be changed if client is running !")
            return False
        
        if not isinstance(value, str):
            print(f"Server IP must be string value (xxx.xxx.xxx.xxx) not {type(value)}")
            return False
        
        ip_l = [x for x in value.split(".") if x != ""]
        
        val_ok = True
        
        if len(ip_l) != 4:
            val_ok = False
        
        try:
            for i in ip_l:
                if int(i) < 0 or int(i) > 255:
                    val_ok = False
        except ValueError:
            val_ok = False
        
        if not val_ok:
            print(f"Incorrect server IP address. {value}")
            return False
        
        self.SERVER = ".".join(ip_l)
        self.ADDR = (self.SERVER, self.PORT)
        return True
