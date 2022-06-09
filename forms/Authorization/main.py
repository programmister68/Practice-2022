from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QGraphicsWidget, QLineEdit
from PyQt5 import uic
from PyQt5.QtCore import *
import logging
import sys
logging.basicConfig(level=logging.INFO)
# logging.disable(logging.INFO)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("res/forms/auth.ui", self)
        self.setWindowIcon(QIcon('res/logo.ico'))
        self.setWindowTitle('Авторизация')
        self.btn_pw.setIcon(QIcon('res/closed.png'))
        self.btn_pw.setIconSize(QSize(16, 16))
        self.btn_reroll.setIcon(QIcon('res/Change.ico'))
        self.btn_reroll.setIconSize(QSize(16, 16))
        self.ui.btn_pw.clicked.connect(self.echo)
        self.ui.btn_pw.clicked.connect(self.open_eye)
        self.pixmap = QPixmap('res/logo.png')
        self.pic_lbl.setPixmap(self.pixmap)

    def echo(self):
        self.linePword.setEchoMode(QLineEdit.EchoMode.Normal)

    def open_eye(self):
        self.btn_pw.setIcon(QIcon('res/eye.png'))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()