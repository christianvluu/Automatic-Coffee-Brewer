import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from functools import partial
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

class Calculator(QMainWindow): # main calculator class
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic Calculator")
        self.setFixedSize(235, 235)

        # set layout + central widget
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget = self.centralWidget

        # create and display buttons
        self._createDisplay() # displays the math expression at the top
        self._createButtons()
    
    def _createDisplay(self): # math expression at top
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)

        self.generalLayout.addWidget(self.display) # adds display widget to the main layout (QVBoxLayout)
        
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())
