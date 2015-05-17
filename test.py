# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Fri Jan 30 21:35:53 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_imageGUI(object):
    def setupUi(self, imageGUI):
        imageGUI.setObjectName(_fromUtf8("imageGUI"))
        imageGUI.resize(750, 150)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(imageGUI.sizePolicy().hasHeightForWidth())
        imageGUI.setSizePolicy(sizePolicy)
        imageGUI.setMinimumSize(QtCore.QSize(750, 150))
        imageGUI.setMaximumSize(QtCore.QSize(750, 150))
        self.layoutWidget = QtGui.QWidget(imageGUI)
        self.layoutWidget.setGeometry(QtCore.QRect(440, 60, 158, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.saveAsImageButton = QtGui.QPushButton(self.layoutWidget)
        self.saveAsImageButton.setObjectName(_fromUtf8("saveAsImageButton"))
        self.horizontalLayout_2.addWidget(self.saveAsImageButton)
        self.extractButton1 = QtGui.QPushButton(self.layoutWidget)
        self.extractButton1.setObjectName(_fromUtf8("extractButton1"))
        self.horizontalLayout_2.addWidget(self.extractButton1)
        self.verticalLayoutWidget_2 = QtGui.QWidget(imageGUI)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(610, 20, 101, 58))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.splitter_2 = QtGui.QSplitter(self.verticalLayoutWidget_2)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.openImageButton = QtGui.QPushButton(self.splitter_2)
        self.openImageButton.setObjectName(_fromUtf8("openImageButton"))
        self.openVideoButton = QtGui.QPushButton(self.splitter_2)
        self.openVideoButton.setObjectName(_fromUtf8("openVideoButton"))
        self.verticalLayout_4.addWidget(self.splitter_2)
        self.verticalLayoutWidget_3 = QtGui.QWidget(imageGUI)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 60, 351, 51))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.splitter_5 = QtGui.QSplitter(self.verticalLayoutWidget_3)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))
        self.splitter_3 = QtGui.QSplitter(self.splitter_5)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.splitter_4 = QtGui.QSplitter(self.splitter_3)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.label = QtGui.QLabel(self.splitter_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.threadSlider = QtGui.QSlider(self.splitter_3)
        self.threadSlider.setMaximum(300)
        self.threadSlider.setOrientation(QtCore.Qt.Horizontal)
        self.threadSlider.setObjectName(_fromUtf8("threadSlider"))
        self.splitter = QtGui.QSplitter(self.splitter_5)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_3 = QtGui.QLabel(self.splitter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.weightSrc = QtGui.QSlider(self.splitter)
        self.weightSrc.setMaximum(100)
        self.weightSrc.setOrientation(QtCore.Qt.Horizontal)
        self.weightSrc.setObjectName(_fromUtf8("weightSrc"))
        self.verticalLayout_5.addWidget(self.splitter_5)
        self.verticalLayoutWidget_4 = QtGui.QWidget(imageGUI)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 581, 28))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.filePath = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.filePath.setObjectName(_fromUtf8("filePath"))
        self.verticalLayout_6.addWidget(self.filePath)

        self.retranslateUi(imageGUI)
        QtCore.QMetaObject.connectSlotsByName(imageGUI)

    def retranslateUi(self, imageGUI):
        imageGUI.setWindowTitle(_translate("imageGUI", "Dialog", None))
        self.saveAsImageButton.setText(_translate("imageGUI", "Save", None))
        self.extractButton1.setText(_translate("imageGUI", "Extract", None))
        self.openImageButton.setText(_translate("imageGUI", "Open Image File", None))
        self.openVideoButton.setText(_translate("imageGUI", "Open Video File", None))
        self.label.setText(_translate("imageGUI", "Thread", None))
        self.label_3.setText(_translate("imageGUI", "Weight of src", None))

