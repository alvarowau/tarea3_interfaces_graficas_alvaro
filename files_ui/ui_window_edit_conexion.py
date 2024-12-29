# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_edit_conexion.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_windows_conec(object):
    def setupUi(self, windows_conec):
        if not windows_conec.objectName():
            windows_conec.setObjectName(u"windows_conec")
        windows_conec.resize(570, 293)
        windows_conec.setMinimumSize(QSize(570, 293))
        windows_conec.setMaximumSize(QSize(570, 293))
        windows_conec.setStyleSheet(u"")
        self.a_widget_principal = QWidget(windows_conec)
        self.a_widget_principal.setObjectName(u"a_widget_principal")
        self.a_widget_principal.setGeometry(QRect(0, 0, 571, 295))
        self.a_widget_principal.setStyleSheet(u"QWidget {\n"
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
"}")
        self.gridLayout_4 = QGridLayout(self.a_widget_principal)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(120, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 0, 2, 1, 1)

        self.a_label_title_windows = QLabel(self.a_widget_principal)
        self.a_label_title_windows.setObjectName(u"a_label_title_windows")
        self.a_label_title_windows.setStyleSheet(u"QLabel{\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    color: #2A9D8F; \n"
"    letter-spacing: 2px;\n"
"    qproperty-alignment: AlignCenter; \n"
"    margin-top: 10px;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.a_label_title_windows, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(120, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.widget = QWidget(self.a_widget_principal)
        self.widget.setObjectName(u"widget")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(148, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.a_button_app = QPushButton(self.widget)
        self.a_button_app.setObjectName(u"a_button_app")
        self.a_button_app.setMinimumSize(QSize(220, 35))
        self.a_button_app.setStyleSheet(u"QPushButton {\n"
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
"")

        self.gridLayout_3.addWidget(self.a_button_app, 1, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(149, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)

        self.a_widget_grupo_conec = QWidget(self.widget)
        self.a_widget_grupo_conec.setObjectName(u"a_widget_grupo_conec")
        self.a_widget_grupo_conec.setStyleSheet(u"QWidget {\n"
"    border: 2px solid #3399FF;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    background-color: #FFFFFF;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.a_widget_grupo_conec)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_title_grupo = QLabel(self.a_widget_grupo_conec)
        self.label_title_grupo.setObjectName(u"label_title_grupo")
        self.label_title_grupo.setMinimumSize(QSize(245, 55))
        self.label_title_grupo.setStyleSheet(u"QLabel#label_title_grupo {\n"
"    color: #007BFF;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.label_title_grupo, 0, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(166, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 2)

        self.widget_2 = QWidget(self.a_widget_grupo_conec)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(320, 65))
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.a_radioButton_mysql = QRadioButton(self.widget_2)
        self.a_radioButton_mysql.setObjectName(u"a_radioButton_mysql")
        self.a_radioButton_mysql.setStyleSheet(u"QRadioButton {\n"
"    font-size: 14px;\n"
"    color: #007BFF;\n"
"}")

        self.gridLayout.addWidget(self.a_radioButton_mysql, 0, 0, 1, 1)

        self.a_label_color_mysql = QLabel(self.widget_2)
        self.a_label_color_mysql.setObjectName(u"a_label_color_mysql")

        self.gridLayout.addWidget(self.a_label_color_mysql, 0, 1, 1, 1)

        self.a_radioButton_sqlite = QRadioButton(self.widget_2)
        self.a_radioButton_sqlite.setObjectName(u"a_radioButton_sqlite")
        self.a_radioButton_sqlite.setStyleSheet(u"QRadioButton {\n"
"    font-size: 14px;\n"
"    color: #007BFF;\n"
"}")

        self.gridLayout.addWidget(self.a_radioButton_sqlite, 0, 2, 1, 1)

        self.a_label_color_sqlite = QLabel(self.widget_2)
        self.a_label_color_sqlite.setObjectName(u"a_label_color_sqlite")

        self.gridLayout.addWidget(self.a_label_color_sqlite, 0, 3, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(236, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.a_button_conec = QPushButton(self.a_widget_grupo_conec)
        self.a_button_conec.setObjectName(u"a_button_conec")
        self.a_button_conec.setMinimumSize(QSize(200, 35))
        self.a_button_conec.setStyleSheet(u"QPushButton {\n"
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
"")

        self.gridLayout_2.addWidget(self.a_button_conec, 2, 1, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(63, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 3, 1, 1)


        self.gridLayout_3.addWidget(self.a_widget_grupo_conec, 0, 0, 1, 3)


        self.gridLayout_4.addWidget(self.widget, 1, 0, 1, 3)


        self.retranslateUi(windows_conec)

        QMetaObject.connectSlotsByName(windows_conec)
    # setupUi

    def retranslateUi(self, windows_conec):
        windows_conec.setWindowTitle(QCoreApplication.translate("windows_conec", u"Form", None))
        self.a_label_title_windows.setText(QCoreApplication.translate("windows_conec", u"conexiones base de datos", None))
        self.a_button_app.setText(QCoreApplication.translate("windows_conec", u"Conectar", None))
        self.label_title_grupo.setText(QCoreApplication.translate("windows_conec", u"Selecciona la Base de Datos", None))
        self.a_radioButton_mysql.setText(QCoreApplication.translate("windows_conec", u"Mysql", None))
        self.a_label_color_mysql.setText("")
        self.a_radioButton_sqlite.setText(QCoreApplication.translate("windows_conec", u"SqLite", None))
        self.a_label_color_sqlite.setText("")
        self.a_button_conec.setText(QCoreApplication.translate("windows_conec", u"Modificar Conexi\u00f3n", None))
    # retranslateUi

