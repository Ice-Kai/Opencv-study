# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_image = QtWidgets.QLabel(Dialog)
        self.label_image.setObjectName("label_image")
        self.gridLayout.addWidget(self.label_image, 1, 0, 1, 1)
        self.btn_choose = QtWidgets.QPushButton(Dialog)
        self.btn_choose.setObjectName("btn_choose")
        self.gridLayout.addWidget(self.btn_choose, 2, 0, 1, 1)
        self.btn_identify = QtWidgets.QPushButton(Dialog)
        self.btn_identify.setObjectName("btn_identify")
        self.gridLayout.addWidget(self.btn_identify, 3, 0, 1, 1)
        self.label_result = QtWidgets.QLabel(Dialog)
        self.label_result.setObjectName("label_result")
        self.gridLayout.addWidget(self.label_result, 4, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "要识别的图片："))
        self.label_image.setText(_translate("Dialog", "图片"))
        self.btn_choose.setText(_translate("Dialog", "选择图片"))
        self.btn_identify.setText(_translate("Dialog", "识别图片"))
        self.label_result.setText(_translate("Dialog", "显示识别结果"))
