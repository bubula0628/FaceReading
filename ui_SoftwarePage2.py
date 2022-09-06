from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SoftwarePage(object):
    def setupUi(self, SoftwarePage):
        SoftwarePage.setObjectName("SoftwarePage")
        SoftwarePage.resize(800, 600)
        self.layoutWidget = QtWidgets.QWidget(SoftwarePage)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 757, 348))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.gridLayout.setObjectName("gridLayout")

        self.LoadBtn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LoadBtn.setFont(font)
        self.LoadBtn.setObjectName("Load img")
        self.gridLayout.addWidget(self.LoadBtn, 4, 0, 1, 1)

        self.FnBtn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FnBtn.setFont(font)
        self.FnBtn.setObjectName("Fn img")
        self.gridLayout.addWidget(self.FnBtn, 4, 1, 1, 1)



        self.cameraButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cameraButton.setFont(font)
        self.cameraButton.setObjectName("WebCam")
        self.gridLayout.addWidget(self.cameraButton, 4, 2, 1, 1)
        
        self.SaveBtn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SaveBtn.setFont(font)
        self.SaveBtn.setObjectName("SaveBtn")
        self.gridLayout.addWidget(self.SaveBtn, 4, 3, 1, 1)
        

        self.cameraLabel = QtWidgets.QLabel(self.layoutWidget)
        self.cameraLabel.setMinimumSize(QtCore.QSize(480, 320))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cameraLabel.setFont(font)
        self.cameraLabel.setObjectName("cameraLabel")
        self.gridLayout.addWidget(self.cameraLabel, 0, 0, 4, 4)


        self.retranslateUi(SoftwarePage)
        QtCore.QMetaObject.connectSlotsByName(SoftwarePage)

    def retranslateUi(self, SoftwarePage):
        _translate = QtCore.QCoreApplication.translate
        SoftwarePage.setWindowTitle(_translate("SoftwarePage", "Face Reading"))
        self.LoadBtn.setText(_translate("SoftwarePage", "Load Image"))
        self.FnBtn.setText(_translate("SoftwarePage", "Function Image"))        
        self.cameraButton.setText(_translate("SoftwarePage", "WebCam"))
        self.SaveBtn.setText(_translate("SoftwarePage", "Save Img"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SoftwarePage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())