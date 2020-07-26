"""Signals and slots example."""

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
import functools

def greeting(person=False):
    print(type(person))
    """Slot function."""
    if msg.text():
        msg.setText("")
    elif (person == False):
        msg.setText("Hello World!")
    else:
        msg.setText(f"Hello {person}")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout()

btn1 = QPushButton('Greet')
btn1.clicked.connect(greeting)  # Connect clicked to greeting()
layout.addWidget(btn1)

btn2 = QPushButton("Personalized Greeting")
btn2.clicked.connect(functools.partial(greeting, "Christian!"))
layout.addWidget(btn2)

msg = QLabel('')
layout.addWidget(msg)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())