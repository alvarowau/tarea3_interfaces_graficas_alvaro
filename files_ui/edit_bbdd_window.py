# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_bbdd_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QWidget,
)


class Ui_edit_bbdd_windows(object):
    def setupUi(self, edit_bbdd_windows):
        if not edit_bbdd_windows.objectName():
            edit_bbdd_windows.setObjectName(u"edit_bbdd_windows")
        edit_bbdd_windows.resize(381, 412)
        edit_bbdd_windows.setMinimumSize(QSize(381, 412))
        edit_bbdd_windows.setMaximumSize(QSize(381, 412))
        edit_bbdd_windows.setStyleSheet(u"QWidget {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0, \n"
"        x2:1, y2:1, \n"
"        stop:0 #EAF4F4, \n"
"        stop:1 #C7E6E5 \n"
"    );\n"
"    font-family: 'Montserrat', sans-serif;\n"
"    font-size: 12px;\n"
"    color: #555555;\n"
"}\n"
"")
        self.widget_3 = QWidget(edit_bbdd_windows)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 381, 411))
        self.gridLayout_5 = QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 0, 4, 1, 1)

        self.a_button_mysql = QPushButton(self.widget_2)
        self.a_button_mysql.setObjectName(u"a_button_mysql")
        self.a_button_mysql.setStyleSheet(u"QPushButton {\n"
"    background-color: #616161; /* Gris oscuro para MySQL */\n"
"    color: white; /* Color de texto blanco */\n"
"    border-radius: 10px;\n"
"    padding: 10px 20px; /* Aumentar el padding para mejor apariencia */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    width: 200px; /* Establecer un ancho fijo para los botones */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #424242; /* Gris a\u00fan m\u00e1s oscuro para hover */\n"
"    color: #FFFFFF; /* Mantener texto blanco en hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #212121; /* Gris m\u00e1s oscuro al presionar */\n"
"    color: #FFFFFF; /* Texto blanco al presionar */\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.a_button_mysql, 0, 1, 1, 1)

        self.a_button_sqlite = QPushButton(self.widget_2)
        self.a_button_sqlite.setObjectName(u"a_button_sqlite")
        self.a_button_sqlite.setStyleSheet(u"QPushButton {\n"
"    background-color: #FF5722; /* Naranja para SQLite */\n"
"    color: white; /* Color de texto blanco */\n"
"    border-radius: 10px;\n"
"    padding: 10px 20px; /* Aumentar el padding para mejor apariencia */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    width: 200px; /* Establecer un ancho fijo para los botones */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E64A19; /* Naranja m\u00e1s oscuro para hover */\n"
"    color: #FFFFFF; /* Mantener texto blanco en hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E76F51; /* Naranja intenso para contraste */\n"
"    color: #FFFFFF; /* Texto blanco al presionar */\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.a_button_sqlite, 0, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_2, 0, 0, 1, 3)

        self.horizontalSpacer_6 = QSpacerItem(114, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_6, 2, 0, 1, 1)

        self.a_button_save = QPushButton(self.widget_3)
        self.a_button_save.setObjectName(u"a_button_save")
        self.a_button_save.setStyleSheet(u"QPushButton {\n"
"    background-color: #007BFF; /* Azul brillante para Aceptar */\n"
"    color: white; /* Color de texto blanco */\n"
"    border-radius: 12px; /* Bordes redondeados para un estilo suave */\n"
"    padding: 12px 24px; /* Aumentar el padding para mejor apariencia */\n"
"    font-size: 14px; /* Fuente m\u00e1s grande para destacar */\n"
"    font-weight: bold; /* Resaltar el texto */\n"
"    width: 220px; /* Establecer un ancho fijo para el bot\u00f3n */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; /* Azul m\u00e1s oscuro para hover */\n"
"    color: #FFFFFF; /* Mantener texto blanco en hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #004085; /* Azul a\u00fan m\u00e1s oscuro al presionar */\n"
"    color: #FFFFFF; /* Texto blanco al presionar */\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.a_button_save, 2, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(114, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 2, 2, 1, 1)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_4 = QGridLayout(self.page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0, \n"
"        x2:1, y2:1, \n"
"        stop:0 #EAF4F4, \n"
"        stop:1 #C7E6E5 \n"
"    );\n"
"    font-family: 'Montserrat', sans-serif;\n"
"    font-size: 12px;\n"
"    color: #555555;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #4CAF50; /* Verde m\u00e1s vivo para diferenciarlo */\n"
"    color: white; /* Color de texto blanco */\n"
"    border-radius: 10px;\n"
"    padding: 10px 20px; /* Aumentar el padding para mejor apariencia */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A4C639; /* Verde-amarillo intermedio */\n"
"    color: #333333; /* Gris oscuro para el texto al pasar el cursor */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E76F51; /* Naranja intenso para contraste */\n"
"    color: #FFFFFF; /* Texto blanco al presionar */\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.a_form_mysql = QWidget(self.widget)
        self.a_form_mysql.setObjectName(u"a_form_mysql")
        self.a_form_mysql.setStyleSheet(u"QWidget {\n"
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
"}\n"
"\n"
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
"\n"
"QLabel {\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    color: #444444; /* Gris m\u00e1s oscuro para mejor contraste */\n"
"    margin-bottom: 8px; /* Mayor espaciado inferior */\n"
"    letter-spacing:"
                        " 0.8px; /* Espaciado entre letras m\u00e1s sutil */\n"
"    text-transform: uppercase; /* Texto en may\u00fasculas */\n"
"	text-align: center; /* Centrar el texto */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #2A9D8F; /* Verde principal al pasar el cursor */\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.a_form_mysql)
        self.gridLayout.setObjectName(u"gridLayout")
        self.a_label_host = QLabel(self.a_form_mysql)
        self.a_label_host.setObjectName(u"a_label_host")

        self.gridLayout.addWidget(self.a_label_host, 0, 0, 1, 1)

        self.a_lineEdit_host = QLineEdit(self.a_form_mysql)
        self.a_lineEdit_host.setObjectName(u"a_lineEdit_host")

        self.gridLayout.addWidget(self.a_lineEdit_host, 0, 1, 1, 1)

        self.a_label_port = QLabel(self.a_form_mysql)
        self.a_label_port.setObjectName(u"a_label_port")

        self.gridLayout.addWidget(self.a_label_port, 1, 0, 1, 1)

        self.a_lineEdit_port = QLineEdit(self.a_form_mysql)
        self.a_lineEdit_port.setObjectName(u"a_lineEdit_port")

        self.gridLayout.addWidget(self.a_lineEdit_port, 1, 1, 1, 1)

        self.a_label_user = QLabel(self.a_form_mysql)
        self.a_label_user.setObjectName(u"a_label_user")

        self.gridLayout.addWidget(self.a_label_user, 2, 0, 1, 1)

        self.a_lineEdit_user = QLineEdit(self.a_form_mysql)
        self.a_lineEdit_user.setObjectName(u"a_lineEdit_user")

        self.gridLayout.addWidget(self.a_lineEdit_user, 2, 1, 1, 1)

        self.a_label_pass = QLabel(self.a_form_mysql)
        self.a_label_pass.setObjectName(u"a_label_pass")

        self.gridLayout.addWidget(self.a_label_pass, 3, 0, 1, 1)

        self.a_lineEdit_password = QLineEdit(self.a_form_mysql)
        self.a_lineEdit_password.setObjectName(u"a_lineEdit_password")

        self.gridLayout.addWidget(self.a_lineEdit_password, 3, 1, 1, 1)

        self.a_label_bbdd = QLabel(self.a_form_mysql)
        self.a_label_bbdd.setObjectName(u"a_label_bbdd")

        self.gridLayout.addWidget(self.a_label_bbdd, 4, 0, 1, 1)

        self.a_lineEdit_bbdd = QLineEdit(self.a_form_mysql)
        self.a_lineEdit_bbdd.setObjectName(u"a_lineEdit_bbdd")

        self.gridLayout.addWidget(self.a_lineEdit_bbdd, 4, 1, 1, 1)


        self.gridLayout_2.addWidget(self.a_form_mysql, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(105, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.a_button_test = QPushButton(self.widget)
        self.a_button_test.setObjectName(u"a_button_test")
        self.a_button_test.setMinimumSize(QSize(100, 30))
        self.a_button_test.setMaximumSize(QSize(100, 30))

        self.gridLayout_2.addWidget(self.a_button_test, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(104, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_7 = QGridLayout(self.page_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget_4 = QWidget(self.page_2)
        self.widget_4.setObjectName(u"widget_4")
        self.a_form_sqlite = QWidget(self.widget_4)
        self.a_form_sqlite.setObjectName(u"a_form_sqlite")
        self.a_form_sqlite.setGeometry(QRect(20, 10, 321, 101))
        self.a_form_sqlite.setStyleSheet(u"\n"
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
"")
        self.gridLayout_6 = QGridLayout(self.a_form_sqlite)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_11 = QSpacerItem(12, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)

        self.a_lineEdit_search_file = QLineEdit(self.a_form_sqlite)
        self.a_lineEdit_search_file.setObjectName(u"a_lineEdit_search_file")

        self.gridLayout_6.addWidget(self.a_lineEdit_search_file, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_10, 0, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(12, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_8, 1, 0, 1, 1)

        self.a_pushButton_select_file = QPushButton(self.a_form_sqlite)
        self.a_pushButton_select_file.setObjectName(u"a_pushButton_select_file")
        self.a_pushButton_select_file.setStyleSheet(u"QPushButton {\n"
"    background-color: #B0BEC5; /* Gris claro para el bot\u00f3n */\n"
"    color: white; /* Texto blanco */\n"
"    border-radius: 12px; /* Bordes redondeados */\n"
"    padding: 12px 24px; /* Aumentar el padding para mejor apariencia */\n"
"    font-size: 14px; /* Fuente m\u00e1s grande */\n"
"    font-weight: bold; /* Texto en negrita */\n"
"    width: 220px; /* Ancho fijo */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #90A4AE; /* Gris m\u00e1s oscuro al pasar el cursor */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #607D8B; /* Gris a\u00fan m\u00e1s oscuro cuando se presiona */\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.a_pushButton_select_file, 1, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_9, 1, 2, 1, 1)

        self.a_button_test_sqlite = QPushButton(self.widget_4)
        self.a_button_test_sqlite.setObjectName(u"a_button_test_sqlite")
        self.a_button_test_sqlite.setGeometry(QRect(120, 120, 100, 30))
        self.a_button_test_sqlite.setMinimumSize(QSize(100, 30))
        self.a_button_test_sqlite.setMaximumSize(QSize(100, 30))
        self.a_button_test_sqlite.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #4CAF50; /* Verde m\u00e1s vivo para diferenciarlo */\n"
"    color: white; /* Color de texto blanco */\n"
"    border-radius: 10px;\n"
"    padding: 10px 20px; /* Aumentar el padding para mejor apariencia */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A4C639; /* Verde-amarillo intermedio */\n"
"    color: #333333; /* Gris oscuro para el texto al pasar el cursor */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E76F51; /* Naranja intenso para contraste */\n"
"    color: #FFFFFF; /* Texto blanco al presionar */\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.widget_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_5.addWidget(self.stackedWidget, 1, 0, 1, 3)


        self.retranslateUi(edit_bbdd_windows)

        QMetaObject.connectSlotsByName(edit_bbdd_windows)
    # setupUi

    def retranslateUi(self, edit_bbdd_windows):
        edit_bbdd_windows.setWindowTitle(QCoreApplication.translate("edit_bbdd_windows", u"Edit bbdd", None))
        self.a_button_mysql.setText(QCoreApplication.translate("edit_bbdd_windows", u"mysql", None))
        self.a_button_sqlite.setText(QCoreApplication.translate("edit_bbdd_windows", u"sqLite", None))
        self.a_button_save.setText(QCoreApplication.translate("edit_bbdd_windows", u"GUARDAR", None))
        self.a_label_host.setText(QCoreApplication.translate("edit_bbdd_windows", u"host:", None))
        self.a_label_port.setText(QCoreApplication.translate("edit_bbdd_windows", u"port:", None))
        self.a_label_user.setText(QCoreApplication.translate("edit_bbdd_windows", u"usuario:", None))
        self.a_label_pass.setText(QCoreApplication.translate("edit_bbdd_windows", u"contrase\u00f1a:", None))
        self.a_label_bbdd.setText(QCoreApplication.translate("edit_bbdd_windows", u"base datos:", None))
        self.a_button_test.setText(QCoreApplication.translate("edit_bbdd_windows", u"test", None))
        self.a_pushButton_select_file.setText(QCoreApplication.translate("edit_bbdd_windows", u"Seleccionar archivo", None))
        self.a_button_test_sqlite.setText(QCoreApplication.translate("edit_bbdd_windows", u"test", None))
    # retranslateUi

