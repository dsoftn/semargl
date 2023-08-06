from PyQt5.QtWidgets import (QFrame, QPushButton, QTextEdit, QScrollArea, QVBoxLayout,
    QGridLayout, QWidget, QSpacerItem, QSizePolicy, QListWidget, QFileDialog, QDialog,
    QLabel, QListWidgetItem, QDesktopWidget, QLineEdit, QCalendarWidget, QHBoxLayout, QCheckBox, QAction,
    QProgressBar, QStackedWidget, QComboBox, QApplication)
from PyQt5.QtGui import QIcon, QFont, QFontMetrics, QStaticText, QPixmap, QCursor, QTextCharFormat, QColor, QImage, QResizeEvent
from PyQt5.QtCore import (QSize, Qt, pyqtSignal, QObject, QCoreApplication, QRect,
    QPoint, QTimer, QThread, QDate)
from PyQt5 import uic, QtGui, QtCore

import threading
import socket
import datetime
import sys
import os

import chat_util_cls
import chat_settings_cls

APP_NAME = "Semargl"

theme_adaptic1 = """/*Copyright (c) DevSec Studio. All rights reserved.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/

/*-----QWidget-----*/
QWidget
{
	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(102, 115, 140, 255),stop:1 rgba(56, 63, 77, 255));
	color: #ffffff;
	border-color: #051a39;

}


/*-----QLabel-----*/
QLabel
{
	background-color: transparent;
	color: #ffffff;
	font-weight: bold;

}


QLabel::disabled
{
	background-color: transparent;
	color: #898988;

}


/*-----QMenuBar-----*/
QMenuBar
{
	background-color: #484c58;
	color: #ffffff;
	border-color: #051a39;
	font-weight: bold;

}


QMenuBar::disabled
{
	background-color: #404040;
	color: #898988;
	border-color: #051a39;

}


QMenuBar::item
{
    background-color: transparent;

}


QMenuBar::item:selected
{
    background-color: #c4c5c3;
	color: #000000;
    border: 1px solid #000000;

}


QMenuBar::item:pressed
{
    background-color: #979796;
    border: 1px solid #000;
    margin-bottom: -1px;
    padding-bottom: 1px;

}


/*-----QMenu-----*/
QMenu
{
    background-color: #c4c5c3;
    border: 1px solid;
    color: #000000;
	font-weight: bold;

}


QMenu::separator
{
    height: 1px;
    background-color: #363942;
    color: #ffffff;
    padding-left: 4px;
    margin-left: 10px;
    margin-right: 5px;

}


QMenu::item
{
    min-width : 150px;
    padding: 3px 20px 3px 20px;

}


QMenu::item:selected
{
    background-color: #363942;
    color: #ffffff;

}


QMenu::item:disabled
{
    color: #898988;
}


/*-----QToolTip-----*/
QToolTip
{
	background-color: #bbbcba;
	color: #000000;
	border-color: #051a39;
	border : 1px solid #000000;
	border-radius: 2px;

}


/*-----QPushButton-----*/
QPushButton
{
	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));
	color: #ffffff;
	font-weight: bold;
	border-style: solid;
	border-width: 1px;
	border-radius: 3px;
	border-color: #051a39;
	padding: 5px;

}


QPushButton::disabled
{
	background-color: #404040;
	color: #656565;
	border-color: #051a39;

}


QPushButton::hover
{
	background-color: #9c0000;
	color: #ffffff;
	border-style: solid;
	border-width: 1px;
	border-radius: 3px;
	border-color: #051a39;
	padding: 5px;

}


QPushButton::pressed
{
	background-color: #880000;
	color: #ffffff;
	border-style: solid;
	border-width: 2px;
	border-radius: 3px;
	border-color: #000000;
	padding: 5px;

}


/*-----QToolButton-----*/
QToolButton 
{
	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(177, 181, 193, 255),stop:1 rgba(159, 163, 174, 255));
	color: #ffffff;
	font-weight: bold;
	border-style: solid;
	border-width: 1px;
	border-radius: 3px;
	border-color: #051a39;
	padding: 5px;

}


QToolButton::disabled
{
	background-color: #404040;
	color: #656565;
	border-color: #051a39;

}


QToolButton::hover
{
	background-color: #9fa3ae;
	color: #ffffff;
	border-style: solid;
	border-width: 1px;
	border-radius: 3px;
	border-color: #051a39;
	padding: 5px;

}


QToolButton::pressed
{
	background-color: #7b7e86;
	color: #ffffff;
	border-style: solid;
	border-width: 2px;
	border-radius: 3px;
	border-color: #000000;
	padding: 5px;

}


/*-----QComboBox-----*/
QComboBox
{
    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(118, 118, 118, 255),stop:1 rgba(70, 70, 70, 255));
    border: 1px solid #333333;
    border-radius: 3px;
    padding-left: 6px;
    color: lightgray;
	font-weight: bold;
    height: 20px;

}


QComboBox::disabled
{
	background-color: #404040;
	color: #656565;
	border-color: #051a39;

}


QComboBox:hover
{
    background-color: #646464;

}


QComboBox:on
{
    background-color: #979796;
	color: #000000;

}


QComboBox QAbstractItemView
{
    background-color: #c4c5c3;
    color: #000000;
    border: 1px solid black;
    selection-background-color: #363942;
    selection-color: #ffffff;
    outline: 0;

}


QComboBox::drop-down
{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid; 
    border-top-right-radius: 3px; 
    border-bottom-right-radius: 3px;

}


QComboBox::down-arrow
{
    image: url(://arrow-down.png);
    width: 8px;
    height: 8px;
}


/*-----QSpinBox & QDoubleSpinBox & QDateTimeEdit-----*/
QSpinBox, 
QDoubleSpinBox,
QDateTimeEdit
{
	background-color: #000000;
	color: #00ff00;
	font-weight: bold;
	border: 1px solid #333333;
	padding : 4px;

}


QSpinBox::disabled, 
QDoubleSpinBox::disabled,
QDateTimeEdit::disabled
{
	background-color: #404040;
	color: #656565;
	border-color: #051a39;

}


QSpinBox:hover, 
QDoubleSpinBox::hover,
QDateTimeEdit::hover
{
    border: 1px solid #00ff00;

}


QSpinBox::up-button, QSpinBox::down-button,
QDoubleSpinBox::up-button, QDoubleSpinBox::down-button,
QDateTimeEdit::up-button, QDateTimeEdit::down-button
{
	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(118, 118, 118, 255),stop:1 rgba(70, 70, 70, 255));
    border: 0px solid #333333;

}


QSpinBox::disabled, 
QDoubleSpinBox::disabled,
QDateTimeEdit::disabled
{
	background-color: #404040;
	color: #656565;
	border-color: #051a39;

}


QSpinBox::up-button:hover, QSpinBox::down-button:hover,
QDoubleSpinBox::up-button:hover, QDoubleSpinBox::down-button:hover,
QDateTimeEdit::up-button:hover, QDateTimeEdit::down-button:hover
{
	background-color: #646464;
    border: 1px solid #333333;


}


QSpinBox::up-button:disabled, QSpinBox::down-button:disabled,
QDoubleSpinBox::up-button:disabled, QDoubleSpinBox::down-button:disabled,
QDateTimeEdit::up-button:disabled, QDateTimeEdit::down-button:disabled
{
	background-color: #404040;
	color: #656565;
	border-color: #051a39;

}


QSpinBox::up-button:pressed, QSpinBox::down-button:pressed,
QDoubleSpinBox::up-button:pressed, QDoubleSpinBox::down-button::pressed,
QDateTimeEdit::up-button:pressed, QDateTimeEdit::down-button::pressed
{
    background-color: #979796;
    border: 1px solid #444444;

}


QSpinBox::down-arrow,
QDoubleSpinBox::down-arrow,
QDateTimeEdit::down-arrow
{
    image: url(://arrow-down.png);
    width: 7px;

}


QSpinBox::up-arrow,
QDoubleSpinBox::up-arrow,
QDateTimeEdit::up-arrow
{
    image: url(://arrow-up.png);
    width: 7px;

}


/*-----QLineEdit-----*/
QLineEdit
{
	background-color: #000000;
	color: #00ff00;
	font-weight: bold;
    border: 1px solid #333333;
	padding: 4px;

}


QLineEdit:hover
{
    border: 1px solid #00ff00;

}


QLineEdit::disabled
{
	background-color: #404040;
	color: #656565;
	border-width: 1px;
	border-color: #051a39;
	padding: 2px;

}


/*-----QTextEdit-----*/
QTextEdit
{
	background-color: #808080;
	color: #fff;
	border: 1px groove #333333;

}


QTextEdit::disabled
{
	background-color: #404040;
	color: #656565;
	border-color: #051a39;

}


/*-----QGroupBox-----*/
QGroupBox 
{
    border: 1px groove #333333;
	border-radius: 2px;
    margin-top: 20px;

}


QGroupBox 
{
	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 169, 169, 255),stop:1 rgba(122, 122, 122, 255));
	font-weight: bold;

}


QGroupBox::title  
{
    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(71, 75, 87, 255),stop:1 rgba(35, 37, 43, 255));
    color: #ffffff;
    border: 2px groove #333333;
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 2px;

}


QGroupBox::title::disabled
{
	background-color: #404040;
	color: #656565;
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 5px;
	border-top-left-radius: 3px;
	border-top-right-radius: 3px;

}


/*-----QCheckBox-----*/
QCheckBox{
	background-color: transparent;
	font-weight: bold;
	color: #fff;

}


QCheckBox::indicator
{
    color: #b1b1b1;
    background-color: #323232;
    border: 2px solid #222222;
    width: 12px;
    height: 12px;

}


QCheckBox::indicator:checked
{
    image:url(://checkbox.png);
    border: 2px solid #00ff00;

}


QCheckBox::indicator:unchecked:hover
{
    border: 2px solid #00ff00;

}


QCheckBox::disabled
{
	color: #656565;

}


QCheckBox::indicator:disabled
{
	background-color: #656565;
	color: #656565;
    border: 1px solid #656565;

}


/*-----QRadioButton-----*/
QRadioButton{
	background-color: transparent;
	font-weight: bold;
	color: #fff;

}


QRadioButton::indicator::unchecked
{ 
	border: 2px inset #222222; 
	border-radius: 6px; 
	background-color:  #323232;
	width: 9px; 
	height: 9px; 

}


QRadioButton::indicator::unchecked:hover
{ 
	border: 2px solid #00ff00; 
	border-radius: 5px; 
	background-color:  #323232;
	width: 9px; 
	height: 9px; 

}


QRadioButton::indicator::checked
{ 
	border: 2px inset #222222; 
	border-radius: 5px; 
	background-color: #00ff00; 
	width: 9px; 
	height: 9px; 

}


QRadioButton::disabled
{
	color: #656565;

}


QRadioButton::indicator:disabled
{
	background-color: #656565;
	color: #656565;
    border: 2px solid #656565;

}


/*-----QTableView & QTableWidget-----*/
QTableView
{
    background-color: #808080;
    border: 1px groove #333333;
    color: #f0f0f0;
	font-weight: bold;
    gridline-color: #333333;
    outline : 0;

}


QTableView::disabled
{
    background-color: #242526;
    border: 1px solid #32414B;
    color: #656565;
    gridline-color: #656565;
    outline : 0;

}


QTableView::item:hover 
{
    background-color: #484c58;
    color: #f0f0f0;

}


QTableView::item:selected 
{
    background-color: #484c58;
    border: 2px groove #00ff00;
    color: #F0F0F0;

}


QTableView::item:selected:disabled
{
    background-color: #1a1b1c;
    border: 2px solid #525251;
    color: #656565;

}


QTableCornerButton::section
{
    background-color: #282830;

}


QHeaderView::section
{
    background-color: #282830;
    color: #fff;
	font-weight: bold;
    text-align: left;
	padding: 4px;
	
}


QHeaderView::section:disabled
{
    background-color: #525251;
    color: #656565;

}


QHeaderView::section:checked
{
    background-color: #00ff00;

}


QHeaderView::section:checked:disabled
{
    color: #656565;
    background-color: #525251;

}


QHeaderView::section::vertical::first,
QHeaderView::section::vertical::only-one
{
    border-top: 0px;

}


QHeaderView::section::vertical
{
    border-top: 0px;

}


QHeaderView::section::horizontal::first,
QHeaderView::section::horizontal::only-one
{
    border-left: 0px;

}


QHeaderView::section::horizontal
{
    border-left: 0px;

}


/*-----QTabWidget-----*/
QTabBar::tab
{
	background-color: transparent;
	color: #ffffff;
	font-weight: bold;
	width: 80px;
	height: 9px;
	
}


QTabBar::tab:disabled
{
	background-color: #656565;
	color: #656565;

}


QTabWidget::pane 
{
	background-color: transparent;
	color: #ffffff;
	border: 1px groove #333333;

}


QTabBar::tab:selected
{
    background-color: #484c58;
	color: #ffffff;
	border: 1px groove #333333;
	border-bottom: 0px;

}


QTabBar::tab:selected:disabled
{
	background-color: #404040;
	color: #656565;

}


QTabBar::tab:!selected 
{
    background-color: #a3a7b2;

}


QTabBar::tab:!selected:hover 
{
    background-color: #484c58;

}


QTabBar::tab:top:!selected 
{
    margin-top: 1px;

}


QTabBar::tab:bottom:!selected 
{
    margin-bottom: 3px;

}


QTabBar::tab:top, QTabBar::tab:bottom 
{
    min-width: 8ex;
    margin-right: -1px;
    padding: 5px 10px 5px 10px;

}


QTabBar::tab:top:selected 
{
    border-bottom-color: none;

}


QTabBar::tab:bottom:selected 
{
    border-top-color: none;

}


QTabBar::tab:top:last, QTabBar::tab:bottom:last,
QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one 
{
    margin-right: 0;

}


QTabBar::tab:left:!selected 
{
    margin-right: 2px;

}


QTabBar::tab:right:!selected
{
    margin-left: 2px;

}


QTabBar::tab:left, QTabBar::tab:right 
{
    min-height: 15ex;
    margin-bottom: -1px;
    padding: 10px 5px 10px 5px;

}


QTabBar::tab:left:selected 
{
    border-left-color: none;

}


QTabBar::tab:right:selected 
{
    border-right-color: none;

}


QTabBar::tab:left:last, QTabBar::tab:right:last,
QTabBar::tab:left:only-one, QTabBar::tab:right:only-one 
{
    margin-bottom: 0;

}


/*-----QSlider-----*/
QSlider{
	background-color: transparent;

}


QSlider::groove:horizontal 
{
	background-color: transparent;
	height: 6px;

}


QSlider::sub-page:horizontal 
{
	background-color: qlineargradient(spread:reflect, x1:1, y1:0, x2:1, y2:1, stop:0.00480769 rgba(201, 201, 201, 255),stop:1 rgba(72, 72, 72, 255));
	border: 1px solid #000;

}


QSlider::add-page:horizontal 
{
	background-color: #404040;
	border: 1px solid #000; 

}


QSlider::handle:horizontal 
{
	background-color: qlineargradient(spread:reflect, x1:1, y1:0, x2:1, y2:1, stop:0.00480769 rgba(201, 201, 201, 255),stop:1 rgba(72, 72, 72, 255));
	border: 1px solid #000; 
	width: 12px;
	margin-top: -6px;
	margin-bottom: -6px;

}


QSlider::handle:horizontal:hover 
{
	background-color: #808080;

}


QSlider::sub-page:horizontal:disabled 
{
	background-color: #bbb;
	border-color: #999;

}


QSlider::add-page:horizontal:disabled 
{
	background-color: #eee;
	border-color: #999;

}


QSlider::handle:horizontal:disabled 
{
	background-color: #eee;
	border: 1px solid #aaa;

}


QSlider::groove:vertical 
{
	background-color: transparent;
	width: 6px;

}


QSlider::sub-page:vertical 
{
	background-color: qlineargradient(spread:reflect, x1:0, y1:0.483, x2:1, y2:0.517, stop:0.00480769 rgba(201, 201, 201, 255),stop:1 rgba(72, 72, 72, 255));
	border: 1px solid #000;

}


QSlider::add-page:vertical 
{
	background-color: #404040;
	border: 1px solid #000;

}


QSlider::handle:vertical 
{
	background-color: qlineargradient(spread:reflect, x1:0, y1:0.483, x2:1, y2:0.517, stop:0.00480769 rgba(201, 201, 201, 255),stop:1 rgba(72, 72, 72, 255));
	border: 1px solid #000;
	height: 12px;
	margin-left: -6px;
	margin-right: -6px;

}


QSlider::handle:vertical:hover 
{
	background-color: #808080;

}


QSlider::sub-page:vertical:disabled 
{
	background-color: #bbb;
	border-color: #999;

}


QSlider::add-page:vertical:disabled 
{
	background-color: #eee;
	border-color: #999;

}


QSlider::handle:vertical:disabled 
{
	background-color: #eee;
	border: 1px solid #aaa;
	border-radius: 3px;

}


/*-----QDial-----*/
QDial
{
	background-color: #600000;

}


QDial::disabled
{
	background-color: #404040;

}


/*-----QScrollBar-----*/
QScrollBar:horizontal
{
    border: 1px solid #222222;
    background-color: #63676d;
    height: 18px;
    margin: 0px 18px 0 18px;

}


QScrollBar::handle:horizontal
{
    background-color: #a6acb3;
	border: 1px solid #656565;
	border-radius: 2px;
    min-height: 20px;

}


QScrollBar::add-line:horizontal
{
    border: 1px solid #1b1b19;
    background-color: #a6acb3;
    width: 18px;
    subcontrol-position: right;
    subcontrol-origin: margin;

}


QScrollBar::sub-line:horizontal
{
    border: 1px solid #1b1b19;
    background-color: #a6acb3;
    width: 18px;
    subcontrol-position: left;
    subcontrol-origin: margin;

}


QScrollBar::right-arrow:horizontal
{
    image: url(://arrow-right.png);
    width: 8px;
    height: 8px;

}


QScrollBar::left-arrow:horizontal
{
    image: url(://arrow-left.png);
    width: 8px;
    height: 8px;

}


QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
    background: none;

}


QScrollBar:vertical
{
    background-color: #63676d;
    width: 18px;
    margin: 18px 0 18px 0;
    border: 1px solid #222222;

}


QScrollBar::handle:vertical
{
    background-color: #a6acb3;
	border: 1px solid #656565;
	border-radius: 2px;
    min-height: 20px;

}


QScrollBar::add-line:vertical
{
    border: 1px solid #1b1b19;
    background-color: #a6acb3;
    height: 18px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;

}


QScrollBar::sub-line:vertical
{
    border: 1px solid #1b1b19;
    background-color: #a6acb3;
    height: 18px;
    subcontrol-position: top;
    subcontrol-origin: margin;

}


QScrollBar::up-arrow:vertical
{
    image: url(://arrow-up.png);
    width: 8px;
    height: 8px;

}


QScrollBar::down-arrow:vertical
{
    image: url(://arrow-down.png);
    width: 8px;
    height: 8px;

}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
    background: none;

}


/*-----QProgressBar-----*/
QProgressBar
{
	background-color: #000;
	color: #00ff00;
	font-weight: bold;
	border: 0px groove #000;
	border-radius: 10px;
	text-align: center;

}


QProgressBar:disabled
{
	background-color: #404040;
	color: #656565;
	border-color: #051a39;
	border: 1px solid #000;
	border-radius: 10px;
	text-align: center;

}


QProgressBar::chunk {
	background-color: #ffaf02;
	border: 0px;
	border-radius: 10px;
	color: #000;

}


QProgressBar::chunk:disabled {
	background-color: #333;
	border: 0px;
	border-radius: 10px;
	color: #656565;
}


/*-----QStatusBar-----*/
QStatusBar
{
	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(102, 115, 140, 255),stop:1 rgba(56, 63, 77, 255));
	color: #ffffff;
	border-color: #051a39;
	font-weight: bold;

}


"""

theme_adaptic2 = """/*Copyright (c) DevSec Studio. All rights reserved.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

/*-----QWidget-----*/
QWidget
{
	background-color: #878d8b;
	color: #000000;
	border-color: #000000;

}


/*-----QMenuBar-----*/
QMenuBar
{
	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(61, 61, 61, 255),stop:0.514423 rgba(89, 89, 89, 255),stop:1 rgba(98, 98, 98, 255));
	color: #cccccc;
	border-color: #000000;

}


QMenuBar::item
{
    background-color: transparent;

}


QMenuBar::item:selected
{
	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(139, 139, 139, 255),stop:0.514423 rgba(89, 89, 89, 255),stop:1 rgba(152, 152, 152, 255));
	color: #fff;

}


QMenuBar::item:pressed
{
    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(39, 39, 39, 255),stop:0.514423 rgba(89, 89, 89, 255),stop:1 rgba(52, 52, 52, 255));
    border: 1px solid #5ab8a0;
    margin-bottom: -1px;
    padding-bottom: 1px;

}


/*-----QMenu-----*/
QMenu
{
    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(61, 61, 61, 255),stop:0.514423 rgba(89, 89, 89, 255),stop:1 rgba(78, 78, 78, 255));
    border: 1px solid;
    color: lightgray;

}


QMenu::separator
{
    height: 1px;
    background-color: #000;
    color: #ffffff;
    padding-left: 4px;
    margin-left: 10px;
    margin-right: 5px;

}


QMenu::item
{
    min-width : 150px;
    padding: 3px 20px 3px 20px;

}


QMenu::item:selected
{
    background-color: #cdceb1;
    color: #000;

}


/*-----QPushButton-----*/
QPushButton
{
	background-color: #cdceb1;
	color: #000000;
	border-style: solid;
	border-width: 1px;
	border-radius: 4px;
	border-color: #dfdfc0;
	margin: 2px;

}


/*-----QLineEdit-----*/
QLineEdit
{
	background-color: #a6d072;
	color: #000000;
	border-style: solid;
	border-width: 1px;
	border-radius: 4px;
	border-color: #000000;
	font-family: "Azonix";

}


"""

theme_adaptic = """/*Copyright (c) DevSec Studio. All rights reserved.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

/*-----QWidget-----*/
QWidget
{
	background-color: #d4d5d2;
	color: #ffffff;
	border-color: #000000;

}


/*-----QLabel-----*/
QLabel
{
	background-color: transparent;
	color: #000;
	border-color: #000000;

}


/*-----QToolTip-----*/
QToolTip
{
	background-color: #fff;
	color: #1ea2ff;
	border: 1px solid #000;
	font-weight: bold;

}


/*-----QToolButton-----*/
QPushButton
{
	background-color: #1ea2ff;
	color: #000000;
	font-weight: bold;
	border: 0px solid;
	border-radius: 2px;

}


QPushButton::hover
{
	background-color:#2ea9ff;   

}


QPushButton::pressed
{
	background-color: #1988d6;

}


QPushButton::checked
{
	background-color: #1988d6;

}


/*-----QToolButton-----*/
QToolButton
{
	background-color: #1ea2ff;
	color: #000000;
	font-weight: bold;
	border: 0px solid;
	border-radius: 2px;

}


QToolButton::hover
{
	background-color: #2ea9ff;  

}


QToolButton::pressed
{
	background-color: #1988d6;

}


QToolButton::checked
{
	background-color: #1988d6;

}


/*-----QLineEdit-----*/
QLineEdit
{
	background-color: white;
	color: #000000;
	padding: 3px;
	border: 1px solid #1ea2ff;
	border-radius: 2px;
	selection-background-color: #0949ff;

}


QLineEdit::focus
{
	padding: 3px;
	border: 1px solid #1ea2ff;
	border-radius: 2px;

}


/*-----QTextEdit-----*/
QTextEdit
{
	background-color: white;
	color: #000;
	border-color: #000000;
	border: 1px solid #1ea2ff;
	border-radius: 2px;

}


/*-----QListView-----*/
QListView
{
	background-color: transparent;
	color: #000;
	border: 0px solid;
	border-radius: 2px;
	font-weight: bold;

}


QListView::item 
{
    padding: 5px;

}


QListView::item:selected 
{
    border: 1px solid #1ea2ff;
    border-radius: 2px;
    color: #fff;
}


QListView::item:selected:!active 
{
    background-color: #1ea2ff;
    border-radius: 2px;
    color: #fff;

}


QListView::item:selected:active 
{
    background-color: #1ea2ff;
    border-radius: 2px;
    color: #fff;

}


QListView::item:hover 
{
    background-color: #8b8b8b;
	margin: 0px;
    border-radius: 2px;

}


/*-----QScrollBar-----*/
QScrollBar:vertical 
{
	border-radius : 5px;
	width: 10px;

}


QScrollBar:horizontal 
{
	border-radius : 5px;
	height: 10px;

}


QScrollBar::handle:vertical,
QScrollBar::handle:horizontal
{
	border-radius : 5px;
	background-color: #1ea2ff;
	min-height: 80px;
	width : 12px;

}


QScrollBar::handle:vertical:hover,
QScrollBar::handle:horizontal:hover
{
	background-color: #1988d6; 

}


QScrollBar::add-line:vertical,
QScrollBar::add-line:horizontal
{
	background: transparent;
	height: 0px;
	subcontrol-position: bottom;
	subcontrol-origin: margin;

}


QScrollBar::add-line:vertical:hover,
QScrollBar::add-line:horizontal:hover
{
	background-color: transparent;

}


QScrollBar::add-line:vertical:pressed, 
QScrollBar::add-line:horizontal:pressed
{
	background-color: #3f3f3f;

}


QScrollBar::sub-line:vertical,
QScrollBar::sub-line:horizontal
{
	background: transparent;
	height: 0px;

}


QScrollBar::sub-line:vertical:hover,
QScrollBar::sub-line:horizontal:hover
{
	background-color: transparent;

}


QScrollBar::sub-line:vertical:pressed,
QScrollBar::sub-line:horizontal:pressed
{
	background-color: #3f3f3f;

}


QScrollBar::up-arrow:vertical,
QScrollBar::up-arrow:horizontal
{
	width: 0px;
	height: 0px;
	background: transparent;

}


QScrollBar::down-arrow:vertical, 
QScrollBar::down-arrow:horizontal
{
	width: 0px;
	height: 0px;
	background: transparent;

}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
	background-color: white;
	
}
"""


class ClientStandAlone(QDialog):
    """This is the stand-alone main client window.
    Use this class if you want full functionality without integrating a graphical interface into your application.
    Usage:
        from chat_client_cls import ClientStandAlone
        ClientStandAlone.show_gui()
    """
    def __init__(self, parent_widget: QWidget = None, application_modal: bool = False, *args, **kwargs):
        super().__init__(parent_widget, *args, **kwargs)
        
        if application_modal:
            self.setWindowModality(Qt.ApplicationModal)
    
        # Define settings class and methods
        self._stt = chat_settings_cls.Settings()
        self.getv = self._stt.get_setting_value
        self.setv = self._stt.set_setting_value
        self.getl = self._stt.lang
        self.get_appv = self._stt.app_setting_get_value
        self.set_appv = self._stt.app_setting_set_value

        # Define variables
        
        self._define_widgets_apperance()

        # Load Client class
        self.content = ClientGUI(settings=self._stt, parent_widget=self)
        self.content.start_gui()

    def show_gui(self):

        self.show()

    def resizeEvent(self, a0: QResizeEvent) -> None:
        self.content.resize(self.contentsRect().width(), self.contentsRect().height())
        return super().resizeEvent(a0)

    def _define_widgets_apperance(self):
        self.setWindowIcon(QIcon(self.getv("stand_alone_win_icon_path")))
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowTitle(APP_NAME)



class ClientGUI(QFrame):
    def __init__(self,
                 settings: chat_settings_cls.Settings = None,
                 parent_widget: QWidget = None,
                 username: str = None,
                 password: str = None,
                 *args, **kwargs
                 ) -> None:
        super().__init__(parent_widget, *args, **kwargs)

        # Define settings class and methods
        if isinstance(settings, chat_settings_cls.Settings):
            self._stt = settings
        else:
            self._stt = chat_settings_cls.Settings()
        self.getv = self._stt.get_setting_value
        self.setv = self._stt.set_setting_value
        self.getl = self._stt.lang
        self.get_appv = self._stt.app_setting_get_value
        self.set_appv = self._stt.app_setting_set_value

        self._stt.app_setting_add("signal", chat_util_cls.Signal(self._stt))
        self._stt.app_setting_add("menu", {})
        self._stt.app_setting_add("util", chat_util_cls.Utilities(self._stt))
        self._stt.app_setting_add("user", chat_util_cls.User(self._stt, username=username, password=password))

        # Set active language
        self._stt.ActiveLanguageID = self.getv("last_language_ID")

        # Load designer GUI file
        uic.loadUi(self.getv("client_ui_file_path"), self)

        # Define variables
        self._parent_widget = parent_widget
        self.user: chat_util_cls.User = self.get_appv("user")
        self.util: chat_util_cls.Utilities = self.get_appv("util")
        self.signal: chat_util_cls.Signal = self.get_appv("signal")

        self._drag_mode = None  # Enables dragging the window by clicking on the username or avatar
        if isinstance(self._parent_widget, ClientStandAlone):
            self._drag_mode_enabled = True
        else:
            self._drag_mode_enabled = False

        # Setup widgets and load user
        self._define_widgets()

        # Connect events with slots
        self._connect_signals()        


    def start_gui(self):
        self.show()
        app.processEvents()
        if self.user.is_user_autoloading(username=self.getv("last_user")):
            self.user.load_user(username=self.getv("last_user"))
        if not self.user.is_user_loaded():
            loged_user = self.user_login()

    def _connect_signals(self):
        self.signal.signal_language_changed.connect(self.change_language)

    def user_login(self, username: str = None, password: str = None) -> str:
        # Start login
        # Result will be in app_setting "user"
        if self.user.is_user_loaded():
            print ("Attempted new user login while a logged in user exists. If you want to log in a new user, the existing user must be logged out.")
            return
        login_win = chat_util_cls.Login(self._stt, self, username=username, password=password, application_modal=True)
        return login_win.start_gui()

    def _define_widgets(self):
        self.lbl_user_avatar: QLabel = self.findChild(QLabel, "lbl_user_avatar")
        self.lbl_user_nick: QLabel = self.findChild(QLabel, "lbl_user_nick")
        self.lbl_user_connected: QLabel = self.findChild(QLabel, "lbl_user_connected")

        self.btn_connect: QPushButton = self.findChild(QPushButton, "btn_connect")
        self.btn_setup: QPushButton = self.findChild(QPushButton, "btn_setup")
        self.btn_language: QPushButton = self.findChild(QPushButton, "btn_language")

        self.area_contacts: QScrollArea = self.findChild(QScrollArea, "area_contacts")
        
        self._define_widgets_text()


    def _define_widgets_text(self):
        self.lbl_user_avatar.setText("")
        self.lbl_user_nick.setText("")
        self.lbl_user_connected.setText(self.getl("cl_GUI_lbl_user_connected_not_conected_text"))
        self.lbl_user_connected.setToolTip(self.getl("cl_GUI_lbl_user_connected_not_conected_tt"))



    def change_language(self):
        print ("Lang changed")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyleSheet(theme_adaptic1)

    client_win = ClientStandAlone(parent_widget=None, application_modal=False)
    client_win.show_gui()

    sys.exit(app.exec_())

