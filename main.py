import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

from lib.machine import get_temp
from ui.ui_main import Ui_MainWindow


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer_100 = QTimer(self)
        self.setup()

    def setup(self):
        self.timer_100.timeout.connect(self.set_temp)
        self.timer_100.start(100)

    def set_temp(self):
        temp = get_temp()
        self.ui.tempBar.setValue(temp)
        self.ui.tempLabel.setText(f"{temp} ℃")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    m_app = App()
    m_app.show()
    sys.exit(app.exec_())
