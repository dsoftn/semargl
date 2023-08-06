from PyQt5.QtWidgets import (QFrame, QPushButton, QTextEdit, QScrollArea, QVBoxLayout,
    QGridLayout, QWidget, QSpacerItem, QSizePolicy, QListWidget, QFileDialog, QDialog,
    QLabel, QListWidgetItem, QDesktopWidget, QLineEdit, QCalendarWidget, QHBoxLayout, QCheckBox, QAction,
    QProgressBar, QStackedWidget, QComboBox, QApplication)
from PyQt5.QtGui import QIcon, QFont, QFontMetrics, QStaticText, QPixmap, QCursor, QTextCharFormat, QColor, QImage, QResizeEvent
from PyQt5.QtCore import (QSize, Qt, pyqtSignal, QObject, QCoreApplication, QRect,
    QPoint, QTimer, QThread, QDate)
from PyQt5 import uic, QtGui, QtCore

import datetime
import os
import json

import chat_settings_cls


class Utilities():
    def __init__(self,
                 settings: chat_settings_cls.Settings
                 ):
        # Define settings class and methods
        self._stt = settings
        self.getv = self._stt.get_setting_value
        self.setv = self._stt.set_setting_value
        self.getl = self._stt.lang
        self.get_appv = self._stt.app_setting_get_value
        self.set_appv = self._stt.app_setting_set_value
        
        self.date_format_string = self.getv("date_format")
        self.time_format_string = self.getv("time_format")

        self.command_string = "!COMMAND:"

    def encode_text(self, txt: str) -> str:
        return txt

    def decode_text(self, txt: str) -> str:
        return txt

    def create_directory_structure(self, file_or_dir_path: str) -> bool:
        if not file_or_dir_path:
            return False
        
        if file_or_dir_path[-1] in "/\\":
            directory = file_or_dir_path[:-1]
        else:            
            directory = os.path.split(file_or_dir_path)
            directory = directory[0]
        
        if not directory:
            return False
        
        if not os.path.isdir(directory):
            os.mkdir(directory)
        
        return True

    def get_current_date(self) -> str:
        date = datetime.date.today()
        result = date.strftime(self.date_format_string)
        return result

    def get_current_time(self) -> str:
        time = datetime.datetime.now()
        result = time.strftime(self.time_format_string)
        return result

    def get_current_date_and_time(self) -> str:
        date = self.get_current_date()
        time = self.get_current_time()
        result = date + " " + time
        return result

    def string_to_integer(self, string_value: str) -> int:
        try:
            result = int(string_value)
            return result
        except ValueError:
            return None

    def is_message_exists(self, message_text: str) -> bool:
        """
        Checks if there is a message that should be displayed to the user.
        Returns True if there is a valid message, False if it is an empty string or text contains only commands.
        """
        if self.parse_message(message_text)[1]:
            return True
        else:
            return False

    def commands_only_list(self, commands_list: list) -> list:
        """
        Arg: commands_list (list): list of commands and values returned from 'parse_message' method
        Returns: list of commands only, without values
        """
        comm_list = [x[0] for x in commands_list]
        return comm_list

    def parse_message(self, message_text: str) -> tuple:
        """
        Checks if the received message contains commands that the server or client should execute.
        If there are commands, it creates list of commands and their values.
        Returns:
            Tuple ( commands list (list), message text (str) )
                commands list (list): [ command name, command value ]
        """
        command_len = len(self.command_string)

        commands = []
        msg_text = ""

        if message_text[:command_len] == self.command_string:
            # Checking that the command string is properly closed.
            if message_text.find(";;;") < 0:
                raise ValueError("Unrecognized command string, end of commands not found !")

            
            # Find commands and make list of command=value pairs
            commands_text = message_text[9:message_text.find(";;;")]
            commands_list = commands_text.split(";;")
            
            # Append all commands and their values in commands list
            for i in commands_list:
                if i.find("=") >= 0:
                    command = i[:i.find("=")].lower()
                    value = i[i.find("=") + 1:]
                else:
                    command = i.lower()
                    value = None
                commands.append([command, value])
            
            # Find message body
            msg_text = message_text[message_text.find(";;;") + 3:]

        else:
            msg_text = message_text
        
        return (commands, msg_text)

    def available_commands(self) -> dict:
        """
        Returns all available commands as dictionary.
        Returns (dict): command = description
        """
        commands = {
            "disconnect": "Terminates the client's connection to the server."
        }

        return commands

        
class MsgUtil():
    def __init__(self, settings: chat_settings_cls.Settings) -> None:
        # Define settings class and methods
        self._stt = settings
        self.getv = self._stt.get_setting_value
        self.setv = self._stt.set_setting_value
        self.getl = self._stt.lang
        self.get_appv = self._stt.app_setting_get_value
        self.set_appv = self._stt.app_setting_set_value
        

class Signal(QObject):
    signal_error = pyqtSignal(dict)
    signal_language_changed = pyqtSignal()

    def __init__(self,
            settings: chat_settings_cls.Settings,
            ) -> None:
        super().__init__()
        # Define settings class and methods
        self._stt = settings
        self.getv = self._stt.get_setting_value
        self.setv = self._stt.set_setting_value
        self.getl = self._stt.lang
        self.get_appv = self._stt.app_setting_get_value
        self.set_appv = self._stt.app_setting_set_value

    def send_signal_error(self, error_dict: dict):
        self.signal_error.emit(error_dict)

    def send_signal_language_changed(self):
        self.signal_language_changed.emit()


class User():
    def __init__(self,
            settings: chat_settings_cls.Settings,
            username: str = None,
            password: str = None
            ) -> None:
        
        # Define settings class and methods
        self._stt = settings
        self.getv = self._stt.get_setting_value
        self.setv = self._stt.set_setting_value
        self.getl = self._stt.lang
        self.get_appv = self._stt.app_setting_get_value
        self.set_appv = self._stt.app_setting_set_value
        self.util: Utilities = self.get_appv("util")

        # Define variables
        self.user_id = None
        self.username = username
        self.password = password
        self.name = None
        self.mail = None
        self.about = None
        self.picture = None
        self.language = None
        self.auto_pass = None
        self.auto_load = None
        self.auto_connect = None
        self.load_user()

    def is_user_loaded(self) -> bool:
        if self.user_id:
            return True
        else:
            return False        

    def is_user_autoconnecting(self) -> bool:
        return self.auto_connect

    def is_user_autoloading(self, username:str) -> bool:
        if not username:
            return None
        
        users = self.get_all_users_data()
        if username in users:
            return users[username]["auto_load"]
        return None

    def load_user(self, username: str = None, password: str = None) -> bool:
        if username is None:
            username = self.username
        else:
            self.username = username
        if password is None:
            password = self.password
        else:
            self.password = password
        
        if username is None:
            return False
        
        users: dict = self.get_all_users_data()
        if username not in users:
            return False
        
        if self.util.decode_text(users[username]["password"]) != password:
            return False
        
        self.user_id = users[username].setdefault("id", "")
        self.username = username
        self.password = password
        self.name = users[username].setdefault("name", "")
        self.mail = users[username].setdefault("mail", "")
        self.about = users[username].setdefault("about", "")
        self.picture = users[username].setdefault("picture", "")
        self.language = users[username].setdefault("language", "")
        self.auto_pass = users[username].setdefault("auto_pass", False)
        self.auto_load = users[username].setdefault("auto_load", False)
        self.auto_connect = users[username].setdefault("auto_connect", True)

        return True

    def get_list_of_all_users(self) -> list:
        result = []
        users = self.get_all_users_data()
        for user in users:
            result.append(user)
        return result

    def get_all_users_data(self) -> dict:
        user_path = os.path.abspath(self.getv("users_folder_path"))
        self.util.create_directory_structure(user_path)
        file_list = os.listdir(user_path)
        result = {}
        for file in file_list:
            if os.path.isdir(file):
                user_data = self._get_user_data_from_dir(file)
                if user_data:
                    result[user_data["username"]] = user_data
        return result

    def _get_user_data_from_dir(self, dir_path: str) -> dict:
        file_list = os.listdir(dir_path)
        if "info.json" not in file_list:
            return None
        
        with open(f"{dir_path}info.json", "r", encoding="utf-8") as file:
            result = json.load(file)
        
        return result


class Login(QDialog):
    def __init__(self,
                 settings: chat_settings_cls.Settings,
                 parent_widget: QWidget = None,
                 username: str = None,
                 password: str = None,
                 application_modal: bool = True,
                 *args, **kwargs
                 ) -> None:
        super().__init__(parent_widget, *args, **kwargs)

        if application_modal:
            self.setWindowModality(Qt.ApplicationModal)

        # Define settings class and methods
        self._stt = settings
        self.getv = self._stt.get_setting_value
        self.setv = self._stt.set_setting_value
        self.getl = self._stt.lang
        self.get_appv = self._stt.app_setting_get_value
        self.set_appv = self._stt.app_setting_set_value

        # Define variables
        self.util: Utilities = self.get_appv("util")
        self.user: User = self.get_appv("user")
        self.signal: Signal = self.get_appv("signal")
        self._selected_user = None

        # Load designer GUI file
        uic.loadUi(self.getv("login_ui_file_path"), self)

        # Define Widgets
        self._define_widgets()

        # Connect events with slots
        self.btn_exit.clicked.connect(self._btn_exit_click)
        self.btn_guest.clicked.connect(self._btn_guest_click)
        self.btn_new.clicked.connect(self._btn_new_click)
        self._connect_signals()


    def _connect_signals(self):
        self.signal.signal_language_changed.connect(self.change_language)

    def _btn_new_click(self):
        new_user_cls =  NewUser(self._stt, self, application_modal=True)
        new_user = new_user_cls.start_gui()
        if new_user:
            self._populate_widgets(select_username=new_user)

    def _btn_guest_click(self):
        self._selected_user = "!GUEST"
        self.close()

    def _btn_exit_click(self):
        self.close()

    def start_gui(self, username: str = None, password: str = None) -> str:
        self._populate_widgets()
        self.show()
        self.exec_()
        return self._selected_user

    def _populate_widgets(self, select_username: str = None):
        users = self.user.get_list_of_all_users()
        self.cmb_username.clear()
        for user in users:
            self.cmb_username.addItem(user)
        
        if select_username:
            if select_username in users:
                self.cmb_username.setCurrentText(select_username)
                return
            
        if self.getv("last_user") in users:
            self.cmb_username.setCurrentText(self.getv("last_user"))
            return

    def _define_widgets(self):
        self.lbl_title: QLabel = self.findChild(QLabel, "lbl_title")
        self.lbl_avatar: QLabel = self.findChild(QLabel, "lbl_avatar")

        self.cmb_username: QComboBox = self.findChild(QComboBox, "cmb_username")
        self.txt_pass: QLineEdit = self.findChild(QLineEdit, "txt_pass")

        self.btn_new: QPushButton = self.findChild(QPushButton, "btn_new")
        self.btn_guest: QPushButton = self.findChild(QPushButton, "btn_guest")
        self.btn_login: QPushButton = self.findChild(QPushButton, "btn_login")
        self.btn_exit: QPushButton = self.findChild(QPushButton, "btn_exit")

        self.change_language()
        self._define_widgets_apperance()
        
    def _define_widgets_apperance(self):
        self.setWindowIcon(QIcon(self.getv("login_icon_path")))
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setFixedSize(500, 230)

    def change_language(self):
        self.setWindowTitle(self.getl("login_lbl_title_text"))
        self.lbl_title.setText(self.getl("login_lbl_title_text"))
        self.cmb_username.setPlaceholderText(self.getl("login_txt_username_placeholder_text"))
        self.txt_pass.setPlaceholderText(self.getl("login_txt_pass_placeholder_text"))
        self.btn_new.setText(self.getl("login_btn_new_text"))
        self.btn_new.setToolTip(self.getl("login_btn_new_tt"))
        self.btn_guest.setText(self.getl("login_btn_guest_text"))
        self.btn_guest.setToolTip(self.getl("login_btn_guest_tt"))
        self.btn_login.setText(self.getl("login_btn_login_text"))
        self.btn_login.setToolTip(self.getl("login_btn_login_tt"))
        self.btn_exit.setText(self.getl("login_btn_exit_text"))
        self.btn_exit.setToolTip(self.getl("login_btn_exit_tt"))


class NewUser(QDialog):
    def __init__(self,
                 settings: chat_settings_cls.Settings,
                 parent_widget: QWidget = None,
                 application_modal: bool = True,
                 *args, **kwargs
                 ) -> None:
        super().__init__(parent_widget, *args, **kwargs)

        if application_modal:
            self.setWindowModality(Qt.ApplicationModal)

        # Define settings class and methods
        self._stt = settings
        self.getv = self._stt.get_setting_value
        self.setv = self._stt.set_setting_value
        self.getl = self._stt.lang
        self.get_appv = self._stt.app_setting_get_value
        self.set_appv = self._stt.app_setting_set_value

        # Define variables
        self.util: Utilities = self.get_appv("util")
        self.user: User = self.get_appv("user")
        self.signal: Signal = self.get_appv("signal")
        self._selected_user = None

        # Load designer GUI file
        uic.loadUi(self.getv("new_user_ui_file_path"), self)

        # Define Widgets
        self._define_widgets()
        self._populate_widgets()

        # Connect events with slots
        self.cmb_lang.currentTextChanged.connect(self._cmb_lang_current_text_changed)
        self._connect_signals()


    def _connect_signals(self):
        self.signal.signal_language_changed.connect(self.change_language)

    def _cmb_lang_current_text_changed(self):
        if self.cmb_lang.currentText():
            self._stt.ActiveLanguageID = self.cmb_lang.currentData()
        self.signal.send_signal_language_changed()

    def start_gui(self) -> str:
        self.show()
        self.exec_()
        return self._selected_user

    def _populate_widgets(self):
        # Populate languages combo box
        self.cmb_lang.clear()
        for language in self._stt.GetListOfAllLanguages:
            self.cmb_lang.addItem(language[1], language[0])
        self.cmb_lang.setCurrentText(self._stt.get_language_name(self._stt.ActiveLanguageID))

    def _define_widgets(self):
        self.lbl_title: QLabel = self.findChild(QLabel, "lbl_title")
        self.lbl_username: QLabel = self.findChild(QLabel, "lbl_username")
        self.lbl_pass: QLabel = self.findChild(QLabel, "lbl_pass")
        self.lbl_pass_conf: QLabel = self.findChild(QLabel, "lbl_pass_conf")
        self.lbl_name: QLabel = self.findChild(QLabel, "lbl_name")
        self.lbl_mail: QLabel = self.findChild(QLabel, "lbl_mail")
        self.lbl_about: QLabel = self.findChild(QLabel, "lbl_about")
        self.lbl_lang: QLabel = self.findChild(QLabel, "lbl_lang")
        self.lbl_picture: QLabel = self.findChild(QLabel, "lbl_picture")

        self.lbl_pic: QLabel = self.findChild(QLabel, "lbl_pic")

        self.txt_username: QLineEdit = self.findChild(QLineEdit, "txt_username")
        self.txt_pass: QLineEdit = self.findChild(QLineEdit, "txt_pass")
        self.txt_pass_conf: QLineEdit = self.findChild(QLineEdit, "txt_pass_conf")
        self.txt_name: QLineEdit = self.findChild(QLineEdit, "txt_name")
        self.txt_mail: QLineEdit = self.findChild(QLineEdit, "txt_mail")
        self.txt_about: QTextEdit = self.findChild(QTextEdit, "txt_about")

        self.cmb_lang: QComboBox = self.findChild(QComboBox, "cmb_lang")

        self.chk_auto_pass: QCheckBox = self.findChild(QCheckBox, "chk_auto_pass")

        self.btn_file: QPushButton = self.findChild(QPushButton, "btn_file")
        self.btn_clip: QPushButton = self.findChild(QPushButton, "btn_clip")
        self.btn_save: QPushButton = self.findChild(QPushButton, "btn_save")
        self.btn_cancel: QPushButton = self.findChild(QPushButton, "btn_cancel")

        self.change_language()
        self._define_widgets_apperance()
        
    def _define_widgets_apperance(self):
        self.setWindowIcon(QIcon(self.getv("new_user_icon_path")))
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setFixedSize(730, 500)

    def change_language(self):
        self.setWindowTitle(self.getl("new_user_lbl_title_text"))
        self.lbl_title.setText(self.getl("new_user_lbl_title_text"))
        self.lbl_title.setToolTip("")
        self.lbl_username.setText(self.getl("new_user_lbl_username_text"))
        self.lbl_username.setToolTip(self.getl("new_user_lbl_username_tt"))
        self.lbl_pass.setText(self.getl("new_user_lbl_pass_text"))
        self.lbl_pass.setToolTip(self.getl("new_user_lbl_pass_tt"))
        self.lbl_pass_conf.setText(self.getl("new_user_lbl_pass_conf_text"))
        self.lbl_pass_conf.setToolTip(self.getl("new_user_lbl_pass_conf_tt"))
        self.lbl_name.setText(self.getl("new_user_lbl_name_text"))
        self.lbl_name.setToolTip(self.getl("new_user_lbl_name_tt"))
        self.lbl_mail.setText(self.getl("new_user_lbl_mail_text"))
        self.lbl_mail.setToolTip(self.getl("new_user_lbl_mail_tt"))
        self.lbl_about.setText(self.getl("new_user_lbl_about_text"))
        self.lbl_about.setToolTip(self.getl("new_user_lbl_about_tt"))
        self.lbl_lang.setText(self.getl("new_user_lbl_lang_text"))
        self.lbl_lang.setToolTip(self.getl("new_user_lbl_lang_tt"))
        self.lbl_picture.setText(self.getl("new_user_lbl_picture_text"))
        self.lbl_picture.setToolTip(self.getl("new_user_lbl_picture_tt"))
        self.lbl_pic.setText("")
        self.lbl_pic.setToolTip(self.getl("new_user_lbl_pic_tt"))

        self.chk_auto_pass.setText(self.getl("new_user_chk_auto_pass_text"))
        self.chk_auto_pass.setToolTip(self.getl("new_user_chk_auto_pass_tt"))

        self.btn_file.setText(self.getl("new_user_btn_file_text"))
        self.btn_file.setToolTip(self.getl("new_user_btn_file_tt"))
        self.btn_clip.setText(self.getl("new_user_btn_clip_text"))
        self.btn_clip.setToolTip(self.getl("new_user_btn_clip_tt"))
        self.btn_save.setText(self.getl("btn_save_text"))
        self.btn_save.setToolTip(self.getl("btn_save_tt"))
        self.btn_cancel.setText(self.getl("btn_cancel_text"))
        self.btn_cancel.setToolTip(self.getl("btn_cancel_tt"))

