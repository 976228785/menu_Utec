# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panes3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_panes3Window(object):
    def setupUi(self, panes3Window):
        panes3Window.setObjectName(_fromUtf8("panes3Window"))
        panes3Window.resize(802, 600)
        self.centralwidget = QtGui.QWidget(panes3Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 440, 171, 61))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 400, 68, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 30, 311, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("UTEC.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 20, 81, 101))
        self.pushButton_2.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("flecha-hacia-la-izquierda-antes-de-icono-4330-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 150, 611, 191))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 440, 171, 61))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        panes3Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(panes3Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENUTEC = QtGui.QMenu(self.menubar)
        self.menuMENUTEC.setObjectName(_fromUtf8("menuMENUTEC"))
        panes3Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(panes3Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        panes3Window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMENUTEC.menuAction())

        self.retranslateUi(panes3Window)
        QtCore.QMetaObject.connectSlotsByName(panes3Window)

    def retranslateUi(self, panes3Window):
        panes3Window.setWindowTitle(_translate("panes3Window", "MainWindow", None))
        self.pushButton_3.setText(_translate("panes3Window", "IMPRIMIR ", None))
        self.label.setText(_translate("panes3Window", "TOTAL : ", None))
        self.pushButton.setText(_translate("panes3Window", "SANDWICHES, JUGOS Y BEBIDAS", None))
        self.textEdit.setHtml(_translate("panes3Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; text-decoration: underline; color:#281f84;\">PAN C/ POLLO </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic; text-decoration: underline;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(DESCRIPCIÓN DEL MENÚ)</p></body></html>", None))
        self.pushButton_4.setText(_translate("panes3Window", "OTRO PEDIDO ", None))
        self.menuMENUTEC.setTitle(_translate("panes3Window", "MENUTEC", None))

