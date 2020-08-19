import sys, time
from threading import Thread
from datetime import datetime as dt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from functools import partial
from PyQt5.QtGui import *
from login_screen import *
from main_screen import *
from manual_brew_screen import *
from semi_auto_brew_screen import *

class BrewModel(object):
    def __init__(self):
        self.isHeating = {"heat":False, "startTime":dt.now().replace(microsecond=0)}
        self.isExtractionPumping = {"pump":False, "startTime":dt.now().replace(microsecond=0)}
        self.isCoolingPumping = {"pump":False, "startTime":dt.now().replace(microsecond=0)}
        self.isConnectedArduino = False
        self.showingScreen = "login_screen"

        self.internalTemp = -1
        self.externalTemp = -1

        self.setExternalTemp = 20 # default value

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
            self._postChangeScreenFromMainToSemiAutoBrew()
            pass
    
    def _postChangeScreenFromMainToManualBrew(self):
        self._model.modeObject = ManualBrewMode(self, self._model, self._view)
    
    def _postChangeScreenFromMainToSemiAutoBrew(self):
        self._model.modeObject = SemiAutoBrewMode(self, self._model, self._view)

    def _preChangeScreenFromLoginToMain(self):
        self._model.userName = self._view.loginScreen.nameEdit.text()
        self._model.userPin = self._view.loginScreen.pinEdit.text()
    
    def stopAll(self):
        self._model.isHeating = {"heat":False, "startTime":dt.now().replace(microsecond=0)}
        self._model.isExtractionPumping = {"pump":False, "startTime":dt.now().replace(microsecond=0)}
        self._model.isCoolingPumping = {"pump":False, "startTime":dt.now().replace(microsecond=0)}
        self._model.setExternalTemp = 20

    def backToMain(self):
        self.stopAll()
        self._model.modeObject = None
        self._changeScreen("main_screen")

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
        self._updateDisplay()

    def _connectButtons(self):
        self._view.manualBrewScreen.heaterButton.clicked.connect(self._buttonTrigger)
        self._view.manualBrewScreen.extractionPumpButton.clicked.connect(self._buttonTrigger)
        self._view.manualBrewScreen.coolingPumpButton.clicked.connect(self._buttonTrigger)
        self._view.manualBrewScreen.backButton.clicked.connect(self._controller.backToMain)
    
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
    
    def _updateDisplay(self):
        self._view.manualBrewScreen.externalTempEdit.setText(str(self._model.externalTemp))
        self._view.manualBrewScreen.internalTempEdit.setText(str(self._model.internalTemp))

        self._view.manualBrewScreen.heaterTimeEdit.setText(str(dt.now().replace(microsecond=0) - self._model.isHeating["startTime"]))
        self._view.manualBrewScreen.coolingPumpTimeEdit.setText(str(dt.now().replace(microsecond=0) - self._model.isCoolingPumping["startTime"]))
        self._view.manualBrewScreen.extractionPumpTimeEdit.setText(str(dt.now().replace(microsecond=0) - self._model.isExtractionPumping["startTime"]))
    
    def run(self):
        self._updateDisplay()

class SemiAutoBrewMode(object):
    def __init__(self, cntrllr, mdl, vw):
        self._controller = cntrllr # weird spelling because matching name at the bottom
        self._model = mdl
        self._view = vw
        self._connectButtons()
        # self.updateDisplay()

        self.tempDelta = 4 # +/- 4 degrees before triggering on/off of heaterButton
        
    def _connectButtons(self):
        self._view.semiAutoBrewScreen.minus10Button.clicked.connect(partial(self._changeExternalTemp, -10))
        self._view.semiAutoBrewScreen.minus5Button.clicked.connect(partial(self._changeExternalTemp, -5))
        self._view.semiAutoBrewScreen.minus1Button.clicked.connect(partial(self._changeExternalTemp, -1))
        self._view.semiAutoBrewScreen.plus1Button.clicked.connect(partial(self._changeExternalTemp, +1))
        self._view.semiAutoBrewScreen.plus5Button.clicked.connect(partial(self._changeExternalTemp, +5))
        self._view.semiAutoBrewScreen.plus10Button.clicked.connect(partial(self._changeExternalTemp, +10))
        # don't include heater button
        self._view.semiAutoBrewScreen.heaterButton.setEnabled(False)
        self._view.semiAutoBrewScreen.extractionPumpButton.clicked.connect(self._buttonTrigger)
        self._view.semiAutoBrewScreen.coolingPumpButton.clicked.connect(self._buttonTrigger)

        self._view.semiAutoBrewScreen.backButton.clicked.connect(self._controller.backToMain)

    def _changeExternalTemp(self, deltaT):
        self._model.setExternalTemp += deltaT
    
    def _buttonTrigger(self): # this function checks the isChecked for the checkable buttons
        if (self._view.semiAutoBrewScreen.extractionPumpButton.isChecked() != self._model.isExtractionPumping["pump"]):
            self._model.isExtractionPumping["startTime"] = dt.now().replace(microsecond=0)
        if (self._view.semiAutoBrewScreen.coolingPumpButton.isChecked() != self._model.isCoolingPumping["pump"]):
            self._model.isCoolingPumping["startTime"] = dt.now().replace(microsecond=0)
        
        self._model.isExtractionPumping["pump"] = self._view.semiAutoBrewScreen.extractionPumpButton.isChecked()
        self._model.isCoolingPumping["pump"] = self._view.semiAutoBrewScreen.coolingPumpButton.isChecked()
    
    def _updateDisplay(self):
        self._view.semiAutoBrewScreen.coolingPumpTimeEdit.setText(str(dt.now().replace(microsecond=0) - self._model.isCoolingPumping["startTime"]))
        self._view.semiAutoBrewScreen.heaterTimeEdit.setText(str(dt.now().replace(microsecond=0) - self._model.isHeating["startTime"]))
        self._view.semiAutoBrewScreen.extractionPumpTimeEdit.setText(str(dt.now().replace(microsecond=0) - self._model.isExtractionPumping["startTime"]))

        self._view.semiAutoBrewScreen.externalTempEdit.setText(str(self._model.externalTemp))
        self._view.semiAutoBrewScreen.internalTempEdit.setText(str(self._model.internalTemp))
        
        self._view.semiAutoBrewScreen.setExternalTempEdit.setText(str(self._model.setExternalTemp))
    
    def _heaterControl(self):
        newHeatState = self._model.isHeating["heat"]
        if ((self._model.setExternalTemp - self.tempDelta) < self._model.externalTemp) and \
            ((self._model.setExternalTemp + self.tempDelta) > self._model.externalTemp):
            # within +/- tempDelta range
            newHeatState = True
        elif ((self._model.setExternalTemp - self.tempDelta) >= self._model.externalTemp):
            # below +/- tempDelta range
            newHeatState = False
        elif ((self._model.setExternalTemp + self.tempDelta) <= self._model.externalTemp):
            # above +/- tempDelta range
            newHeatState = False
        else:
            raise "set temp case not considered"

        if (newHeatState != self._model.isHeating["heat"]):
            self._model.isHeating["heat"] = newHeatState
            self._model.isHeating["startTime"] = dt.now().replace(microsecond=0)
        

    def run(self):
        self._updateDisplay()
        self._heaterControl()


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
        else:
            raise "ERROR, NO SCREEN FOUND"

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

def printAllInfo(mdl, vw, cntrllr): # debugger that prints all information
    while(True):
        #print(f"heat:{mdl.isHeating}, cool:{mdl.isCoolingPumping}, extract:{mdl.isExtractionPumping}")
        print(f"setExternalTemp:{mdl.setExternalTemp}", end=" ")
        heater = mdl.isHeating["heat"]
        cooling = mdl.isCoolingPumping["pump"]
        extraction = mdl.isExtractionPumping["pump"]
        print(f"heat:{heater} cooling:{cooling} extraction:{extraction}")
        time.sleep(1)

def mainThread(mdl, vw, cntrllr):
    # calls the looping function run in the current mode
    # looping function is responsible for updating display, starting/stopping heater depending on temp, etc.
    while(True):
        time.sleep(0.05)
        if (mdl.modeObject != None):
            mdl.modeObject.run()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = BrewView()
    view.show()
    model = BrewModel()
    controller = BrewController(view, model)
    debugger = Thread(target=printAllInfo, args=(model, view, controller))
    debugger.start()
    looping = Thread(target=mainThread, args=(model, view, controller))
    looping.start()
    sys.exit(app.exec_())