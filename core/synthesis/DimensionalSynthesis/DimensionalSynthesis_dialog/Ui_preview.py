# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/桌面/Pyslvs-PyQt5/core/synthesis/DimensionalSynthesis/DimensionalSynthesis_dialog/preview.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        Dialog.setMinimumSize(QtCore.QSize(800, 600))
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.information_tab = QtWidgets.QTabWidget(Dialog)
        self.information_tab.setObjectName("information_tab")
        self.geometry = QtWidgets.QWidget()
        self.geometry.setObjectName("geometry")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.geometry)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.geometry)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(3)
        self.splitter.setObjectName("splitter")
        self.leftWidget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftWidget.sizePolicy().hasHeightForWidth())
        self.leftWidget.setSizePolicy(sizePolicy)
        self.leftWidget.setObjectName("leftWidget")
        self.left_layout = QtWidgets.QHBoxLayout(self.leftWidget)
        self.left_layout.setContentsMargins(0, 0, 0, 0)
        self.left_layout.setObjectName("left_layout")
        self.line = QtWidgets.QFrame(self.leftWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.left_layout.addWidget(self.line)
        self.rightWidget = QtWidgets.QWidget(self.splitter)
        self.rightWidget.setObjectName("rightWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.rightWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.basic_groupbox = QtWidgets.QGroupBox(self.rightWidget)
        self.basic_groupbox.setObjectName("basic_groupbox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.basic_groupbox)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.basic_label = QtWidgets.QLabel(self.basic_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.basic_label.sizePolicy().hasHeightForWidth())
        self.basic_label.setSizePolicy(sizePolicy)
        self.basic_label.setObjectName("basic_label")
        self.verticalLayout_4.addWidget(self.basic_label)
        spacerItem = QtWidgets.QSpacerItem(20, 47, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.basic_groupbox)
        self.algorithm_groupbox = QtWidgets.QGroupBox(self.rightWidget)
        self.algorithm_groupbox.setObjectName("algorithm_groupbox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.algorithm_groupbox)
        self.verticalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.algorithm_groupbox)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 735, 186))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.algorithm_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.algorithm_label.sizePolicy().hasHeightForWidth())
        self.algorithm_label.setSizePolicy(sizePolicy)
        self.algorithm_label.setObjectName("algorithm_label")
        self.verticalLayout_5.addWidget(self.algorithm_label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 201, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.addWidget(self.scrollArea_2)
        self.verticalLayout_2.addWidget(self.algorithm_groupbox)
        self.hardware_groupbox = QtWidgets.QGroupBox(self.rightWidget)
        self.hardware_groupbox.setObjectName("hardware_groupbox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.hardware_groupbox)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.hardware_groupbox)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 735, 186))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.hardware_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hardware_label.sizePolicy().hasHeightForWidth())
        self.hardware_label.setSizePolicy(sizePolicy)
        self.hardware_label.setObjectName("hardware_label")
        self.verticalLayout_8.addWidget(self.hardware_label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 201, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.scrollArea_3)
        self.verticalLayout_2.addWidget(self.hardware_groupbox)
        self.verticalLayout.addWidget(self.splitter)
        self.information_tab.addTab(self.geometry, "")
        self.verticalLayout_6.addWidget(self.information_tab)

        self.retranslateUi(Dialog)
        self.information_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.basic_groupbox.setTitle(_translate("Dialog", "Basic information"))
        self.basic_label.setText(_translate("Dialog", "TextLabel"))
        self.algorithm_groupbox.setTitle(_translate("Dialog", "Algorithm information"))
        self.algorithm_label.setText(_translate("Dialog", "TextLabel"))
        self.hardware_groupbox.setTitle(_translate("Dialog", "Hardware information"))
        self.hardware_label.setText(_translate("Dialog", "TextLabel"))
        self.information_tab.setTabText(self.information_tab.indexOf(self.geometry), _translate("Dialog", "Geometry"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

