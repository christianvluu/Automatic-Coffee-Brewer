import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from functools import partial
from PyQt5.QtGui import *
from login_screen import *
from main_screen import *
from manual_brew_screen import *
from semi_auto__brew_screen import *

class BrewModel(object):
    def __init__(self):
        self.isHeating = False
        self.isPumping = False
        self.isConnectedArduino = False
        self.showingScreen = "login_screen"

        self.userName = None
        self.userPin = None
    
    def connectArduino(self):
        # do stuff here to connect to connect to Arduino
        # if success:
            # self.isConnectedArduino = True
        return True

class BrewController(object):
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self._view.screenSelector(self._model.showingScreen)
        self._connectButtons()
    
    def _connectButtons(self):
        if (self._model.showingScreen == "login_screen"):
            self._view.loginScreen.loginButton.clicked.connect(partial(self._changeScreen, "main_screen"))
        elif (self._model.showingScreen == "main_screen"):
            self._view.mainScreen.manualBrewButton.clicked.connect(partial(self._changeScreen, "manual_brew_screen"))
            self._view.mainScreen.profileBrewButton.clicked.connect(partial(self._changeScreen, "profile_brew_screen"))
            self._view.mainScreen.semiAutoBrewButton.clicked.connect(partial(self._changeScreen, "semi_auto_brew_screen"))
    
    def _changeScreen(self, screen): # calls function to do stuff appropriate to the button pressed
        if (screen == "main_screen" and self._model.showingScreen == "login_screen"):
            self._changeScreenFromLoginToMain()
        elif (screen == "manual_brew_screen" and self._model.showingScreen == "main_screen"):
            self._changeScreenFromMainToManualBrew()
        elif (screen == "profile_brew_screen" and self._model.showingScreen == "main_screen"):
            # do something
            pass
        elif (screen == "semi_auto_brew_screen" and self._model.showingScreen == "main_screen"):
            self._changeScreenFromMainToSemiAutoBrew()
            pass
        self._model.showingScreen = screen
        self._view.screenSelector(self._model.showingScreen)
        self.__init__(self._view, self._model) # reconnects buttons, reset controller, keeps model values
        print("user: ", self._model.userName)
        print("pin: ", self._model.userPin)
    
    def _changeScreenFromMainToSemiAutoBrew(self):
        return True
    
    def _changeScreenFromMainToManualBrew(self):
        return True

    def _changeScreenFromLoginToMain(self):
        self._model.userName = self._view.loginScreen.nameEdit.text()
        self._model.userPin = self._view.loginScreen.pinEdit.text()

class ManualBrewMode(object):
    # this obj gets called when manual brew screen is showing
    # it should store functions responsible for reacting to# the buttons
    # BUT the connecting signals to slots (butons to functions) should NOT be
    # here BUT be in the main controller class
    # general store all the necessary stuff to make the Controller class cleaner
    def __init__(self, controller):
        pass 

class BrewView(QMainWindow):
    windowXSize = 970
    windowYSize = 550
    def __init__(self):
        super().__init__()
        #self.setMinimumSize(BrewView.windowXSize, BrewView.windowYSize)
        self.setWindowTitle("Automatic Coffee Brewer")
        self.generalLayout = QGridLayout()
        self._centralWidget = QWidget()
        self._centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(self._centralWidget)

    
    def screenSelector(self, showingScreen):
        if (showingScreen == "login_screen"):
            self._showLoginScreen()
        elif (showingScreen == "main_screen"):
            self._showMainScreen()
        elif (showingScreen == "manual_brew_screen"):
            self._showManualBrewScreen()
        elif (showingScreen == "semi_auto_brew_screen"):
            self._showSemiAutoBrewScreen()

    def _showLoginScreen(self):
        self.loginScreen = LoginScreen()
        self.loginScreen.setupUi(view)

        
        # self.loginLabel = QLabel("Login to System")
        # self.generalLayout.addWidget(self.loginLabel, 0, 1, 1, 2, alignment=Qt.AlignCenter)

        # self.nameLabel = QLabel("Name:")
        # self.generalLayout.addWidget(self.nameLabel, 1, 0, alignment=Qt.AlignCenter)

        # self.nameInput = QLineEdit()
        # self.nameInput.setReadOnly(False)
        # self.nameInput.setAlignment(Qt.AlignLeft)
        # #self.nameInput.setFixedHeight(View.windowYSize/10)
        # self.generalLayout.addWidget(self.nameInput, 1, 1)

        # self.pinLabel = QLabel("Pin:")
        # self.generalLayout.addWidget(self.pinLabel, 1, 2, alignment=Qt.AlignCenter)

        # self.pinInput = QLineEdit()
        # self.pinInput.setReadOnly(False)
        # self.pinInput.setAlignment(Qt.AlignLeft)
        # #self.pinInput.setFixedHeight(View.windowYSize/10)
        # self.generalLayout.addWidget(self.pinInput, 1, 3)

        # self.loginButton = QPushButton(text = "Login")
        # self.generalLayout.addWidget(self.loginButton, 2, 3)

    def _showMainScreen(self):
        self.mainScreen = MainScreen()
        self.mainScreen.setupUi(view)
    
    def _showManualBrewScreen(self):
        self.manualBrewScreen = ManualBrewScreen()
        self.manualBrewScreen.setupUi(view)

    def _showSemiAutoBrewScreen(self):
        self.semiAutoBrewScreen = SemiAutoBrewScreen()
        self.semiAutoBrewScreen.setupUi(view)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = BrewView()
    view.show()
    model = BrewModel()
    controller = BrewController(view, model)
    #CalculatorControl(view = win, model = model)
    sys.exit(app.exec_())