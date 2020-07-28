import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from functools import partial
from PyQt5.QtGui import *

# class MainApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Test Platform")
#         self.setMinimumSize(500, 500)
#         self.generalLayout = QVBoxLayout()
#         self._centralWidget = QWidget(self)
#         self._centralWidget.setLayout(self.generalLayout)
#         self.setCentralWidget(self._centralWidget) # self.setCentralWidget is a something called in the super() class

#         self.button1 = QPushButton("Button1")
#         self.button1.setCheckable(True)
#         self.button1.clicked.connect(self.doButton1Stuff)
#         print(self.button1.isChecked())
#         self.generalLayout.addWidget(self.button1)

#     def doButton1Stuff(self):
#         print(self.button1.isChecked())

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = MainApp()
#     win.show()
#     sys.exit(app.exec_())

class test1(object):
    def __init__(self):
        self.var1 = 123

class test2(object):
    def __init__(self, obj):
        self.obj = obj
    def change(self):
        self.obj.var1 = 321


a = test1()
print(a.var1)
b = test2(a)
b.change()
print(a.var1)
