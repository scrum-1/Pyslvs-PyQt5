# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ahshoe\Desktop\Pyslvs-PyQt5\core\panel\run_Path_Solving.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(521, 492)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(521, 492))
        Dialog.setMaximumSize(QtCore.QSize(521, 492))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/bezier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pointNum = QtWidgets.QLabel(Dialog)
        self.pointNum.setObjectName("pointNum")
        self.horizontalLayout_4.addWidget(self.pointNum)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.mainPanel = QtWidgets.QWidget(Dialog)
        self.mainPanel.setObjectName("mainPanel")
        self.mainPanelLayout = QtWidgets.QHBoxLayout(self.mainPanel)
        self.mainPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.mainPanelLayout.setObjectName("mainPanelLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Point_list = QtWidgets.QListWidget(self.mainPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Point_list.sizePolicy().hasHeightForWidth())
        self.Point_list.setSizePolicy(sizePolicy)
        self.Point_list.setObjectName("Point_list")
        self.verticalLayout_2.addWidget(self.Point_list)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.mainPanel)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.X_coordinate = QtWidgets.QLineEdit(self.mainPanel)
        self.X_coordinate.setObjectName("X_coordinate")
        self.horizontalLayout_3.addWidget(self.X_coordinate)
        self.label_4 = QtWidgets.QLabel(self.mainPanel)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.Y_coordinate = QtWidgets.QLineEdit(self.mainPanel)
        self.Y_coordinate.setObjectName("Y_coordinate")
        self.horizontalLayout_3.addWidget(self.Y_coordinate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.mainPanelLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.clearAll = QtWidgets.QPushButton(self.mainPanel)
        self.clearAll.setObjectName("clearAll")
        self.verticalLayout.addWidget(self.clearAll)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.moveUp = QtWidgets.QPushButton(self.mainPanel)
        self.moveUp.setObjectName("moveUp")
        self.verticalLayout.addWidget(self.moveUp)
        self.moveDown = QtWidgets.QPushButton(self.mainPanel)
        self.moveDown.setObjectName("moveDown")
        self.verticalLayout.addWidget(self.moveDown)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.remove = QtWidgets.QPushButton(self.mainPanel)
        self.remove.setObjectName("remove")
        self.verticalLayout.addWidget(self.remove)
        self.add = QtWidgets.QPushButton(self.mainPanel)
        self.add.setObjectName("add")
        self.verticalLayout.addWidget(self.add)
        self.mainPanelLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.mainPanel)
        self.startPanel = QtWidgets.QWidget(Dialog)
        self.startPanel.setObjectName("startPanel")
        self.startPanelLayout = QtWidgets.QHBoxLayout(self.startPanel)
        self.startPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.startPanelLayout.setObjectName("startPanelLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.startPanelLayout.addItem(spacerItem4)
        self.Generate = QtWidgets.QPushButton(self.startPanel)
        self.Generate.setObjectName("Generate")
        self.startPanelLayout.addWidget(self.Generate)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.startPanelLayout.addItem(spacerItem5)
        self.verticalLayout_3.addWidget(self.startPanel)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Path Solving"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Choose the points in the path as you want.</span></p><p><span style=\" font-size:12pt;\">This generator will design a crank rocker to meet this path requirement.</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Point(s):</span></p></body></html>"))
        self.pointNum.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aa00;\">0</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aa00;\">Point(s).</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "x: "))
        self.X_coordinate.setPlaceholderText(_translate("Dialog", "0.0"))
        self.label_4.setText(_translate("Dialog", "y: "))
        self.Y_coordinate.setPlaceholderText(_translate("Dialog", "0.0"))
        self.clearAll.setText(_translate("Dialog", "Clear All"))
        self.moveUp.setText(_translate("Dialog", "Move up"))
        self.moveDown.setText(_translate("Dialog", "Move down"))
        self.remove.setText(_translate("Dialog", "-"))
        self.add.setText(_translate("Dialog", "+"))
        self.Generate.setText(_translate("Dialog", "Generate"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

