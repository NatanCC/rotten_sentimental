# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
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

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName(_fromUtf8("main"))
        main.resize(525, 378)
        self.tab1 = QtGui.QWidget()
        self.tab1.setEnabled(True)
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.button_analyze = QtGui.QPushButton(self.tab1)
        self.button_analyze.setGeometry(QtCore.QRect(100, 270, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button_analyze.setFont(font)
        self.button_analyze.setObjectName(_fromUtf8("button_analyze"))
        self.result_text = QtGui.QTextBrowser(self.tab1)
        self.result_text.setGeometry(QtCore.QRect(270, 270, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.result_text.setFont(font)
        self.result_text.setStyleSheet(_fromUtf8("style=\"text-align:center\""))
        self.result_text.setObjectName(_fromUtf8("result_text"))
        self.input_text = QtGui.QTextEdit(self.tab1)
        self.input_text.setGeometry(QtCore.QRect(10, 30, 491, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_text.setFont(font)
        self.input_text.setObjectName(_fromUtf8("input_text"))
        self.label = QtGui.QLabel(self.tab1)
        self.label.setGeometry(QtCore.QRect(230, 0, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        main.addTab(self.tab1, _fromUtf8(""))
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.button_open = QtGui.QPushButton(self.tab2)
        self.button_open.setGeometry(QtCore.QRect(80, 300, 161, 31))
        self.button_open.setObjectName(_fromUtf8("button_open"))
        self.button_file_analyze = QtGui.QPushButton(self.tab2)
        self.button_file_analyze.setGeometry(QtCore.QRect(330, 300, 161, 31))
        self.button_file_analyze.setObjectName(_fromUtf8("button_file_analyze"))
        self.file_text = QtGui.QTextBrowser(self.tab2)
        self.file_text.setGeometry(QtCore.QRect(20, 30, 281, 261))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.file_text.setFont(font)
        self.file_text.setObjectName(_fromUtf8("file_text"))
        self.results_text = QtGui.QTextBrowser(self.tab2)
        self.results_text.setGeometry(QtCore.QRect(330, 30, 161, 261))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.results_text.setFont(font)
        self.results_text.setObjectName(_fromUtf8("results_text"))
        self.label_2 = QtGui.QLabel(self.tab2)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab2)
        self.label_3.setGeometry(QtCore.QRect(380, 10, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        main.addTab(self.tab2, _fromUtf8(""))

        self.retranslateUi(main)
        main.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        main.setWindowTitle(_translate("main", "Review Analyzer", None))
        self.button_analyze.setText(_translate("main", "Analyze", None))
        self.label.setText(_translate("main", "Review", None))
        main.setTabText(main.indexOf(self.tab1), _translate("main", "Normal", None))
        self.button_open.setText(_translate("main", "Open File", None))
        self.button_file_analyze.setText(_translate("main", "Analyze", None))
        self.label_2.setText(_translate("main", "Reviews", None))
        self.label_3.setText(_translate("main", "Results", None))
        main.setTabText(main.indexOf(self.tab2), _translate("main", "File", None))

