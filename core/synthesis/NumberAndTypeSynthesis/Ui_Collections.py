# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/Desktop/Pyslvs-PyQt5/core/synthesis/NumberAndTypeSynthesis/Collections.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(439, 630)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/collections.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graph_engine_text = QtWidgets.QLabel(Form)
        self.graph_engine_text.setObjectName("graph_engine_text")
        self.horizontalLayout.addWidget(self.graph_engine_text)
        self.graph_engine = QtWidgets.QComboBox(Form)
        self.graph_engine.setObjectName("graph_engine")
        self.horizontalLayout.addWidget(self.graph_engine)
        self.reload_atlas = QtWidgets.QPushButton(Form)
        self.reload_atlas.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/dataupdate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reload_atlas.setIcon(icon1)
        self.reload_atlas.setObjectName("reload_atlas")
        self.horizontalLayout.addWidget(self.reload_atlas)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.graph_link_as_node = QtWidgets.QCheckBox(Form)
        self.graph_link_as_node.setObjectName("graph_link_as_node")
        self.horizontalLayout.addWidget(self.graph_link_as_node)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.add_by_edges_button = QtWidgets.QPushButton(Form)
        self.add_by_edges_button.setObjectName("add_by_edges_button")
        self.verticalLayout_3.addWidget(self.add_by_edges_button)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.collection_list = QtWidgets.QListWidget(self.splitter)
        self.collection_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.collection_list.setIconSize(QtCore.QSize(100, 100))
        self.collection_list.setMovement(QtWidgets.QListView.Static)
        self.collection_list.setResizeMode(QtWidgets.QListView.Adjust)
        self.collection_list.setViewMode(QtWidgets.QListView.IconMode)
        self.collection_list.setUniformItemSizes(True)
        self.collection_list.setObjectName("collection_list")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Preview_window = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.Preview_window.setMinimumSize(QtCore.QSize(210, 230))
        self.Preview_window.setMaximumSize(QtCore.QSize(210, 230))
        self.Preview_window.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.Preview_window.setIconSize(QtCore.QSize(200, 200))
        self.Preview_window.setMovement(QtWidgets.QListView.Static)
        self.Preview_window.setViewMode(QtWidgets.QListView.IconMode)
        self.Preview_window.setObjectName("Preview_window")
        self.horizontalLayout_2.addWidget(self.Preview_window)
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 230))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Expression_edges = QtWidgets.QLineEdit(self.widget)
        self.Expression_edges.setReadOnly(True)
        self.Expression_edges.setObjectName("Expression_edges")
        self.horizontalLayout_3.addWidget(self.Expression_edges)
        self.Expression_copy = QtWidgets.QPushButton(self.widget)
        self.Expression_copy.setObjectName("Expression_copy")
        self.horizontalLayout_3.addWidget(self.Expression_copy)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.NL_text = QtWidgets.QLabel(self.widget)
        self.NL_text.setObjectName("NL_text")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.NL_text)
        self.NL = QtWidgets.QLabel(self.widget)
        self.NL.setObjectName("NL")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.NL)
        self.NJ_text = QtWidgets.QLabel(self.widget)
        self.NJ_text.setObjectName("NJ_text")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.NJ_text)
        self.NJ = QtWidgets.QLabel(self.widget)
        self.NJ.setObjectName("NJ")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.NJ)
        self.DOF_text = QtWidgets.QLabel(self.widget)
        self.DOF_text.setObjectName("DOF_text")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.DOF_text)
        self.DOF = QtWidgets.QLabel(self.widget)
        self.DOF.setObjectName("DOF")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.DOF)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.delete_button = QtWidgets.QPushButton(self.widget)
        self.delete_button.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon2)
        self.delete_button.setObjectName("delete_button")
        self.verticalLayout_2.addWidget(self.delete_button)
        self.grounded_button = QtWidgets.QPushButton(self.widget)
        self.grounded_button.setEnabled(False)
        self.grounded_button.setIcon(icon1)
        self.grounded_button.setObjectName("grounded_button")
        self.verticalLayout_2.addWidget(self.grounded_button)
        self.horizontalLayout_2.addWidget(self.widget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.grounded_list = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.grounded_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.grounded_list.setIconSize(QtCore.QSize(150, 150))
        self.grounded_list.setMovement(QtWidgets.QListView.Static)
        self.grounded_list.setResizeMode(QtWidgets.QListView.Adjust)
        self.grounded_list.setViewMode(QtWidgets.QListView.IconMode)
        self.grounded_list.setUniformItemSizes(True)
        self.grounded_list.setObjectName("grounded_list")
        self.horizontalLayout_4.addWidget(self.grounded_list)
        self.grounded_merge = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.grounded_merge.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grounded_merge.sizePolicy().hasHeightForWidth())
        self.grounded_merge.setSizePolicy(sizePolicy)
        self.grounded_merge.setObjectName("grounded_merge")
        self.horizontalLayout_4.addWidget(self.grounded_merge)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addWidget(self.splitter)

        self.retranslateUi(Form)
        self.graph_engine.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.graph_engine_text.setText(_translate("Form", "Engine: "))
        self.graph_link_as_node.setText(_translate("Form", "Linkage as node"))
        self.add_by_edges_button.setText(_translate("Form", "Add by edges"))
        self.Expression_copy.setText(_translate("Form", "Copy"))
        self.NL_text.setText(_translate("Form", "Number of links:"))
        self.NL.setText(_translate("Form", "0"))
        self.NJ_text.setText(_translate("Form", "Number of joints:"))
        self.NJ.setText(_translate("Form", "0"))
        self.DOF_text.setText(_translate("Form", "Degree of freedom:"))
        self.DOF.setText(_translate("Form", "0"))
        self.delete_button.setText(_translate("Form", "Delete"))
        self.grounded_button.setText(_translate("Form", "Generate layout"))
        self.grounded_merge.setText(_translate("Form", "Merge"))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

