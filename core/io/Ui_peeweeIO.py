# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/Desktop/Pyslvs-PyQt5/core/io/peeweeIO.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(497, 653)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.CommitTable_text = QtWidgets.QLabel(Form)
        self.CommitTable_text.setObjectName("CommitTable_text")
        self.verticalLayout_2.addWidget(self.CommitTable_text)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.commit_current_id = QtWidgets.QSpinBox(Form)
        self.commit_current_id.setEnabled(False)
        self.commit_current_id.setObjectName("commit_current_id")
        self.horizontalLayout_3.addWidget(self.commit_current_id)
        self.commit_search_text = QtWidgets.QLineEdit(Form)
        self.commit_search_text.setObjectName("commit_search_text")
        self.horizontalLayout_3.addWidget(self.commit_search_text)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.CommitTable = QtWidgets.QTableWidget(Form)
        self.CommitTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.CommitTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.CommitTable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.CommitTable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.CommitTable.setObjectName("CommitTable")
        self.CommitTable.setColumnCount(6)
        self.CommitTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.CommitTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.CommitTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.CommitTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.CommitTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.CommitTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.CommitTable.setHorizontalHeaderItem(5, item)
        self.verticalLayout_2.addWidget(self.CommitTable)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BranchList = QtWidgets.QListWidget(Form)
        self.BranchList.setObjectName("BranchList")
        self.horizontalLayout_2.addWidget(self.BranchList)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.branch_current = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.branch_current.sizePolicy().hasHeightForWidth())
        self.branch_current.setSizePolicy(sizePolicy)
        self.branch_current.setMaximumSize(QtCore.QSize(93, 16777215))
        self.branch_current.setReadOnly(True)
        self.branch_current.setObjectName("branch_current")
        self.verticalLayout.addWidget(self.branch_current)
        self.branch_checkout = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/git.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.branch_checkout.setIcon(icon)
        self.branch_checkout.setObjectName("branch_checkout")
        self.verticalLayout.addWidget(self.branch_checkout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.branch_delete = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.branch_delete.setIcon(icon1)
        self.branch_delete.setObjectName("branch_delete")
        self.verticalLayout.addWidget(self.branch_delete)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.AuthorList_text = QtWidgets.QLabel(Form)
        self.AuthorList_text.setObjectName("AuthorList_text")
        self.verticalLayout_2.addWidget(self.AuthorList_text)
        self.AuthorList = QtWidgets.QListWidget(Form)
        self.AuthorList.setObjectName("AuthorList")
        self.verticalLayout_2.addWidget(self.AuthorList)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FileAuthor_text = QtWidgets.QLabel(Form)
        self.FileAuthor_text.setObjectName("FileAuthor_text")
        self.horizontalLayout.addWidget(self.FileAuthor_text)
        self.FileAuthor = QtWidgets.QLineEdit(Form)
        self.FileAuthor.setObjectName("FileAuthor")
        self.horizontalLayout.addWidget(self.FileAuthor)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.FileDescription_text = QtWidgets.QLabel(Form)
        self.FileDescription_text.setObjectName("FileDescription_text")
        self.verticalLayout_2.addWidget(self.FileDescription_text)
        self.FileDescription = QtWidgets.QLineEdit(Form)
        self.FileDescription.setObjectName("FileDescription")
        self.verticalLayout_2.addWidget(self.FileDescription)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.commit_add = QtWidgets.QPushButton(Form)
        self.commit_add.setIcon(icon)
        self.commit_add.setObjectName("commit_add")
        self.horizontalLayout_4.addWidget(self.commit_add)
        self.branch_add = QtWidgets.QPushButton(Form)
        self.branch_add.setIcon(icon)
        self.branch_add.setObjectName("branch_add")
        self.horizontalLayout_4.addWidget(self.branch_add)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.commit_stash = QtWidgets.QPushButton(Form)
        self.commit_stash.setIcon(icon1)
        self.commit_stash.setObjectName("commit_stash")
        self.horizontalLayout_4.addWidget(self.commit_stash)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.CommitTable_text.setText(_translate("Form", "Commits:"))
        self.commit_current_id.setPrefix(_translate("Form", "#"))
        self.commit_search_text.setPlaceholderText(_translate("Form", "Filter: Enter a keyword about the commit description."))
        item = self.CommitTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.CommitTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Date"))
        item = self.CommitTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Description"))
        item = self.CommitTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Author"))
        item = self.CommitTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Previous"))
        item = self.CommitTable.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Branch"))
        self.label.setText(_translate("Form", "Branch list:"))
        self.branch_checkout.setStatusTip(_translate("Form", "Switch and load the latest commit of this branch."))
        self.branch_checkout.setText(_translate("Form", "Checkout"))
        self.branch_delete.setStatusTip(_translate("Form", "Remove all the commits on this branch."))
        self.branch_delete.setText(_translate("Form", "Delete"))
        self.AuthorList_text.setText(_translate("Form", "Author list:"))
        self.FileAuthor_text.setText(_translate("Form", "Author:"))
        self.FileDescription_text.setText(_translate("Form", "Description:"))
        self.FileDescription.setPlaceholderText(_translate("Form", "Explain what you have done here (required)."))
        self.commit_add.setStatusTip(_translate("Form", "Save the changes for this phase and provide backtracking points for this phase."))
        self.commit_add.setText(_translate("Form", "Commit"))
        self.branch_add.setStatusTip(_translate("Form", "Creat a new branch then save the commit to this branch."))
        self.branch_add.setText(_translate("Form", "New Branch"))
        self.commit_stash.setStatusTip(_translate("Form", "Abandon all changes of this time, and return to the latest commit."))
        self.commit_stash.setText(_translate("Form", "Stash"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

