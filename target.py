# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'target.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Target(object):
    def setupUi(self, Target):
        Target.setObjectName("Target")
        Target.resize(1027, 759)
        self.verticalLayout = QtWidgets.QVBoxLayout(Target)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Target)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Target)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.t1 = QtWidgets.QLineEdit(Target)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t1.sizePolicy().hasHeightForWidth())
        self.t1.setSizePolicy(sizePolicy)
        self.t1.setObjectName("t1")
        self.horizontalLayout.addWidget(self.t1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Target)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.t2 = QtWidgets.QLineEdit(Target)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t2.sizePolicy().hasHeightForWidth())
        self.t2.setSizePolicy(sizePolicy)
        self.t2.setObjectName("t2")
        self.horizontalLayout_2.addWidget(self.t2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Target)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.t3 = QtWidgets.QLineEdit(Target)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t3.sizePolicy().hasHeightForWidth())
        self.t3.setSizePolicy(sizePolicy)
        self.t3.setObjectName("t3")
        self.horizontalLayout_3.addWidget(self.t3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(Target)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.t4 = QtWidgets.QLineEdit(Target)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t4.sizePolicy().hasHeightForWidth())
        self.t4.setSizePolicy(sizePolicy)
        self.t4.setObjectName("t4")
        self.horizontalLayout_4.addWidget(self.t4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(Target)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.t5 = QtWidgets.QLineEdit(Target)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t5.sizePolicy().hasHeightForWidth())
        self.t5.setSizePolicy(sizePolicy)
        self.t5.setObjectName("t5")
        self.horizontalLayout_7.addWidget(self.t5)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(Target)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.t6 = QtWidgets.QLineEdit(Target)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t6.sizePolicy().hasHeightForWidth())
        self.t6.setSizePolicy(sizePolicy)
        self.t6.setObjectName("t6")
        self.horizontalLayout_6.addWidget(self.t6)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.discard = QtWidgets.QPushButton(Target)
        self.discard.setObjectName("discard")
        self.horizontalLayout_5.addWidget(self.discard)
        self.save = QtWidgets.QPushButton(Target)
        self.save.setObjectName("save")
        self.horizontalLayout_5.addWidget(self.save)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Target)
        QtCore.QMetaObject.connectSlotsByName(Target)



    def retranslateUi(self, Target):
        _translate = QtCore.QCoreApplication.translate
        Target.setWindowTitle(_translate("Target", "Dialog"))
        self.label.setText(_translate("Target", "crop preview"))
        self.label_2.setText(_translate("Target", "Shape"))
        self.label_3.setText(_translate("Target", "Shape Color"))
        self.label_4.setText(_translate("Target", "Character"))
        self.label_5.setText(_translate("Target", "Character Color"))
        self.label_8.setText(_translate("Target", "Orientation"))
        self.label_7.setText(_translate("Target", "CC"))
        self.discard.setText(_translate("Target", "Discard"))
        self.save.setText(_translate("Target", "Save"))



