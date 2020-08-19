# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# from functools import partial
# from PyQt5.QtGui import *

# # class MainApp(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #         self.setWindowTitle("Test Platform")
# #         self.setMinimumSize(500, 500)
# #         self.generalLayout = QVBoxLayout()
# #         self._centralWidget = QWidget(self)
# #         self._centralWidget.setLayout(self.generalLayout)
# #         self.setCentralWidget(self._centralWidget) # self.setCentralWidget is a something called in the super() class

# #         self.button1 = QPushButton("Button1")
# #         self.button1.setCheckable(True)
# #         self.button1.clicked.connect(self.doButton1Stuff)
# #         print(self.button1.isChecked())
# #         self.generalLayout.addWidget(self.button1)

# #     def doButton1Stuff(self):
# #         self.button1.setChecked(True)
# #         print(self.button1.isChecked())

# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     win = MainApp()
# #     win.show()
# #     sys.exit(app.exec_())

# # class test1(object):
# #     def __init__(self):
# #         self.var1 = 123

# # class test2(object):
# #     def __init__(self, obj):
# #         self.obj = obj
# #     def change(self):
# #         self.obj.var1 = 321


# # a = test1()
# # print(a.var1)
# # b = test2(a)
# # b.change()
# # print(a.var1)

# # FROM: https://gist.github.com/arunreddy/ee01b4ccdd1f2e5773cdd5352783d9c6
# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.Qt import Qt
# from PyQt5.QtWidgets import *


# class VKQLineEdit(QLineEdit):
#     def __init__(self, parent=None, name=None, mainWindowObj=None):
#         super(VKQLineEdit, self).__init__(parent)
#         self.name = name
#         self.setFixedHeight(40)
#         self.mainWindowObj = mainWindowObj
#         self.setFocusPolicy(Qt.ClickFocus)

#     def focusInEvent(self, e):
#         self.mainWindowObj.keyboardWidget.currentTextBox = self
#         self.mainWindowObj.keyboardWidget.show()

#         # self.setStyleSheet("border: 1px solid red;")
#         super(VKQLineEdit, self).focusInEvent(e)

#     def mousePressEvent(self, e):
#         # print(e)
#         # self.setFocusPolicy(Qt.ClickFocus)
#         super(VKQLineEdit, self).mousePressEvent(e)
        



# class KeyboardWidget(QWidget):
#     def __init__(self, parent=None):
#         super(KeyboardWidget, self).__init__(parent)
#         self.currentTextBox = None

#         self.signalMapper = QSignalMapper(self)
#         self.signalMapper.mapped[int].connect(self.buttonClicked)

#         self.initUI()

#     def initUI(self):
#         layout = QGridLayout()

#         # p = self.palette()
#         # p.setColor(self.backgroundRole(),Qt.white)
#         # self.setPalette(p)
#         self.setAutoFillBackground(True)
#         self.text_box = QTextEdit()
#         self.text_box.setFont(QFont('Arial', 12))
#         # text_box.setFixedHeight(50)
#         # self.text_box.setFixedWidth(300)
#         layout.addWidget(self.text_box, 0, 0, 1, 13)

#         names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
#                  '1', '2', '3', '4', '5', '5', '7', '8', '9', '0', '.', '(', ')']

#         positions = [(i + 1, j) for i in range(3) for j in range(13)]

#         for position, name in zip(positions, names):

#             if name == '':
#                 continue
#             button = QPushButton(name)
#             button.setFont(QFont('Arial', 12))
#             button.setFixedHeight(25)
#             button.setFixedWidth(25)

#             button.KEY_CHAR = ord(name)
#             button.clicked.connect(self.signalMapper.map)
#             self.signalMapper.setMapping(button, button.KEY_CHAR)
#             layout.addWidget(button, *position)

#         # Cancel button
#         cancel_button = QPushButton('Cancel')
#         cancel_button.setFixedHeight(25)
#         cancel_button.setFont(QFont('Arial', 12))
#         cancel_button.KEY_CHAR = Qt.Key_Cancel
#         layout.addWidget(cancel_button, 5, 0, 1, 2)
#         cancel_button.clicked.connect(self.signalMapper.map)
#         self.signalMapper.setMapping(cancel_button, cancel_button.KEY_CHAR)
#         cancel_button.setFixedWidth(60)

#         # Cancel button
#         clear_button = QPushButton('Clear')
#         clear_button.setFixedHeight(25)
#         clear_button.setFont(QFont('Arial', 12))
#         clear_button.KEY_CHAR = Qt.Key_Clear
#         layout.addWidget(clear_button, 5, 2, 1, 2)
#         clear_button.clicked.connect(self.signalMapper.map)
#         self.signalMapper.setMapping(clear_button, clear_button.KEY_CHAR)
#         clear_button.setFixedWidth(60)

#         # Space button
#         space_button = QPushButton('Space')
#         space_button.setFixedHeight(25)
#         space_button.setFont(QFont('Arial', 12))
#         space_button.KEY_CHAR = Qt.Key_Space
#         layout.addWidget(space_button, 5, 4, 1, 3)
#         space_button.clicked.connect(self.signalMapper.map)
#         self.signalMapper.setMapping(space_button, space_button.KEY_CHAR)
#         space_button.setFixedWidth(85)


#         # Back button
#         back_button = QPushButton('Back')
#         back_button.setFixedHeight(25)
#         back_button.setFont(QFont('Arial', 12))
#         back_button.KEY_CHAR = Qt.Key_Backspace
#         layout.addWidget(back_button, 5, 7, 1, 2)
#         back_button.clicked.connect(self.signalMapper.map)
#         self.signalMapper.setMapping(back_button, back_button.KEY_CHAR)
#         back_button.setFixedWidth(60)



#         # Enter button
#         enter_button = QPushButton('Enter')
#         enter_button.setFixedHeight(25)
#         enter_button.setFont(QFont('Arial', 12))
#         enter_button.KEY_CHAR = Qt.Key_Enter
#         layout.addWidget(enter_button, 5, 9, 1, 2)
#         enter_button.clicked.connect(self.signalMapper.map)
#         self.signalMapper.setMapping(enter_button, enter_button.KEY_CHAR)
#         enter_button.setFixedWidth(60)

#         # Done button
#         done_button = QPushButton('Done')
#         done_button.setFixedHeight(25)
#         done_button.setFont(QFont('Arial', 12))
#         done_button.KEY_CHAR = Qt.Key_Home
#         layout.addWidget(done_button, 5, 11, 1, 2)
#         done_button.clicked.connect(self.signalMapper.map)
#         self.signalMapper.setMapping(done_button, done_button.KEY_CHAR)
#         done_button.setFixedWidth(60)

#         self.setGeometry(0, 0, 480, 300)
#         self.setLayout(layout)

#     def buttonClicked(self, char_ord):

#         txt = self.text_box.toPlainText()

#         if char_ord == Qt.Key_Backspace:
#             txt = txt[:-1]
#         elif char_ord == Qt.Key_Enter:
#             txt += chr(10)
#         elif char_ord == Qt.Key_Home:
#             self.currentTextBox.setText(txt)
#             self.text_box.setText("")
#             self.hide()
#             return
#         elif char_ord == Qt.Key_Clear:
#             txt = ""
#         elif char_ord == Qt.Key_Space:
#             txt += ' '
#         else:
#             txt += chr(char_ord)

#         self.text_box.setText(txt)


# class KeyboardUI(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         first_name = VKQLineEdit(name='First Name', mainWindowObj=self)
#         last_name = VKQLineEdit(name='Last Name', mainWindowObj=self)

#         mainWidget = QWidget()
#         layout = QGridLayout()
#         layout.addWidget(first_name, 0, 0)
#         layout.addWidget(last_name, 1, 0)

#         self.keyboardWidget = KeyboardWidget()
#         layout.addWidget(self.keyboardWidget, 0, 0, 10, 10)
#         mainWidget.setLayout(layout)

#         self.keyboardWidget.hide()

#         self.setCentralWidget(mainWidget)

#         self.statusBar().showMessage('Ready')

#         self.setGeometry(0, 0, 480, 320)
#         self.setWindowTitle('StethoX v1.0')
#         self.show()


# if __name__ == '__main__':
#     app = QApplication([])
#     ex = KeyboardUI()
#     ex.show()
#     sys.exit(app.exec_())

from datetime import datetime as dt

time = dt.now()
input()
print(str(dt.now().replace(microsecond=0)))

# import sys
# import random
# import matplotlib
# matplotlib.use('Qt5Agg')

# from PyQt5 import QtCore, QtWidgets

# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure


# class MplCanvas(FigureCanvas):

#     def __init__(self, parent=None, width=5, height=4, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         super(MplCanvas, self).__init__(fig)


# class MainWindow(QtWidgets.QMainWindow):

#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)

#         self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
#         self.setCentralWidget(self.canvas)

#         n_data = 50
#         self.xdata = list(range(n_data))
#         self.ydata = [random.randint(0, 10) for i in range(n_data)]
#         self.update_plot()

#         self.show()

#         # Setup a timer to trigger the redraw by calling update_plot.
#         self.timer = QtCore.QTimer()
#         self.timer.setInterval(100)
#         self.timer.timeout.connect(self.update_plot)
#         self.timer.start()

#     def update_plot(self):
#         # Drop off the first y element, append a new one.
#         self.ydata = self.ydata[1:] + [random.randint(0, 10)]
#         self.canvas.axes.cla()  # Clear the canvas.
#         self.canvas.axes.plot(self.xdata, self.ydata, 'r')
#         # Trigger the canvas to update and redraw.
#         self.canvas.draw()


# app = QtWidgets.QApplication(sys.argv)
# w = MainWindow()
# app.exec_()