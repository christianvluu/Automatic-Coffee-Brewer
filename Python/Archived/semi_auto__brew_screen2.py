# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'semi_auto_brew_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class SemiAutoBrewScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 641, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.titleLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout.addWidget(self.titleLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(190, 80, 261, 91))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.externalTempLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.externalTempLabel.setObjectName("externalTempLabel")
        self.gridLayout_2.addWidget(self.externalTempLabel, 2, 0, 1, 1)
        self.internalTempLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.internalTempLabel.setObjectName("internalTempLabel")
        self.gridLayout_2.addWidget(self.internalTempLabel, 1, 0, 1, 1)
        self.internalTempEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.internalTempEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.internalTempEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.internalTempEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.internalTempEdit.setReadOnly(True)
        self.internalTempEdit.setObjectName("internalTempEdit")
        self.gridLayout_2.addWidget(self.internalTempEdit, 1, 1, 1, 1)
        self.externalTempEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.externalTempEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.externalTempEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.externalTempEdit.setReadOnly(True)
        self.externalTempEdit.setObjectName("externalTempEdit")
        self.gridLayout_2.addWidget(self.externalTempEdit, 2, 1, 1, 1)
        self.tempLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tempLabel.setFont(font)
        self.tempLabel.setObjectName("tempLabel")
        self.gridLayout_2.addWidget(self.tempLabel, 0, 0, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 190, 534, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.minus1Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.minus1Button.setMinimumSize(QtCore.QSize(40, 40))
        self.minus1Button.setMaximumSize(QtCore.QSize(40, 40))
        self.minus1Button.setAutoRepeat(True)
        self.minus1Button.setObjectName("minus1Button")
        self.gridLayout.addWidget(self.minus1Button, 1, 3, 1, 1)
        self.minus10Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.minus10Button.sizePolicy().hasHeightForWidth())
        self.minus10Button.setSizePolicy(sizePolicy)
        self.minus10Button.setMinimumSize(QtCore.QSize(40, 40))
        self.minus10Button.setAutoRepeat(True)
        self.minus10Button.setObjectName("minus10Button")
        self.gridLayout.addWidget(self.minus10Button, 1, 1, 1, 1)
        self.plus5Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.plus5Button.setMinimumSize(QtCore.QSize(40, 40))
        self.plus5Button.setMaximumSize(QtCore.QSize(40, 40))
        self.plus5Button.setAutoRepeat(True)
        self.plus5Button.setObjectName("plus5Button")
        self.gridLayout.addWidget(self.plus5Button, 1, 6, 1, 1)
        self.minus5Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.minus5Button.setMinimumSize(QtCore.QSize(40, 40))
        self.minus5Button.setMaximumSize(QtCore.QSize(40, 40))
        self.minus5Button.setAutoRepeat(True)
        self.minus5Button.setObjectName("minus5Button")
        self.gridLayout.addWidget(self.minus5Button, 1, 2, 1, 1)
        self.plus1Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.plus1Button.setMinimumSize(QtCore.QSize(40, 40))
        self.plus1Button.setMaximumSize(QtCore.QSize(40, 40))
        self.plus1Button.setAutoRepeat(True)
        self.plus1Button.setObjectName("plus1Button")
        self.gridLayout.addWidget(self.plus1Button, 1, 5, 1, 1)
        self.setTempEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.setTempEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.setTempEdit.setReadOnly(True)
        self.setTempEdit.setObjectName("setTempEdit")
        self.gridLayout.addWidget(self.setTempEdit, 1, 4, 1, 1)
        self.plus10Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.plus10Button.sizePolicy().hasHeightForWidth())
        self.plus10Button.setSizePolicy(sizePolicy)
        self.plus10Button.setMinimumSize(QtCore.QSize(40, 40))
        self.plus10Button.setAutoRepeat(True)
        self.plus10Button.setObjectName("plus10Button")
        self.gridLayout.addWidget(self.plus10Button, 1, 7, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 5, 1, 3)
        self.tempControlLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tempControlLabel.setFont(font)
        self.tempControlLabel.setObjectName("tempControlLabel")
        self.gridLayout.addWidget(self.tempControlLabel, 0, 1, 1, 4, QtCore.Qt.AlignHCenter)
        self.externalTempLabel2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.externalTempLabel2.setObjectName("externalTempLabel2")
        self.gridLayout.addWidget(self.externalTempLabel2, 1, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(200, 300, 238, 121))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.extractionPumpTimeEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.extractionPumpTimeEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.extractionPumpTimeEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.extractionPumpTimeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.extractionPumpTimeEdit.setReadOnly(True)
        self.extractionPumpTimeEdit.setObjectName("extractionPumpTimeEdit")
        self.gridLayout_3.addWidget(self.extractionPumpTimeEdit, 3, 1, 1, 1)
        self.heaterButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.heaterButton.setMinimumSize(QtCore.QSize(130, 0))
        self.heaterButton.setMaximumSize(QtCore.QSize(130, 16777215))
        self.heaterButton.setCheckable(True)
        self.heaterButton.setObjectName("heaterButton")
        self.gridLayout_3.addWidget(self.heaterButton, 1, 0, 1, 1)
        self.coolingPumpTimeEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.coolingPumpTimeEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.coolingPumpTimeEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.coolingPumpTimeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.coolingPumpTimeEdit.setReadOnly(True)
        self.coolingPumpTimeEdit.setObjectName("coolingPumpTimeEdit")
        self.gridLayout_3.addWidget(self.coolingPumpTimeEdit, 2, 1, 1, 1)
        self.electricalSystemsLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.electricalSystemsLabel.setFont(font)
        self.electricalSystemsLabel.setObjectName("electricalSystemsLabel")
        self.gridLayout_3.addWidget(self.electricalSystemsLabel, 0, 0, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.coolingPumpButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.coolingPumpButton.setMinimumSize(QtCore.QSize(130, 0))
        self.coolingPumpButton.setMaximumSize(QtCore.QSize(130, 16777215))
        self.coolingPumpButton.setCheckable(True)
        self.coolingPumpButton.setObjectName("coolingPumpButton")
        self.gridLayout_3.addWidget(self.coolingPumpButton, 2, 0, 1, 1)
        self.heaterTimeEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heaterTimeEdit.sizePolicy().hasHeightForWidth())
        self.heaterTimeEdit.setSizePolicy(sizePolicy)
        self.heaterTimeEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.heaterTimeEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.heaterTimeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.heaterTimeEdit.setReadOnly(True)
        self.heaterTimeEdit.setObjectName("heaterTimeEdit")
        self.gridLayout_3.addWidget(self.heaterTimeEdit, 1, 1, 1, 1)
        self.extractionPump = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.extractionPump.setMinimumSize(QtCore.QSize(130, 0))
        self.extractionPump.setMaximumSize(QtCore.QSize(130, 16777215))
        self.extractionPump.setCheckable(True)
        self.extractionPump.setObjectName("extractionPump")
        self.gridLayout_3.addWidget(self.extractionPump, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "Semi Auto Brew"))
        self.externalTempLabel.setText(_translate("MainWindow", "External Temperature:"))
        self.internalTempLabel.setText(_translate("MainWindow", "Internal Temperature:"))
        self.tempLabel.setText(_translate("MainWindow", "Temperatures"))
        self.minus1Button.setText(_translate("MainWindow", "-1"))
        self.minus10Button.setText(_translate("MainWindow", "-10"))
        self.plus5Button.setText(_translate("MainWindow", "+5"))
        self.minus5Button.setText(_translate("MainWindow", "-5"))
        self.plus1Button.setText(_translate("MainWindow", "+1"))
        self.plus10Button.setText(_translate("MainWindow", "+10"))
        self.tempControlLabel.setText(_translate("MainWindow", "Temperature Controls"))
        self.externalTempLabel2.setText(_translate("MainWindow", "External Temperature:"))
        self.heaterButton.setText(_translate("MainWindow", "Heater"))
        self.electricalSystemsLabel.setText(_translate("MainWindow", "Electrical Systems"))
        self.coolingPumpButton.setText(_translate("MainWindow", "Cooling Pump"))
        self.extractionPump.setText(_translate("MainWindow", "Extraction Pump"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SemiAutoBrewScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())