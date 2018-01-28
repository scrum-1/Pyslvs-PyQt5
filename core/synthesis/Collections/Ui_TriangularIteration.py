# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/桌面/Pyslvs-PyQt5/core/synthesis/Collections/TriangularIteration.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(348, 712)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/collection-triangular-iteration.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.addToCollection_button = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/collection-structure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addToCollection_button.setIcon(icon1)
        self.addToCollection_button.setObjectName("addToCollection_button")
        self.horizontalLayout_4.addWidget(self.addToCollection_button)
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_4.addWidget(self.line_5)
        self.load_button = QtWidgets.QPushButton(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/data.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.load_button.setIcon(icon2)
        self.load_button.setObjectName("load_button")
        self.horizontalLayout_4.addWidget(self.load_button)
        self.clear_button = QtWidgets.QPushButton(Form)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/newfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_button.setIcon(icon3)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_4.addWidget(self.clear_button)
        self.save_button = QtWidgets.QPushButton(Form)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/savefile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_button.setIcon(icon4)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_4.addWidget(self.save_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_9.addWidget(self.line)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.main_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName("main_layout")
        self.joint_panel = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.joint_panel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.joint_panel.setObjectName("joint_panel")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.joint_panel)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.joint_name_label = QtWidgets.QLabel(self.joint_panel)
        self.joint_name_label.setObjectName("joint_name_label")
        self.verticalLayout_6.addWidget(self.joint_name_label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.joint_name = QtWidgets.QComboBox(self.joint_panel)
        self.joint_name.setObjectName("joint_name")
        self.horizontalLayout_5.addWidget(self.joint_name)
        self.add_customization = QtWidgets.QPushButton(self.joint_panel)
        self.add_customization.setMaximumSize(QtCore.QSize(30, 16777215))
        self.add_customization.setObjectName("add_customization")
        self.horizontalLayout_5.addWidget(self.add_customization)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.status_label = QtWidgets.QLabel(self.joint_panel)
        self.status_label.setObjectName("status_label")
        self.verticalLayout_6.addWidget(self.status_label)
        self.status = QtWidgets.QLabel(self.joint_panel)
        self.status.setObjectName("status")
        self.verticalLayout_6.addWidget(self.status)
        self.solution_label = QtWidgets.QLabel(self.joint_panel)
        self.solution_label.setObjectName("solution_label")
        self.verticalLayout_6.addWidget(self.solution_label)
        self.PLAP_solution = QtWidgets.QPushButton(self.joint_panel)
        self.PLAP_solution.setEnabled(False)
        self.PLAP_solution.setObjectName("PLAP_solution")
        self.verticalLayout_6.addWidget(self.PLAP_solution)
        self.PLLP_solution = QtWidgets.QPushButton(self.joint_panel)
        self.PLLP_solution.setEnabled(False)
        self.PLLP_solution.setObjectName("PLLP_solution")
        self.verticalLayout_6.addWidget(self.PLLP_solution)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.main_layout.addWidget(self.joint_panel)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_7.addWidget(self.line_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Driver_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Driver_label.setObjectName("Driver_label")
        self.verticalLayout_2.addWidget(self.Driver_label)
        self.Driver_list = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.Driver_list.setObjectName("Driver_list")
        self.verticalLayout_2.addWidget(self.Driver_list)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.Driver_add = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Driver_add.setMaximumSize(QtCore.QSize(30, 16777215))
        self.Driver_add.setObjectName("Driver_add")
        self.verticalLayout_11.addWidget(self.Driver_add)
        self.Follower_add = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Follower_add.setMaximumSize(QtCore.QSize(30, 16777215))
        self.Follower_add.setObjectName("Follower_add")
        self.verticalLayout_11.addWidget(self.Follower_add)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Follower_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Follower_label.setObjectName("Follower_label")
        self.verticalLayout_4.addWidget(self.Follower_label)
        self.Follower_list = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.Follower_list.setObjectName("Follower_list")
        self.verticalLayout_4.addWidget(self.Follower_list)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.grounded_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.grounded_label.setObjectName("grounded_label")
        self.verticalLayout_15.addWidget(self.grounded_label)
        self.grounded_list = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.grounded_list.setObjectName("grounded_list")
        self.verticalLayout_15.addWidget(self.grounded_list)
        self.horizontalLayout.addLayout(self.verticalLayout_15)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_7.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Target_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Target_label.sizePolicy().hasHeightForWidth())
        self.Target_label.setSizePolicy(sizePolicy)
        self.Target_label.setObjectName("Target_label")
        self.horizontalLayout_7.addWidget(self.Target_label)
        self.Target_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Target_button.setObjectName("Target_button")
        self.horizontalLayout_7.addWidget(self.Target_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.Target_list = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.Target_list.setObjectName("Target_list")
        self.verticalLayout_3.addWidget(self.Target_list)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.constraints_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.constraints_button.setObjectName("constraints_button")
        self.verticalLayout_5.addWidget(self.constraints_button)
        self.constraint_list = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.constraint_list.setObjectName("constraint_list")
        self.verticalLayout_5.addWidget(self.constraint_list)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.show_solutions = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_solutions.sizePolicy().hasHeightForWidth())
        self.show_solutions.setSizePolicy(sizePolicy)
        self.show_solutions.setChecked(True)
        self.show_solutions.setObjectName("show_solutions")
        self.horizontalLayout_6.addWidget(self.show_solutions)
        self.Expression_list_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Expression_list_label.setObjectName("Expression_list_label")
        self.horizontalLayout_6.addWidget(self.Expression_list_label)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.Expression_list = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.Expression_list.setObjectName("Expression_list")
        self.verticalLayout_10.addWidget(self.Expression_list)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Expression_pop = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Expression_pop.setMaximumSize(QtCore.QSize(16777215, 24))
        self.Expression_pop.setObjectName("Expression_pop")
        self.horizontalLayout_8.addWidget(self.Expression_pop)
        self.Expression_clear = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Expression_clear.setIcon(icon5)
        self.Expression_clear.setObjectName("Expression_clear")
        self.horizontalLayout_8.addWidget(self.Expression_clear)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Link_Expression_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Link_Expression_label.setObjectName("Link_Expression_label")
        self.verticalLayout.addWidget(self.Link_Expression_label)
        self.Link_Expression = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Link_Expression.setReadOnly(True)
        self.Link_Expression.setObjectName("Link_Expression")
        self.verticalLayout.addWidget(self.Link_Expression)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Expression_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Expression_label.setObjectName("Expression_label")
        self.verticalLayout_8.addWidget(self.Expression_label)
        self.Expression = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Expression.setReadOnly(True)
        self.Expression.setObjectName("Expression")
        self.verticalLayout_8.addWidget(self.Expression)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout_9.addWidget(self.splitter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addToCollection_button.setStatusTip(_translate("Form", "Turn this structure diagram back to structure collections."))
        self.load_button.setStatusTip(_translate("Form", "Triangular iteration data and common structure data collections."))
        self.load_button.setText(_translate("Form", "Collections"))
        self.clear_button.setStatusTip(_translate("Form", "Create a new iteration profile."))
        self.save_button.setStatusTip(_translate("Form", "Save this iteration profile to data collections."))
        self.joint_name_label.setText(_translate("Form", "Joint:"))
        self.joint_name.setStatusTip(_translate("Form", "Choose a joint tag to see it\'s status."))
        self.add_customization.setStatusTip(_translate("Form", "Customize joints and multiple joints option interface."))
        self.add_customization.setText(_translate("Form", "..."))
        self.status_label.setText(_translate("Form", "Status:"))
        self.status.setStatusTip(_translate("Form", "Each joint should have a solution to find out it\'s position."))
        self.status.setText(_translate("Form", "N/A"))
        self.solution_label.setText(_translate("Form", "Solutions:"))
        self.PLAP_solution.setText(_translate("Form", "PLAP"))
        self.PLLP_solution.setText(_translate("Form", "PLLP"))
        self.Driver_label.setText(_translate("Form", "Drivers:"))
        self.Driver_list.setStatusTip(_translate("Form", "These joints will setup an revolute input. The number of them as same as DOF."))
        self.Driver_add.setText(_translate("Form", "<<"))
        self.Follower_add.setText(_translate("Form", ">>"))
        self.Follower_label.setText(_translate("Form", "Followers:"))
        self.Follower_list.setStatusTip(_translate("Form", "These joints are on the grounded link, the position of them will generate. So they are don\'t need to have a solution."))
        self.label.setText(_translate("Form", "<<"))
        self.grounded_label.setText(_translate("Form", "Gounded:"))
        self.grounded_list.setStatusTip(_translate("Form", "Set a link as the ground. Existing solutions will be reset."))
        self.Target_button.setText(_translate("Form", "Targets"))
        self.Target_list.setStatusTip(_translate("Form", "Target points will match as the target path of dimensional synthesis."))
        self.constraints_button.setText(_translate("Form", "Constraints"))
        self.constraint_list.setStatusTip(_translate("Form", "Four bar loop to apply Gruebler\'s Equation."))
        self.show_solutions.setStatusTip(_translate("Form", "Show triangle sketch on preview window."))
        self.Expression_list_label.setText(_translate("Form", "Solutions:"))
        self.Expression_list.setStatusTip(_translate("Form", "Solutions to find all the positions of joints."))
        self.Expression_pop.setStatusTip(_translate("Form", "Remove the last solution."))
        self.Expression_pop.setText(_translate("Form", "-"))
        self.Expression_clear.setStatusTip(_translate("Form", "Clear all the solutions."))
        self.Link_Expression_label.setText(_translate("Form", "Link expression:"))
        self.Link_Expression.setStatusTip(_translate("Form", "Link relative expression."))
        self.Expression_label.setText(_translate("Form", "Expression:"))
        self.Expression.setStatusTip(_translate("Form", "Triangular iteration expression."))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

