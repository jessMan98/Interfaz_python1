# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(669, 503)
        MainWindow.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(1, 165, 113);\n"
"\n"
"\n"
"")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Pintar = QTabWidget(self.centralwidget)
        self.Pintar.setObjectName(u"Pintar")
        self.Pintar.setGeometry(QRect(20, 10, 631, 451))
        self.Pintar.setStyleSheet(u"\n"
"background-color: rgb(201, 232, 222);\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.muestra = QPushButton(self.tab)
        self.muestra.setObjectName(u"muestra")
        self.muestra.setGeometry(QRect(50, 380, 201, 23))
        self.muestra.setStyleSheet(u"background-color: rgb(2, 107, 77);\n"
"color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 290, 16, 16))
        self.green = QSpinBox(self.tab)
        self.green.setObjectName(u"green")
        self.green.setGeometry(QRect(110, 290, 141, 20))
        self.green.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.green.setMaximum(255)
        self.inserta = QPushButton(self.tab)
        self.inserta.setObjectName(u"inserta")
        self.inserta.setGeometry(QRect(50, 350, 201, 23))
        self.inserta.setStyleSheet(u"background-color: rgb(2, 107, 77);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.blue = QSpinBox(self.tab)
        self.blue.setObjectName(u"blue")
        self.blue.setGeometry(QRect(110, 320, 141, 20))
        self.blue.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.blue.setMaximum(255)
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 220, 31, 20))
        self.label_8.setStyleSheet(u"font: 11pt \"MS Reference Sans Serif\";\n"
"color:rgb(208, 6, 9);")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 260, 16, 16))
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 50, 201, 164))
        self.formLayout_2 = QFormLayout(self.layoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.id = QLineEdit(self.layoutWidget)
        self.id.setObjectName(u"id")
        self.id.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.id)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label)

        self.origen_X1 = QLineEdit(self.layoutWidget)
        self.origen_X1.setObjectName(u"origen_X1")
        self.origen_X1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.origen_X1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.origen_Y1 = QLineEdit(self.layoutWidget)
        self.origen_Y1.setObjectName(u"origen_Y1")
        self.origen_Y1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.origen_Y1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.destino_X2 = QLineEdit(self.layoutWidget)
        self.destino_X2.setObjectName(u"destino_X2")
        self.destino_X2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.destino_X2)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.destino_Y2 = QLineEdit(self.layoutWidget)
        self.destino_Y2.setObjectName(u"destino_Y2")
        self.destino_Y2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.destino_Y2)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_10)

        self.velocidad = QLineEdit(self.layoutWidget)
        self.velocidad.setObjectName(u"velocidad")
        self.velocidad.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.velocidad)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.red = QSpinBox(self.tab)
        self.red.setObjectName(u"red")
        self.red.setGeometry(QRect(110, 260, 141, 20))
        self.red.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.red.setMaximum(255)
        self.red.setValue(0)
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 320, 16, 16))
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(73, 9, 107, 25))
        self.label_9.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(2, 107, 77);")
        self.label_9.setIndent(2)
        self.salidaDatos = QPlainTextEdit(self.tab)
        self.salidaDatos.setObjectName(u"salidaDatos")
        self.salidaDatos.setGeometry(QRect(290, 30, 311, 381))
        self.salidaDatos.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(85, 0, 127);")
        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(70, 220, 21, 21))
        self.label_12.setStyleSheet(u"font: 11pt \"MS Reference Sans Serif\";\n"
"color: rgb(23, 127, 35);")
        self.label_12.setMargin(0)
        self.label_12.setIndent(2)
        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(90, 220, 16, 21))
        self.label_13.setStyleSheet(u"font: 11pt \"MS Reference Sans Serif\";\n"
"color: rgb(16, 140, 255);")
        self.label_13.setMargin(0)
        self.label_13.setIndent(5)
        self.Pintar.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.busca_linea = QLineEdit(self.tab_2)
        self.busca_linea.setObjectName(u"busca_linea")
        self.busca_linea.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.busca_linea)

        self.busca = QPushButton(self.tab_2)
        self.busca.setObjectName(u"busca")
        self.busca.setStyleSheet(u"background-color: rgb(2, 107, 77);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.busca)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tabla.setFont(font)
        self.tabla.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tabla.setAutoScrollMargin(19)
        self.tabla.setTextElideMode(Qt.ElideMiddle)
        self.tabla.setShowGrid(True)
        self.tabla.setGridStyle(Qt.CustomDashLine)
        self.tabla.horizontalHeader().setCascadingSectionResizes(False)

        self.gridLayout.addWidget(self.tabla, 1, 0, 1, 1)

        self.mostrar = QPushButton(self.tab_2)
        self.mostrar.setObjectName(u"mostrar")
        self.mostrar.setStyleSheet(u"background-color: rgb(2, 107, 77);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.mostrar, 2, 0, 1, 1)

        self.Pintar.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibuja = QPushButton(self.tab_3)
        self.dibuja.setObjectName(u"dibuja")
        self.dibuja.setStyleSheet(u"background-color: rgb(2, 107, 77);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.dibuja, 1, 0, 1, 1)

        self.limpia = QPushButton(self.tab_3)
        self.limpia.setObjectName(u"limpia")
        self.limpia.setStyleSheet(u"background-color: rgb(2, 107, 77);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.limpia, 1, 1, 1, 1)

        self.Pintar.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 669, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.Pintar.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.muestra.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.inserta.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"C o", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"r", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Origen X", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Part\u00edculas</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"l o", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"r", None))
        self.Pintar.setTabText(self.Pintar.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.busca.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.Pintar.setTabText(self.Pintar.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibuja.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpia.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.Pintar.setTabText(self.Pintar.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Pintar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

