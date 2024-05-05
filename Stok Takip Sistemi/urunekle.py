# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urunekle.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(429, 411)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 50, 321, 311))
        self.label.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"border-radius:20;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit_ad = QtWidgets.QLineEdit(Form)
        self.lineEdit_ad.setGeometry(QtCore.QRect(105, 150, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_ad.setFont(font)
        self.lineEdit_ad.setStyleSheet("border-radius:20;")
        self.lineEdit_ad.setText("")
        self.lineEdit_ad.setObjectName("lineEdit_ad")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_miktar = QtWidgets.QLineEdit(Form)
        self.lineEdit_miktar.setGeometry(QtCore.QRect(105, 200, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_miktar.setFont(font)
        self.lineEdit_miktar.setStyleSheet("border-radius:20;")
        self.lineEdit_miktar.setText("")
        self.lineEdit_miktar.setObjectName("lineEdit_miktar")
        self.pushButton_ekle = QtWidgets.QPushButton(Form)
        self.pushButton_ekle.setGeometry(QtCore.QRect(125, 270, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ekle.setFont(font)
        self.pushButton_ekle.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(216, 216, 216);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(163, 163, 163);\n"
"}")
        self.pushButton_ekle.setObjectName("pushButton_ekle")
        self.pushButton_iptal = QtWidgets.QPushButton(Form)
        self.pushButton_iptal.setGeometry(QtCore.QRect(135, 320, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_iptal.setFont(font)
        self.pushButton_iptal.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(168, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(176, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_iptal.setObjectName("pushButton_iptal")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_ad.setPlaceholderText(_translate("Form", "Ürün Adı"))
        self.label_2.setText(_translate("Form", "Ürün Ekleme"))
        self.lineEdit_miktar.setPlaceholderText(_translate("Form", "Stok Miktarı"))
        self.pushButton_ekle.setText(_translate("Form", "Ürün Ekle"))
        self.pushButton_iptal.setText(_translate("Form", "İptal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
