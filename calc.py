# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(374, 348)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 10, 321, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(22)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pbAdd = QtGui.QPushButton(self.centralwidget)
        self.pbAdd.setGeometry(QtCore.QRect(30, 80, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.pbAdd.setFont(font)
        self.pbAdd.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pbAdd.setObjectName(_fromUtf8("pbAdd"))
        self.pbMin = QtGui.QPushButton(self.centralwidget)
        self.pbMin.setGeometry(QtCore.QRect(30, 190, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.pbMin.setFont(font)
        self.pbMin.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pbMin.setObjectName(_fromUtf8("pbMin"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 80, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pbDiv = QtGui.QPushButton(self.centralwidget)
        self.pbDiv.setGeometry(QtCore.QRect(140, 190, 101, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(40)
        self.pbDiv.setFont(font)
        self.pbDiv.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pbDiv.setObjectName(_fromUtf8("pbDiv"))
        self.pbC = QtGui.QPushButton(self.centralwidget)
        self.pbC.setGeometry(QtCore.QRect(250, 80, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.pbC.setFont(font)
        self.pbC.setObjectName(_fromUtf8("pbC"))
        self.pbC.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pbMul = QtGui.QPushButton(self.centralwidget)
        self.pbMul.setGeometry(QtCore.QRect(140, 80, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.pbMul.setFont(font)
        self.pbMul.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pbMul.setObjectName(_fromUtf8("pbMul"))
        self.pbEqu = QtGui.QPushButton(self.centralwidget)
        self.pbEqu.setGeometry(QtCore.QRect(250, 190, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.pbEqu.setFont(font)
        self.pbEqu.setObjectName(_fromUtf8("pbEqu"))
        self.pbEqu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 161, 31))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 374, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        self.lst = []
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtCore.QObject.connect(self.pbAdd, QtCore.SIGNAL("clicked()"), self.adder)
        QtCore.QObject.connect(self.pbC, QtCore.SIGNAL("clicked()"), self.C)
        QtCore.QObject.connect(self.pbEqu, QtCore.SIGNAL("clicked()"), self.Equ)
        QtCore.QObject.connect(self.pbMul, QtCore.SIGNAL("clicked()"), self.Mul)        
    def adder(self):
        self.lst.append(self.lineEdit.text())
        if self.lineEdit.text()=="":
            del self.lst[-2]
        self.lst.append('+')
        dispStr = ''.join(self.lst)
        self.label.setText(dispStr)
        self.lineEdit.setText('')
    def C(self):
        self.lineEdit.setText('')
        self.lst.clear()
        self.label.setText("")
    def Equ(self):
        self.lst.append(self.lineEdit.text())
        if self.lineEdit.text()=="":
            del self.lst[-2]
        dispStr = ''.join(self.lst)
        ans = eval(dispStr)
        self.lineEdit.setText(str(ans))
        self.lst.clear()
        self.label.setText("")
    def Mul(self):
        self.lst.append(self.lineEdit.text())
        if self.lineEdit.text()=="":
            del self.lst[-2]
        self.lst.append('*')
        dispStr = ''.join(self.lst)
        self.label.setText(dispStr)
        self.lineEdit.setText('')        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lineEdit.setText(_translate("MainWindow", "", None))
        self.pbAdd.setText(_translate("MainWindow", "+", None))
        self.pbMin.setText(_translate("MainWindow", "-", None))
        self.pushButton_3.setText(_translate("MainWindow", "×", None))
        self.pbDiv.setText(_translate("MainWindow", "÷", None))
        self.pbC.setText(_translate("MainWindow", "c", None))
        self.pbMul.setText(_translate("MainWindow", "×", None))
        self.pbEqu.setText(_translate("MainWindow", "=", None))
        self.label.setText(_translate("MainWindow", "", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

