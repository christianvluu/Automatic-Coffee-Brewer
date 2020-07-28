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
import PyQt5

class Calculator(QMainWindow): # main calculator class
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic Calculator")
        self.setFixedSize(500, 500)

        # set layout + central widget
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self._centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(self._centralWidget) # self.setCentralWidget is a something called in the super() class

        # create and display buttons
        self._createDisplay() # displays the math expression at the top
        self._createButtons()
    
    def _createDisplay(self): # math expression at top
        self.display = QLineEdit()
        self.display.setFixedHeight(75)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)

        self.generalLayout.addWidget(self.display) # adds display widget to the main layout (QVBoxLayout)
    
    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {'7': (0, 0), # this is in the form of Number : (x, y)
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4)}
        for text, pos in buttons.items():
            print (text, pos)
            self.buttons[text] = QPushButton(text)
            self.buttons[text].setFixedSize(80, 80)
            buttonsLayout.addWidget(self.buttons[text], pos[0], pos[1])
        self.generalLayout.addLayout(buttonsLayout)
    
    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()
    
    def getDisplayText(self):
        return self.display.text()
    
    def clearDisplay(self):
        self.display.setText("")

class CalculatorControl:
    def __init__(self, view, model):
        self._view = view
        self._connectSignals()
        self._model = model
    
    def _connectSignals(self): # connect signals and slots
        for text, btn in self._view.buttons.items():
            if text not in ["=", "C"]:
                btn.clicked.connect(partial(self._buildExpression, text))
        self._view.buttons["C"].clicked.connect(self._view.clearDisplay)
        self._view.buttons["="].clicked.connect(self._calculateResult)
    
    def _buildExpression(self, text):
        expression = self._view.getDisplayText() + text # combines current display with the new input
        self._view.setDisplayText(expression)
    
    def _calculateResult(self):
        result = self._model.evaluateExpression(self._view.getDisplayText())
        self._view.setDisplayText(result)

class CalculatorModel:
    def __init__(self):
        a = "a"
    
    def evaluateExpression(self, expression):
        try:
            result = str(eval(expression, {}, {}))
        except Exception:
            result = "ERROR"
        
        return result

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    model = CalculatorModel()
    CalculatorControl(view = win, model = model)
    sys.exit(app.exec_())
