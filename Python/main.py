import sys
from datetime import datetime as dt
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
        self.isHeating = {"heat":False, "startTime":dt.now()}
        self.isExtractionPumping = {"pump":False, "startTime":dt.now()}
        self.isCoolingPumping = {"pump":False, "startTime":dt.now()}
        self.isConnectedArduino = False
        self.showingScreen = "login_screen"

        self.internalTemp = -1
        self.externalTemp = -1

        self.userName = None
        self.userPin = None

        self.modeObject = None
    
    def connectArduino(self):
        # do stuff here to connect to connect to Arduino
        # if success:
            # self.isConnectedArduino = True
        return True

class BrewController(object):
    def __init__(self, vw, mdl):
        self._view = vw
        self._model = mdl
        self._view.screenSelector(self._model.showingScreen)
        self._connectButtons()
    
    def _connectButtons(self):
        if (self._model.showingScreen == "login_screen"):
            self._view.loginScreen.loginButton.clicked.connect(partial(self._changeScreen, "main_screen"))
        elif (self._model.showingScreen == "main_screen"):
            self._view.mainScreen.manualBrewButton.clicked.connect(partial(self._changeScreen, "manual_brew_screen"))
            self._view.mainScreen.profileBrewButton.clicked.connect(partial(self._changeScreen, "profile_brew_screen"))
            self._view.mainScreen.semiAutoBrewButton.clicked.connect(partial(self._changeScreen, "semi_auto_brew_screen"))
    
    def _changeScreen(self, newScreen): # calls function to do stuff appropriate to the button pressed
        oldScreen = self._model.showingScreen
        if (newScreen == "main_screen" and oldScreen == "login_screen"):
            self._preChangeScreenFromLoginToMain()
        elif (newScreen == "manual_brew_screen" and oldScreen == "main_screen"):
            #self._preChangeScreenFromMainToManualBrew()
            pass
        elif (newScreen == "profile_brew_screen" and oldScreen == "main_screen"):
            # do something
            pass
        elif (newScreen == "semi_auto_brew_screen" and oldScreen == "main_screen"):
            #self._preChangeScreenFromMainToSemiAutoBrew()
            pass
        
        self._model.showingScreen = newScreen
        self._view.screenSelector(self._model.showingScreen)
        self.__init__(self._view, self._model) # reconnects buttons, reset controller, keeps model values

        if (newScreen == "main_screen" and oldScreen == "login_screen"):
            #self._postChangeScreenFromLoginToMain()
            pass
        elif (newScreen == "manual_brew_screen" and oldScreen == "main_screen"):
            self._postChangeScreenFromMainToManualBrew()
            pass
        elif (newScreen == "profile_brew_screen" and oldScreen == "main_screen"):
            # do something
            pass
        elif (newScreen == "semi_auto_brew_screen" and oldScreen == "main_screen"):
            #self._postChangeScreenFromMainToSemiAutoBrew()
            pass
    
    def _postChangeScreenFromMainToManualBrew(self):
        self._model.modeObject = ManualBrewMode(self, self._model, self._view)
        print("DO STUFF")

    def _preChangeScreenFromLoginToMain(self):
        self._model.userName = self._view.loginScreen.nameEdit.text()
        self._model.userPin = self._view.loginScreen.pinEdit.text()

class ManualBrewMode(object):
    # this obj gets called when manual brew screen is showing
    # it should store functions responsible for reacting to# the buttons
    # BUT the connecting signals to slots (butons to functions) should NOT be
    # here BUT be in the main controller class
    # general store all the necessary stuff to make the Controller class cleaner
    def __init__(self, cntrllr, mdl, vw):
        self._controller = cntrllr # weird spelling because matching name at the bottom
        self._model = mdl
        self._view = vw
        self._connectButtons()
        self.updateDisplay()

    def _connectButtons(self):
        self._view.manualBrewScreen.heaterButton.clicked.connect(self._buttonTrigger)
        self._view.manualBrewScreen.extractionPumpButton.clicked.connect(self._buttonTrigger)
        self._view.manualBrewScreen.coolingPumpButton.clicked.connect(self._buttonTrigger)
    
    def _buttonTrigger(self): # this function checks the isChecked for the checkable buttons
        if (self._view.manualBrewScreen.heaterButton.isChecked() != self._model.isHeating["heat"]):
            self._model.isHeating["startTime"] = dt.now()
        if (self._view.manualBrewScreen.extractionPumpButton.isChecked() != self._model.isExtractionPumping["pump"]):
            self._model.isExtractionPumping["startTime"] = dt.now()
        if (self._view.manualBrewScreen.coolingPumpButton.isChecked() != self._model.isCoolingPumping["pump"]):
            self._model.isCoolingPumping["startTime"] = dt.now()
        
        self._model.isHeating["heat"] = self._view.manualBrewScreen.heaterButton.isChecked()
        self._model.isExtractionPumping["pump"] = self._view.manualBrewScreen.extractionPumpButton.isChecked()
        self._model.isCoolingPumping["pump"] = self._view.manualBrewScreen.coolingPumpButton.isChecked()
    
    def updateDisplay(self):
        self._view.manualBrewScreen.externalTempEdit.setText(str(self._model.externalTemp))
        self._view.manualBrewScreen.internalTempEdit.setText(str(self._model.internalTemp))

        self._view.manualBrewScreen.heaterTimeEdit.setText(str(dt.now() - self._model.isHeating["startTime"]))
        self._view.manualBrewScreen.coolingPumpTimeEdit.setText(str(dt.now() - self._model.isCoolingPumping["startTime"]))
        self._view.manualBrewScreen.extractionPumpTimeEdit.setText(str(dt.now() - self._model.isExtractionPumping["startTime"]))


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
    sys.exit(app.exec_())