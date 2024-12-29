# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_windows.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)

from .resources_rc import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName("Login")
        Login.resize(332, 440)
        Login.setMinimumSize(QSize(332, 440))
        Login.setMaximumSize(QSize(332, 440))
        Login.setStyleSheet(
            "QWidget {\n"
            "    background-color: qlineargradient(\n"
            "        spread:pad, \n"
            "        x1:0, y1:0, \n"
            "        x2:1, y2:1, \n"
            "        stop:0 #EAF4F4, /* Verde muy claro */\n"
            "        stop:1 #C7E6E5  /* Tonalidad verde suave */\n"
            "    );\n"
            "    font-family: 'Montserrat', sans-serif;\n"
            "    font-size: 12px;\n"
            "    color: #555555; /* Gris suave para el texto general */\n"
            "}"
        )
        self.widget = QWidget(Login)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(0, 0, 333, 439))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.a_widget_title = QWidget(self.widget)
        self.a_widget_title.setObjectName("a_widget_title")
        self.a_widget_title.setStyleSheet(
            "QWidget {\n"
            "    background-color: qlineargradient(\n"
            "        spread:pad, \n"
            "        x1:0, y1:0, \n"
            "        x2:1, y2:1, \n"
            "        stop:0 #EAF4F4, \n"
            "        stop:1 #C7E6E5 \n"
            "    );\n"
            "    font-family: 'Montserrat', sans-serif;\n"
            "    font-size: 12px;\n"
            "    color: #555555; \n"
            "}"
        )
        self.verticalLayout_2 = QVBoxLayout(self.a_widget_title)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.a_label_title = QLabel(self.a_widget_title)
        self.a_label_title.setObjectName("a_label_title")
        self.a_label_title.setStyleSheet(
            "QLabel{\n"
            "    font-size: 20px;\n"
            "    font-weight: bold;\n"
            "    color: #2A9D8F; /* Verde moderno */\n"
            "    letter-spacing: 2px; /* Espaciado entre letras */\n"
            "    qproperty-alignment: AlignCenter; /* Alineaci\u00f3n centrada */\n"
            "    margin-top: 10px;\n"
            "}\n"
            ""
        )

        self.verticalLayout_2.addWidget(self.a_label_title)

        self.gridLayout.addWidget(self.a_widget_title, 0, 0, 1, 1)

        self.a_widget_logo = QWidget(self.widget)
        self.a_widget_logo.setObjectName("a_widget_logo")
        self.a_widget_logo.setStyleSheet(
            "QWidget {\n"
            "    background-color: qlineargradient(\n"
            "        spread:pad, \n"
            "        x1:0, y1:0, \n"
            "        x2:1, y2:1, \n"
            "        stop:0 #EAF4F4, \n"
            "        stop:1 #C7E6E5 \n"
            "    );\n"
            "    font-family: 'Montserrat', sans-serif;\n"
            "    font-size: 12px;\n"
            "    color: #555555; \n"
            "}"
        )
        self.horizontalLayout = QHBoxLayout(self.a_widget_logo)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            96, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.a_label_logo = QLabel(self.a_widget_logo)
        self.a_label_logo.setObjectName("a_label_logo")
        self.a_label_logo.setPixmap(QPixmap(":/images/icons/brianda1.png"))

        self.horizontalLayout.addWidget(self.a_label_logo)

        self.horizontalSpacer_2 = QSpacerItem(
            96, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.gridLayout.addWidget(self.a_widget_logo, 1, 0, 1, 1)

        self.a_widget_button = QWidget(self.widget)
        self.a_widget_button.setObjectName("a_widget_button")
        self.a_widget_button.setStyleSheet(
            "QWidget {\n"
            "    background-color: qlineargradient(\n"
            "        spread:pad, \n"
            "        x1:0, y1:0, \n"
            "        x2:1, y2:1, \n"
            "        stop:0 #EAF4F4, \n"
            "        stop:1 #C7E6E5 \n"
            "    );\n"
            "    font-family: 'Montserrat', sans-serif;\n"
            "    font-size: 12px;\n"
            "    color: #555555; \n"
            "}"
        )
        self.verticalLayout = QVBoxLayout(self.a_widget_button)
        self.verticalLayout.setObjectName("verticalLayout")
        self.a_label_user = QLabel(self.a_widget_button)
        self.a_label_user.setObjectName("a_label_user")
        self.a_label_user.setStyleSheet(
            "QLabel {\n"
            "    font-size: 14px;\n"
            "    font-weight: bold;\n"
            "    color: #444444; /* Gris m\u00e1s oscuro para mejor contraste */\n"
            "    margin-bottom: 8px; /* Mayor espaciado inferior */\n"
            "    letter-spacing: 0.8px; /* Espaciado entre letras m\u00e1s sutil */\n"
            "    text-transform: uppercase; /* Texto en may\u00fasculas */\n"
            "}\n"
            "\n"
            "QLabel:hover {\n"
            "    color: #2A9D8F; /* Verde principal al pasar el cursor */\n"
            "}\n"
            ""
        )

        self.verticalLayout.addWidget(self.a_label_user)

        self.a_lineEdit_user = QLineEdit(self.a_widget_button)
        self.a_lineEdit_user.setObjectName("a_lineEdit_user")
        self.a_lineEdit_user.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #FFFFFF; \n"
            "    border: 2px solid #CCCCCC; \n"
            "    border-radius: 8px; \n"
            "    padding: 5px;\n"
            "    font-size: 12px;\n"
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
            "    border: 2px solid #2A9D8F;\n"
            "    outline: none;\n"
            "    background-color: #F0FDFC; \n"
            "    color: #333333; \n"
            "}\n"
            ""
        )

        self.verticalLayout.addWidget(self.a_lineEdit_user)

        self.a_label_pass = QLabel(self.a_widget_button)
        self.a_label_pass.setObjectName("a_label_pass")
        self.a_label_pass.setStyleSheet(
            "QLabel {\n"
            "    font-size: 14px;\n"
            "    font-weight: bold;\n"
            "    color: #444444; /* Gris m\u00e1s oscuro para mejor contraste */\n"
            "    margin-bottom: 8px; /* Mayor espaciado inferior */\n"
            "    letter-spacing: 0.8px; /* Espaciado entre letras m\u00e1s sutil */\n"
            "    text-transform: uppercase; /* Texto en may\u00fasculas */\n"
            "}\n"
            "\n"
            "QLabel:hover {\n"
            "    color: #2A9D8F; /* Verde principal al pasar el cursor */\n"
            "}\n"
            ""
        )

        self.verticalLayout.addWidget(self.a_label_pass)

        self.a_lineEdit_pass = QLineEdit(self.a_widget_button)
        self.a_lineEdit_pass.setObjectName("a_lineEdit_pass")
        self.a_lineEdit_pass.setEchoMode(QLineEdit.Password)  # type: ignore
        self.a_lineEdit_pass.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #FFFFFF; \n"
            "    border: 2px solid #CCCCCC; \n"
            "    border-radius: 8px; \n"
            "    padding: 5px;\n"
            "    font-size: 12px;\n"
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
            "    border: 2px solid #2A9D8F;\n"
            "    outline: none;\n"
            "    background-color: #F0FDFC; \n"
            "    color: #333333; \n"
            "}\n"
            ""
        )

        self.verticalLayout.addWidget(self.a_lineEdit_pass)

        self.horizontalSpacer_4 = QSpacerItem(
            310, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.verticalLayout.addItem(self.horizontalSpacer_4)

        self.a_button_login = QPushButton(self.a_widget_button)
        self.a_button_login.setObjectName("a_button_login")
        self.a_button_login.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #2A9D8F; /* Verde original */\n"
            "    color: white;\n"
            "    border-radius: 10px;\n"
            "    padding: 5px;\n"
            "    font-size: 14px;\n"
            "    font-weight: bold;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #A4C639; /* Verde-amarillo intermedio */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #E76F51; /* Naranja intenso para contraste */\n"
            "    color: #FFFFFF; /* Texto blanco */\n"
            "}\n"
            "\n"
            ""
        )
        self.a_button_login.setCheckable(True)

        self.verticalLayout.addWidget(self.a_button_login)

        self.horizontalSpacer_3 = QSpacerItem(
            310, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.gridLayout.addWidget(self.a_widget_button, 2, 0, 1, 1)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)

    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", "LOGIN", None))
        self.a_label_title.setText(
            QCoreApplication.translate("Login", "CENTRO DE RESERVAS", None)
        )
        self.a_label_logo.setText("")
        self.a_label_user.setText(QCoreApplication.translate("Login", "Usuario:", None))
        self.a_label_pass.setText(
            QCoreApplication.translate("Login", "CONTRASE\u00d1A", None)
        )
        self.a_button_login.setText(QCoreApplication.translate("Login", "LOGIN", None))

    # retranslateUi
