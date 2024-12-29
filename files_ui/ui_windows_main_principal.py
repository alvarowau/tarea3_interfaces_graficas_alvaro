# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windows_main_principal.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QWidget)

class Ui_windows_main_principal(object):
    def setupUi(self, windows_main_principal):
        if not windows_main_principal.objectName():
            windows_main_principal.setObjectName(u"windows_main_principal")
        windows_main_principal.resize(826, 583)
        windows_main_principal.setMinimumSize(QSize(826, 583))
        windows_main_principal.setMaximumSize(QSize(826, 583))
        self.a_frame = QFrame(windows_main_principal)
        self.a_frame.setObjectName(u"a_frame")
        self.a_frame.setGeometry(QRect(0, 0, 831, 581))
        self.a_frame.setStyleSheet(u"QFrame {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, \n"
"        x1:0, y1:0, \n"
"        x2:1, y2:1, \n"
"        stop:0 #EAF4F4, \n"
"        stop:1 #C7E6E5\n"
"    );\n"
"    font-family: 'Montserrat', sans-serif;\n"
"    font-size: 12px;\n"
"    color: #555555;\n"
"    border-radius: 10px;  \n"
"    border: 1px solid #D1D1D1;  \n"
"}\n"
"\n"
"\n"
"")
        self.a_frame.setFrameShape(QFrame.StyledPanel)
        self.a_frame.setFrameShadow(QFrame.Raised)
        self.a_tableView_table = QTableView(self.a_frame)
        self.a_tableView_table.setObjectName(u"a_tableView_table")
        self.a_tableView_table.setGeometry(QRect(180, 100, 611, 381))
        self.a_tableView_table.setStyleSheet(u"QTableView {\n"
"    background-color: #FFFFFF;  /* Fondo blanco para la tabla */\n"
"    border: 1px solid #D1D1D1;  /* Borde sutil gris */\n"
"    border-radius: 10px;        /* Bordes redondeados */\n"
"    font-family: 'Montserrat', sans-serif;\n"
"    font-size: 12px;\n"
"    color: #555555;             /* Color del texto en las celdas */\n"
"    padding: 10px;              /* Espaciado interno */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #2A9D8F;\n"
"    color: white;                \n"
"    padding: 8px;              \n"
"    border: none;              \n"
"    font-weight: bold;      \n"
"    font-size: 13px;            \n"
"    text-align: center;          \n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 8px;                \n"
"    border-bottom: 1px solid #D1D1D1; \n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #2A9D8F; \n"
"    color: white;               \n"
"}\n"
"\n"
"QTableView::item:hover {\n"
"    background-color: #A4C639;  \n"
"    color: white"
                        ";           \n"
"}\n"
"\n"
"QTableView::item:focus {\n"
"    outline: none;            \n"
"}\n"
"\n"
"QTableView QScrollBar:vertical {\n"
"    background: #F0F0F0;        \n"
"    width: 10px;             \n"
"}\n"
"\n"
"QTableView QScrollBar:horizontal {\n"
"    background: #F0F0F0;       \n"
"    height: 10px;                \n"
"}\n"
"\n"
"QTableView QScrollBar::handle:vertical {\n"
"    background: #A4C639;      \n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTableView QScrollBar::handle:horizontal {\n"
"    background: #A4C639;   \n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.a_listWidget_list = QListWidget(self.a_frame)
        self.a_listWidget_list.setObjectName(u"a_listWidget_list")
        self.a_listWidget_list.setGeometry(QRect(20, 160, 141, 231))
        self.a_listWidget_list.setStyleSheet(u"QListWidget {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #D1D1D1;  \n"
"    border-radius: 10px;       \n"
"    font-family: 'Montserrat', sans-serif;\n"
"    font-size: 12px;\n"
"    color: #555555;            \n"
"    padding: 5px;               \n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: transparent;  \n"
"    padding: 8px;                  \n"
"    border-radius: 5px;             \n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #2A9D8F; \n"
"    color: white;                \n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #A4C639;  \n"
"    color: white;               \n"
"}\n"
"\n"
"QListWidget::item:focus {\n"
"    outline: none; \n"
"}\n"
"")
        self.widget = QWidget(self.a_frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 500, 691, 58))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(117, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.a_pushButton_exit = QPushButton(self.widget)
        self.a_pushButton_exit.setObjectName(u"a_pushButton_exit")
        self.a_pushButton_exit.setMinimumSize(QSize(130, 40))
        self.a_pushButton_exit.setStyleSheet(u"QPushButton {\n"
"    background-color: #E63946;  /* Rojo intenso */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #F1A1A6; /* Rojo m\u00e1s claro */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D94E3D;  /* Rojo oscuro */\n"
"    color: #FFFFFF; \n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.a_pushButton_exit)

        self.a_pushButton_modi_reserva = QPushButton(self.widget)
        self.a_pushButton_modi_reserva.setObjectName(u"a_pushButton_modi_reserva")
        self.a_pushButton_modi_reserva.setMinimumSize(QSize(130, 40))
        self.a_pushButton_modi_reserva.setStyleSheet(u"QPushButton {\n"
"    background-color: #F4A261;  /* Color suave y c\u00e1lido (naranja) */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #F9C74F;  /* Naranja m\u00e1s claro */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E76F51;  /* Rojo m\u00e1s oscuro para el estado presionado */\n"
"    color: #FFFFFF; \n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.a_pushButton_modi_reserva)

        self.a_pushButton_new_reserva = QPushButton(self.widget)
        self.a_pushButton_new_reserva.setObjectName(u"a_pushButton_new_reserva")
        self.a_pushButton_new_reserva.setMinimumSize(QSize(130, 40))
        self.a_pushButton_new_reserva.setStyleSheet(u"QPushButton {\n"
"    background-color: #2A9D8F; \n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A4C639; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E76F51; \n"
"    color: #FFFFFF; \n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.a_pushButton_new_reserva)

        self.horizontalSpacer_2 = QSpacerItem(117, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.widget_2 = QWidget(self.a_frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(40, 10, 731, 52))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(215, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.a_label_title = QLabel(self.widget_2)
        self.a_label_title.setObjectName(u"a_label_title")
        self.a_label_title.setStyleSheet(u"QLabel{\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    color: #2A9D8F; \n"
"    letter-spacing: 2px; \n"
"    qproperty-alignment: AlignCenter; \n"
"    margin-top: 10px;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.a_label_title)

        self.horizontalSpacer_3 = QSpacerItem(214, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.retranslateUi(windows_main_principal)

        QMetaObject.connectSlotsByName(windows_main_principal)
    # setupUi

    def retranslateUi(self, windows_main_principal):
        windows_main_principal.setWindowTitle(QCoreApplication.translate("windows_main_principal", u"Form", None))
        self.a_pushButton_exit.setText(QCoreApplication.translate("windows_main_principal", u"SALIR", None))
        self.a_pushButton_modi_reserva.setText(QCoreApplication.translate("windows_main_principal", u"MODIFICAR RESERVA", None))
        self.a_pushButton_new_reserva.setText(QCoreApplication.translate("windows_main_principal", u"NUEVA RESERVA", None))
        self.a_label_title.setText(QCoreApplication.translate("windows_main_principal", u"CENTRO DE RESERVAS", None))
    # retranslateUi

