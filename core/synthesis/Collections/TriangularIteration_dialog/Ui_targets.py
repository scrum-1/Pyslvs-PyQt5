# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ahshoe\Desktop\Pyslvs-PyQt5\core\synthesis\Collections\TriangularIteration_dialog\targets.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(346, 309)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/collection-triangular-iteration.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.main_label = QtWidgets.QLabel(Dialog)
        self.main_label.setObjectName("main_label")
        self.verticalLayout_4.addWidget(self.main_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.other_label = QtWidgets.QLabel(Dialog)
        self.other_label.setObjectName("other_label")
        self.verticalLayout_3.addWidget(self.other_label)
        self.other_list = QtWidgets.QListWidget(Dialog)
        self.other_list.setObjectName("other_list")
        self.verticalLayout_3.addWidget(self.other_list)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.targets_add = QtWidgets.QPushButton(Dialog)
        self.targets_add.setMaximumSize(QtCore.QSize(30, 16777215))
        self.targets_add.setObjectName("targets_add")
        self.verticalLayout.addWidget(self.targets_add)
        self.other_add = QtWidgets.QPushButton(Dialog)
        self.other_add.setMaximumSize(QtCore.QSize(30, 16777215))
        self.other_add.setObjectName("other_add")
        self.verticalLayout.addWidget(self.other_add)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.targets_label = QtWidgets.QLabel(Dialog)
        self.targets_label.setObjectName("targets_label")
        self.verticalLayout_2.addWidget(self.targets_label)
        self.targets_list = QtWidgets.QListWidget(Dialog)
        self.targets_list.setObjectName("targets_list")
        self.verticalLayout_2.addWidget(self.targets_list)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.main_label.setText(_translate("Dialog", "Choose the target point(s) to verify with path(s)."))
        self.other_label.setText(_translate("Dialog", "To be selected:"))
        self.targets_add.setText(_translate("Dialog", ">>"))
        self.other_add.setText(_translate("Dialog", "<<"))
        self.targets_label.setText(_translate("Dialog", "Tragets:"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

