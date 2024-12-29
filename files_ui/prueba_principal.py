# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prueba_principal.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTableView,
    QWidget)

class Ui_prueba_principal(object):
    def setupUi(self, prueba_principal):
        if not prueba_principal.objectName():
            prueba_principal.setObjectName(u"prueba_principal")
        prueba_principal.resize(826, 583)
        self.frame = QFrame(prueba_principal)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 831, 581))
        self.frame.setStyleSheet(u"QWidget {\n"
"    background-color: #F8F9FA; \n"
"    font-family: \"Segoe UI\", Arial, sans-serif; \n"
"    font-size: 14px; \n"
"    color: #333333;\n"
"}\n"
"\n"
"QListWidget {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    padding: 5px; \n"
"    font-size: 12px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #2A9D8F; \n"
"    color: #FFFFFF; \n"
"}\n"
"\n"
"QTableView {\n"
"    background-color: #FFFFFF; \n"
"    border: 2px solid #CCCCCC; \n"
"    border-radius: 8px; \n"
"    font-family: \"Segoe UI\", Arial, sans-serif; \n"
"    font-size: 14px; \n"
"    color: #333333; \n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #2A9D8F; \n"
"    color: #FFFFFF; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #2A9D8F; \n"
"    color: white; \n"
"    font-wei"
                        "ght: bold; \n"
"    padding: 5px; \n"
"    border: 1px solid #CCCCCC; \n"
"}\n"
"\n"
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
"    background-color: #A4C639; \n"
"    border: 2px solid #A4C639; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #207567; \n"
"    border: 2px solid #207567; \n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tableView = QTableView(self.frame)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(130, 20, 661, 381))
        self.tableView.setStyleSheet(u"")
        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 20, 101, 192))
        self.listWidget.setStyleSheet(u"")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 460, 171, 51))
        self.pushButton.setStyleSheet(u"")

        self.retranslateUi(prueba_principal)

        QMetaObject.connectSlotsByName(prueba_principal)
    # setupUi

    def retranslateUi(self, prueba_principal):
        prueba_principal.setWindowTitle(QCoreApplication.translate("prueba_principal", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("prueba_principal", u"Reservar", None))
    # retranslateUi

