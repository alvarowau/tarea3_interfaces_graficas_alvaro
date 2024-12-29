# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_reserva.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QWidget)

class Ui_window_reserva(object):
    def setupUi(self, window_reserva):
        if not window_reserva.objectName():
            window_reserva.setObjectName(u"window_reserva")
        window_reserva.resize(481, 761)
        window_reserva.setMinimumSize(QSize(481, 761))
        window_reserva.setMaximumSize(QSize(481, 761))
        self.a_frame = QFrame(window_reserva)
        self.a_frame.setObjectName(u"a_frame")
        self.a_frame.setGeometry(QRect(0, 0, 481, 761))
        self.a_frame.setMinimumSize(QSize(481, 761))
        self.a_frame.setMaximumSize(QSize(481, 761))
        self.a_frame.setStyleSheet(u"QWidget {\n"
"    background-color: #F8F9FA; \n"
"    font-family: \"Segoe UI\", Arial, sans-serif; \n"
"    font-size: 14px; \n"
"    color: #333333; \n"
"}\n"
"QLabel {\n"
"    font-weight: bold; \n"
"    color: #2A9D8F; \n"
"    font-size: 12px; \n"
"}\n"
"QLineEdit {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"    selection-background-color: #2A9D8F; \n"
"    selection-color: #FFFFFF; \n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"    color: #333333; \n"
"}\n"
"QPushButton {\n"
"    background-color: #2A9D8F; \n"
"    color: #FFFFFF; \n"
"    border-radius: 8px; \n"
"    padding: 6px 12px; \n"
"    font-size: 14px; \n"
"    border: 2px solid #2A9D8F; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A4C639; "
                        "\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #207567; \n"
"    border: 2px solid #207567; \n"
"}\n"
"QComboBox {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #FFFFFF; \n"
"    selection-background-color: #2A9D8F; \n"
"    selection-color: #FFFFFF; \n"
"}\n"
"QSpinBox {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid "
                        "#2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}\n"
"QRadioButton {\n"
"    color: #333333; \n"
"    font-size: 12px; \n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 6px; \n"
"    width: 12px; \n"
"    height: 12px; \n"
"    background: #FFFFFF; \n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background: #2A9D8F; \n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    margin-top: 10px; \n"
"    font-weight: bold; \n"
"    font-size: 12px; \n"
"    color: #2A9D8F; \n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top center; \n"
"    padding: 0 10px; \n"
"    background-color: #FFFFFF; \n"
"}\n"
"QDateEdit {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size:"
                        " 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}")
        self.a_frame.setFrameShape(QFrame.StyledPanel)
        self.a_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.a_frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.a_widget_title = QWidget(self.a_frame)
        self.a_widget_title.setObjectName(u"a_widget_title")
        self.a_widget_title.setStyleSheet(u"QWidget {\n"
"    background-color: #F8F9FA; \n"
"    font-family: \"Segoe UI\", Arial, sans-serif; \n"
"    font-size: 14px; \n"
"    color: #333333; \n"
"}\n"
"QLabel {\n"
"    font-weight: bold; \n"
"    color: #2A9D8F; \n"
"    font-size: 12px; \n"
"}\n"
"QLineEdit {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"    selection-background-color: #2A9D8F; \n"
"    selection-color: #FFFFFF; \n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"    color: #333333; \n"
"}\n"
"QPushButton {\n"
"    background-color: #2A9D8F; \n"
"    color: #FFFFFF; \n"
"    border-radius: 8px; \n"
"    padding: 6px 12px; \n"
"    font-size: 14px; \n"
"    border: 2px solid #2A9D8F; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A4C639; "
                        "\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #207567; \n"
"    border: 2px solid #207567; \n"
"}\n"
"QComboBox {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #FFFFFF; \n"
"    selection-background-color: #2A9D8F; \n"
"    selection-color: #FFFFFF; \n"
"}\n"
"QSpinBox {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid "
                        "#2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}\n"
"QRadioButton {\n"
"    color: #333333; \n"
"    font-size: 12px; \n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 6px; \n"
"    width: 12px; \n"
"    height: 12px; \n"
"    background: #FFFFFF; \n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background: #2A9D8F; \n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    margin-top: 10px; \n"
"    font-weight: bold; \n"
"    font-size: 12px; \n"
"    color: #2A9D8F; \n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top center; \n"
"    padding: 0 10px; \n"
"    background-color: #FFFFFF; \n"
"}\n"
"QDateEdit {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size:"
                        " 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}")
        self.gridLayout = QGridLayout(self.a_widget_title)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_11 = QSpacerItem(120, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)

        self.a_label_title = QLabel(self.a_widget_title)
        self.a_label_title.setObjectName(u"a_label_title")
        self.a_label_title.setStyleSheet(u"QLabel{\n"
"    font-size: 24px; \n"
"    font-weight: bold; \n"
"    color: #2A9D8F; \n"
"    background-color: transparent; \n"
"    border: none; \n"
"    text-align: center; \n"
"    padding: 10px;\n"
"    text-transform: uppercase; \n"
"    letter-spacing: 2px; \n"
"}")

        self.gridLayout.addWidget(self.a_label_title, 0, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(120, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_12, 0, 2, 1, 1)


        self.gridLayout_7.addWidget(self.a_widget_title, 0, 0, 1, 1)

        self.a_widget_tipo_reserva = QWidget(self.a_frame)
        self.a_widget_tipo_reserva.setObjectName(u"a_widget_tipo_reserva")
        self.a_widget_tipo_reserva.setStyleSheet(u"QWidget {\n"
"    background-color: #F8F9FA; \n"
"    font-family: \"Segoe UI\", Arial, sans-serif; \n"
"    font-size: 14px; \n"
"    color: #333333; \n"
"}\n"
"QLabel {\n"
"    font-weight: bold; \n"
"    color: #2A9D8F; \n"
"    font-size: 12px; \n"
"}\n"
"QLineEdit {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"    selection-background-color: #2A9D8F; \n"
"    selection-color: #FFFFFF; \n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"    color: #333333; \n"
"}\n"
"QPushButton {\n"
"    background-color: #2A9D8F; \n"
"    color: #FFFFFF; \n"
"    border-radius: 8px; \n"
"    padding: 6px 12px; \n"
"    font-size: 14px; \n"
"    border: 2px solid #2A9D8F; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A4C639; "
                        "\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #207567; \n"
"    border: 2px solid #207567; \n"
"}\n"
"QComboBox {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #FFFFFF; \n"
"    selection-background-color: #2A9D8F; \n"
"    selection-color: #FFFFFF; \n"
"}\n"
"QSpinBox {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid "
                        "#2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}\n"
"QRadioButton {\n"
"    color: #333333; \n"
"    font-size: 12px; \n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 6px; \n"
"    width: 12px; \n"
"    height: 12px; \n"
"    background: #FFFFFF; \n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background: #2A9D8F; \n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    margin-top: 10px; \n"
"    font-weight: bold; \n"
"    font-size: 12px; \n"
"    color: #2A9D8F; \n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top center; \n"
"    padding: 0 10px; \n"
"    background-color: #FFFFFF; \n"
"}\n"
"QDateEdit {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size:"
                        " 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}")
        self.gridLayout_2 = QGridLayout(self.a_widget_tipo_reserva)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.a_label_title_type = QLabel(self.a_widget_tipo_reserva)
        self.a_label_title_type.setObjectName(u"a_label_title_type")
        self.a_label_title_type.setStyleSheet(u"QLabel {\n"
"     font-size: 14px; \n"
"    font-weight: 600; \n"
"    color: #555555; \n"
"    background-color: transparent; \n"
"    border: none; \n"
"    text-align: left; \n"
"    padding: 2px; \n"
"    border-bottom: 2px solid #CCCCCC; \n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.a_label_title_type, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(357, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.a_label_type_reserva = QLabel(self.a_widget_tipo_reserva)
        self.a_label_type_reserva.setObjectName(u"a_label_type_reserva")

        self.gridLayout_2.addWidget(self.a_label_type_reserva, 1, 0, 1, 1)

        self.a_comboBox_tipe_reserva = QComboBox(self.a_widget_tipo_reserva)
        self.a_comboBox_tipe_reserva.setObjectName(u"a_comboBox_tipe_reserva")
        self.a_comboBox_tipe_reserva.setMinimumSize(QSize(220, 33))
        self.a_comboBox_tipe_reserva.setMaximumSize(QSize(220, 33))

        self.gridLayout_2.addWidget(self.a_comboBox_tipe_reserva, 1, 1, 1, 1)


        self.gridLayout_7.addWidget(self.a_widget_tipo_reserva, 1, 0, 1, 1)

        self.a_widget_datas_person = QWidget(self.a_frame)
        self.a_widget_datas_person.setObjectName(u"a_widget_datas_person")
        self.a_widget_datas_person.setStyleSheet(u"QWidget {\n"
"    background-color: #F8F9FA; \n"
"    font-family: \"Segoe UI\", Arial, sans-serif; \n"
"    font-size: 14px; \n"
"    color: #333333; \n"
"}\n"
"QLabel {\n"
"    font-weight: bold; \n"
"    color: #2A9D8F; \n"
"    font-size: 12px; \n"
"}\n"
"QLineEdit {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"    selection-background-color: #2A9D8F; \n"
"    selection-color: #FFFFFF; \n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"    color: #333333; \n"
"}\n"
"QPushButton {\n"
"    background-color: #2A9D8F; \n"
"    color: #FFFFFF; \n"
"    border-radius: 8px; \n"
"    padding: 6px 12px; \n"
"    font-size: 14px; \n"
"    border: 2px solid #2A9D8F; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A4C639; "
                        "\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #207567; \n"
"    border: 2px solid #207567; \n"
"}\n"
"QComboBox {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #FFFFFF; \n"
"    selection-background-color: #2A9D8F; \n"
"    selection-color: #FFFFFF; \n"
"}\n"
"QSpinBox {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid "
                        "#2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}\n"
"QRadioButton {\n"
"    color: #333333; \n"
"    font-size: 12px; \n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 6px; \n"
"    width: 12px; \n"
"    height: 12px; \n"
"    background: #FFFFFF; \n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background: #2A9D8F; \n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    margin-top: 10px; \n"
"    font-weight: bold; \n"
"    font-size: 12px; \n"
"    color: #2A9D8F; \n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top center; \n"
"    padding: 0 10px; \n"
"    background-color: #FFFFFF; \n"
"}\n"
"QDateEdit {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size:"
                        " 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}")
        self.gridLayout_3 = QGridLayout(self.a_widget_datas_person)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.a_label_phone = QLabel(self.a_widget_datas_person)
        self.a_label_phone.setObjectName(u"a_label_phone")

        self.gridLayout_3.addWidget(self.a_label_phone, 2, 0, 1, 1)

        self.a_lineEdit_name = QLineEdit(self.a_widget_datas_person)
        self.a_lineEdit_name.setObjectName(u"a_lineEdit_name")
        self.a_lineEdit_name.setMaximumSize(QSize(220, 33))

        self.gridLayout_3.addWidget(self.a_lineEdit_name, 1, 1, 1, 1)

        self.a_lineEdit_phone = QLineEdit(self.a_widget_datas_person)
        self.a_lineEdit_phone.setObjectName(u"a_lineEdit_phone")
        self.a_lineEdit_phone.setMaximumSize(QSize(220, 33))

        self.gridLayout_3.addWidget(self.a_lineEdit_phone, 2, 1, 1, 1)

        self.a_label_name = QLabel(self.a_widget_datas_person)
        self.a_label_name.setObjectName(u"a_label_name")

        self.gridLayout_3.addWidget(self.a_label_name, 1, 0, 1, 1)

        self.a_label_title_person = QLabel(self.a_widget_datas_person)
        self.a_label_title_person.setObjectName(u"a_label_title_person")
        self.a_label_title_person.setStyleSheet(u"QLabel {\n"
"     font-size: 14px; \n"
"    font-weight: 600; \n"
"    color: #555555; \n"
"    background-color: transparent; \n"
"    border: none; \n"
"    text-align: left; \n"
"    padding: 2px; \n"
"    border-bottom: 2px solid #CCCCCC; \n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.a_label_title_person, 0, 0, 1, 2)


        self.gridLayout_7.addWidget(self.a_widget_datas_person, 2, 0, 1, 1)

        self.a_widget_reservas = QWidget(self.a_frame)
        self.a_widget_reservas.setObjectName(u"a_widget_reservas")
        self.a_widget_reservas.setStyleSheet(u"QWidget {\n"
"    background-color: #F8F9FA; \n"
"    font-family: \"Segoe UI\", Arial, sans-serif; \n"
"    font-size: 14px; \n"
"    color: #333333; \n"
"}\n"
"QLabel {\n"
"    font-weight: bold; \n"
"    color: #2A9D8F; \n"
"    font-size: 12px; \n"
"}\n"
"QLineEdit {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"    selection-background-color: #2A9D8F; \n"
"    selection-color: #FFFFFF; \n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"    color: #333333; \n"
"}\n"
"QPushButton {\n"
"    background-color: #2A9D8F; \n"
"    color: #FFFFFF; \n"
"    border-radius: 8px; \n"
"    padding: 6px 12px; \n"
"    font-size: 14px; \n"
"    border: 2px solid #2A9D8F; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A4C639; "
                        "\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #207567; \n"
"    border: 2px solid #207567; \n"
"}\n"
"QComboBox {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #FFFFFF; \n"
"    selection-background-color: #2A9D8F; \n"
"    selection-color: #FFFFFF; \n"
"}\n"
"QSpinBox {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid "
                        "#2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}\n"
"QRadioButton {\n"
"    color: #333333; \n"
"    font-size: 12px; \n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 6px; \n"
"    width: 12px; \n"
"    height: 12px; \n"
"    background: #FFFFFF; \n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background: #2A9D8F; \n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    margin-top: 10px; \n"
"    font-weight: bold; \n"
"    font-size: 12px; \n"
"    color: #2A9D8F; \n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top center; \n"
"    padding: 0 10px; \n"
"    background-color: #FFFFFF; \n"
"}\n"
"QDateEdit {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size:"
                        " 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}")
        self.gridLayout_4 = QGridLayout(self.a_widget_reservas)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.a_label_title_reserva = QLabel(self.a_widget_reservas)
        self.a_label_title_reserva.setObjectName(u"a_label_title_reserva")
        self.a_label_title_reserva.setStyleSheet(u"QLabel {\n"
"     font-size: 14px; \n"
"    font-weight: 600; \n"
"    color: #555555; \n"
"    background-color: transparent; \n"
"    border: none; \n"
"    text-align: left; \n"
"    padding: 2px; \n"
"    border-bottom: 2px solid #CCCCCC; \n"
"}")

        self.gridLayout_4.addWidget(self.a_label_title_reserva, 0, 0, 1, 2)

        self.a_label_date = QLabel(self.a_widget_reservas)
        self.a_label_date.setObjectName(u"a_label_date")

        self.gridLayout_4.addWidget(self.a_label_date, 1, 0, 1, 1)

        self.a_dateEdit_date = QDateEdit(self.a_widget_reservas)
        self.a_dateEdit_date.setObjectName(u"a_dateEdit_date")
        self.a_dateEdit_date.setMinimumSize(QSize(220, 33))

        self.gridLayout_4.addWidget(self.a_dateEdit_date, 1, 1, 1, 1)

        self.a_label_type_salon = QLabel(self.a_widget_reservas)
        self.a_label_type_salon.setObjectName(u"a_label_type_salon")

        self.gridLayout_4.addWidget(self.a_label_type_salon, 2, 0, 1, 1)

        self.a_comboBox_salon = QComboBox(self.a_widget_reservas)
        self.a_comboBox_salon.setObjectName(u"a_comboBox_salon")
        self.a_comboBox_salon.setMinimumSize(QSize(220, 33))

        self.gridLayout_4.addWidget(self.a_comboBox_salon, 2, 1, 1, 1)

        self.a_label_asistent = QLabel(self.a_widget_reservas)
        self.a_label_asistent.setObjectName(u"a_label_asistent")

        self.gridLayout_4.addWidget(self.a_label_asistent, 3, 0, 1, 1)

        self.a_spinBox_asistans = QSpinBox(self.a_widget_reservas)
        self.a_spinBox_asistans.setObjectName(u"a_spinBox_asistans")
        self.a_spinBox_asistans.setMinimumSize(QSize(70, 33))
        self.a_spinBox_asistans.setMaximumSize(QSize(70, 33))

        self.gridLayout_4.addWidget(self.a_spinBox_asistans, 3, 1, 1, 1)

        self.a_label_tipo_cocina = QLabel(self.a_widget_reservas)
        self.a_label_tipo_cocina.setObjectName(u"a_label_tipo_cocina")

        self.gridLayout_4.addWidget(self.a_label_tipo_cocina, 4, 0, 1, 1)

        self.a_comboBox_cocina = QComboBox(self.a_widget_reservas)
        self.a_comboBox_cocina.setObjectName(u"a_comboBox_cocina")
        self.a_comboBox_cocina.setMinimumSize(QSize(220, 33))

        self.gridLayout_4.addWidget(self.a_comboBox_cocina, 4, 1, 1, 1)


        self.gridLayout_7.addWidget(self.a_widget_reservas, 3, 0, 1, 1)

        self.a_widget_data_congres = QWidget(self.a_frame)
        self.a_widget_data_congres.setObjectName(u"a_widget_data_congres")
        self.a_widget_data_congres.setStyleSheet(u"QWidget {\n"
"    background-color: #F8F9FA; \n"
"    font-family: \"Segoe UI\", Arial, sans-serif; \n"
"    font-size: 14px; \n"
"    color: #333333; \n"
"}\n"
"QLabel {\n"
"    font-weight: bold; \n"
"    color: #2A9D8F; \n"
"    font-size: 12px; \n"
"}\n"
"QLineEdit {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"    selection-background-color: #2A9D8F; \n"
"    selection-color: #FFFFFF; \n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"    color: #333333; \n"
"}\n"
"QPushButton {\n"
"    background-color: #2A9D8F; \n"
"    color: #FFFFFF; \n"
"    border-radius: 8px; \n"
"    padding: 6px 12px; \n"
"    font-size: 14px; \n"
"    border: 2px solid #2A9D8F; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A4C639; "
                        "\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #207567; \n"
"    border: 2px solid #207567; \n"
"}\n"
"QComboBox {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #FFFFFF; \n"
"    selection-background-color: #2A9D8F; \n"
"    selection-color: #FFFFFF; \n"
"}\n"
"QSpinBox {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid "
                        "#2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}\n"
"QRadioButton {\n"
"    color: #333333; \n"
"    font-size: 12px; \n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 6px; \n"
"    width: 12px; \n"
"    height: 12px; \n"
"    background: #FFFFFF; \n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background: #2A9D8F; \n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    margin-top: 10px; \n"
"    font-weight: bold; \n"
"    font-size: 12px; \n"
"    color: #2A9D8F; \n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top center; \n"
"    padding: 0 10px; \n"
"    background-color: #FFFFFF; \n"
"}\n"
"QDateEdit {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size:"
                        " 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}")
        self.gridLayout_5 = QGridLayout(self.a_widget_data_congres)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.a_label_title_congres = QLabel(self.a_widget_data_congres)
        self.a_label_title_congres.setObjectName(u"a_label_title_congres")
        self.a_label_title_congres.setStyleSheet(u"QLabel {\n"
"     font-size: 14px; \n"
"    font-weight: 600; \n"
"    color: #555555; \n"
"    background-color: transparent; \n"
"    border: none; \n"
"    text-align: left; \n"
"    padding: 2px; \n"
"    border-bottom: 2px solid #CCCCCC; \n"
"}")

        self.gridLayout_5.addWidget(self.a_label_title_congres, 0, 0, 1, 2)

        self.a_label_jornadas = QLabel(self.a_widget_data_congres)
        self.a_label_jornadas.setObjectName(u"a_label_jornadas")

        self.gridLayout_5.addWidget(self.a_label_jornadas, 1, 0, 1, 1)

        self.a_spinBox_jornadas = QSpinBox(self.a_widget_data_congres)
        self.a_spinBox_jornadas.setObjectName(u"a_spinBox_jornadas")
        self.a_spinBox_jornadas.setMinimumSize(QSize(70, 33))
        self.a_spinBox_jornadas.setMaximumSize(QSize(70, 30))

        self.gridLayout_5.addWidget(self.a_spinBox_jornadas, 1, 1, 1, 1)

        self.a_label_habita = QLabel(self.a_widget_data_congres)
        self.a_label_habita.setObjectName(u"a_label_habita")

        self.gridLayout_5.addWidget(self.a_label_habita, 1, 2, 1, 1)

        self.a_radioButton_habita = QRadioButton(self.a_widget_data_congres)
        self.a_radioButton_habita.setObjectName(u"a_radioButton_habita")

        self.gridLayout_5.addWidget(self.a_radioButton_habita, 1, 3, 1, 1)


        self.gridLayout_7.addWidget(self.a_widget_data_congres, 4, 0, 1, 1)

        self.a_widget_buttons = QWidget(self.a_frame)
        self.a_widget_buttons.setObjectName(u"a_widget_buttons")
        self.a_widget_buttons.setStyleSheet(u"QWidget {\n"
"    background-color: #F8F9FA; \n"
"    font-family: \"Segoe UI\", Arial, sans-serif; \n"
"    font-size: 14px; \n"
"    color: #333333; \n"
"}\n"
"QLabel {\n"
"    font-weight: bold; \n"
"    color: #2A9D8F; \n"
"    font-size: 12px; \n"
"}\n"
"QLineEdit {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"    selection-background-color: #2A9D8F; \n"
"    selection-color: #FFFFFF; \n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"    color: #333333; \n"
"}\n"
"QPushButton {\n"
"    background-color: #2A9D8F; \n"
"    color: #FFFFFF; \n"
"    border-radius: 8px; \n"
"    padding: 6px 12px; \n"
"    font-size: 14px; \n"
"    border: 2px solid #2A9D8F; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A4C639; "
                        "\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #207567; \n"
"    border: 2px solid #207567; \n"
"}\n"
"QComboBox {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #FFFFFF; \n"
"    selection-background-color: #2A9D8F; \n"
"    selection-color: #FFFFFF; \n"
"}\n"
"QSpinBox {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 2px solid "
                        "#2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}\n"
"QRadioButton {\n"
"    color: #333333; \n"
"    font-size: 12px; \n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 6px; \n"
"    width: 12px; \n"
"    height: 12px; \n"
"    background: #FFFFFF; \n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background: #2A9D8F; \n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    margin-top: 10px; \n"
"    font-weight: bold; \n"
"    font-size: 12px; \n"
"    color: #2A9D8F; \n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; \n"
"    subcontrol-position: top center; \n"
"    padding: 0 10px; \n"
"    background-color: #FFFFFF; \n"
"}\n"
"QDateEdit {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size:"
                        " 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 2px solid #2A9D8F; \n"
"    outline: none; \n"
"    background-color: #F0FDFC; \n"
"}")
        self.gridLayout_6 = QGridLayout(self.a_widget_buttons)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_13 = QSpacerItem(77, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_13, 0, 0, 1, 1)

        self.a_pushButton_volver = QPushButton(self.a_widget_buttons)
        self.a_pushButton_volver.setObjectName(u"a_pushButton_volver")
        self.a_pushButton_volver.setMinimumSize(QSize(90, 36))
        self.a_pushButton_volver.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #E76F51;\n"
"    color: #FFFFFF;  \n"
"    border-radius: 8px; \n"
"    padding: 6px 12px;\n"
"    font-size: 14px;  \n"
"    border: 2px solid #E76F51;  \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #F4A261;\n"
"    border: 2px solid #F4A261;  \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D75D32; \n"
"    border: 2px solid #D75D32; \n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.a_pushButton_volver, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(76, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.a_pushButton_reserva = QPushButton(self.a_widget_buttons)
        self.a_pushButton_reserva.setObjectName(u"a_pushButton_reserva")
        self.a_pushButton_reserva.setMinimumSize(QSize(90, 36))

        self.gridLayout_6.addWidget(self.a_pushButton_reserva, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(77, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)


        self.gridLayout_7.addWidget(self.a_widget_buttons, 5, 0, 1, 1)


        self.retranslateUi(window_reserva)

        QMetaObject.connectSlotsByName(window_reserva)
    # setupUi

    def retranslateUi(self, window_reserva):
        window_reserva.setWindowTitle(QCoreApplication.translate("window_reserva", u"Form", None))
        self.a_label_title.setText(QCoreApplication.translate("window_reserva", u"TextLabel", None))
        self.a_label_title_type.setText(QCoreApplication.translate("window_reserva", u"Tipo", None))
        self.a_label_type_reserva.setText(QCoreApplication.translate("window_reserva", u"Tipo reserva:", None))
        self.a_label_phone.setText(QCoreApplication.translate("window_reserva", u"T\u00e9lefono:", None))
        self.a_label_name.setText(QCoreApplication.translate("window_reserva", u"Nombre:", None))
        self.a_label_title_person.setText(QCoreApplication.translate("window_reserva", u"Datos Personales:", None))
        self.a_label_title_reserva.setText(QCoreApplication.translate("window_reserva", u"Datos reserva:", None))
        self.a_label_date.setText(QCoreApplication.translate("window_reserva", u"Fecha:", None))
        self.a_label_type_salon.setText(QCoreApplication.translate("window_reserva", u"Tipo sal\u00f3n", None))
        self.a_label_asistent.setText(QCoreApplication.translate("window_reserva", u"Asistentes", None))
        self.a_label_tipo_cocina.setText(QCoreApplication.translate("window_reserva", u"Tipo cocina:", None))
        self.a_label_title_congres.setText(QCoreApplication.translate("window_reserva", u"Congreso", None))
        self.a_label_jornadas.setText(QCoreApplication.translate("window_reserva", u"Jornadas:", None))
        self.a_label_habita.setText(QCoreApplication.translate("window_reserva", u"Habitaciones:", None))
        self.a_radioButton_habita.setText(QCoreApplication.translate("window_reserva", u"Aceptar", None))
        self.a_pushButton_volver.setText(QCoreApplication.translate("window_reserva", u"volver", None))
        self.a_pushButton_reserva.setText(QCoreApplication.translate("window_reserva", u"reservar", None))
    # retranslateUi

