# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dirSettingsDialog.ui'
#
# Created: Fri Nov 23 14:27:45 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_dirSettingsDialog(object):
    def setupUi(self, dirSettingsDialog):
        dirSettingsDialog.setObjectName(_fromUtf8("dirSettingsDialog"))
        dirSettingsDialog.resize(418, 155)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("宋体"))
        font.setPointSize(10)
        dirSettingsDialog.setFont(font)
        self.layoutWidget = QtGui.QWidget(dirSettingsDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 110, 158, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.okButton = QtGui.QPushButton(self.layoutWidget)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout_3.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(self.layoutWidget)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_3.addWidget(self.cancelButton)
        self.layoutWidget1 = QtGui.QWidget(dirSettingsDialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 30, 332, 58))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("宋体"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.mp3LocationEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.mp3LocationEdit.setObjectName(_fromUtf8("mp3LocationEdit"))
        self.horizontalLayout.addWidget(self.mp3LocationEdit)
        self.mp3LocationButton = QtGui.QPushButton(self.layoutWidget1)
        self.mp3LocationButton.setObjectName(_fromUtf8("mp3LocationButton"))
        self.horizontalLayout.addWidget(self.mp3LocationButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("宋体"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lrcLocationEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.lrcLocationEdit.setObjectName(_fromUtf8("lrcLocationEdit"))
        self.horizontalLayout_2.addWidget(self.lrcLocationEdit)
        self.lrcLocationButton = QtGui.QPushButton(self.layoutWidget1)
        self.lrcLocationButton.setObjectName(_fromUtf8("lrcLocationButton"))
        self.horizontalLayout_2.addWidget(self.lrcLocationButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(dirSettingsDialog)
#        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), dirSettingsDialog.close)
        QtCore.QMetaObject.connectSlotsByName(dirSettingsDialog)

    def retranslateUi(self, dirSettingsDialog):
        dirSettingsDialog.setWindowTitle(QtGui.QApplication.translate("dirSettingsDialog", "设置", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("dirSettingsDialog", "确定", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("dirSettingsDialog", "取消", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dirSettingsDialog", "歌曲存放目录：", None, QtGui.QApplication.UnicodeUTF8))
        self.mp3LocationButton.setText(QtGui.QApplication.translate("dirSettingsDialog", "选择目录", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dirSettingsDialog", "歌词存放目录：", None, QtGui.QApplication.UnicodeUTF8))
        self.lrcLocationButton.setText(QtGui.QApplication.translate("dirSettingsDialog", "选择目录", None, QtGui.QApplication.UnicodeUTF8))

