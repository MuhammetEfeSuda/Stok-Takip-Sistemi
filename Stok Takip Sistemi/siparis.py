# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'siparis.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(512, 601)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 50, 411, 511))
        self.label.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"border-radius:20;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.tableWidget_Urun = QtWidgets.QTableWidget(Form)
        self.tableWidget_Urun.setGeometry(QtCore.QRect(80, 80, 351, 371))
        self.tableWidget_Urun.setStyleSheet("")
        self.tableWidget_Urun.setObjectName("tableWidget_Urun")
        self.tableWidget_Urun.setColumnCount(3)
        self.tableWidget_Urun.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Urun.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Urun.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Urun.setHorizontalHeaderItem(2, item)
        self.pushButton_Siparis = QtWidgets.QPushButton(Form)
        self.pushButton_Siparis.setGeometry(QtCore.QRect(140, 465, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Siparis.setFont(font)
        self.pushButton_Siparis.setStyleSheet("QPushButton {\n"
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
        self.pushButton_Siparis.setObjectName("pushButton_Siparis")
        self.pushButton_Geri = QtWidgets.QPushButton(Form)
        self.pushButton_Geri.setGeometry(QtCore.QRect(180, 515, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Geri.setFont(font)
        self.pushButton_Geri.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(168, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.pushButton_Geri.setObjectName("pushButton_Geri")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget_Urun.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Ürün No"))
        item = self.tableWidget_Urun.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Ürün Adı"))
        item = self.tableWidget_Urun.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Stok Miktarı"))
        self.pushButton_Siparis.setText(_translate("Form", "Sipariş Oluştur"))
        self.pushButton_Geri.setText(_translate("Form", "Geri"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
