import logging
import sys
from random import *
from string import ascii_letters

from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import QSize
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QGraphicsScene, QHBoxLayout

logging.basicConfig(level=logging.INFO)
# logging.disable(logging.INFO)

class AuthWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
        self.scene = QGraphicsScene(0, 0, 300, 40)
        self.ui.cap_viev.setScene(self.scene)

        self.ui.btn_ext.clicked.connect(self.Exit)
        self.visible_captcha(False)
        self.ui.enter_btn.clicked.connect(self.counter_test)

        self.count_try_entry = 0
        self.now_captcha = None


    # def captcha_generation(self):
    #     self.scene.clear()
    #     symb = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    #     count_syms = 3
    #     now_syms = [''] * count_syms
    #     x, y = 30, 20
    #
    #     for i in range(count_syms):
    #         now_syms[i] = symb[random.randint(0, 30)]
    #         x += 20
    #         text = self.scene.addText(f"{now_syms[i]}")
    #         text.setFont(QFont("MS Shell Dlg 2", 15))
    #         text.moveBy(x, y + random.randint(-10, 20))
    #     self.now_captcha = ''.join(now_syms)

    def counter_test(self):
        self.count_try_entry +=1

        if self.count_try_entry == 2:
            self.visible_captcha(True)


    def auth(self):
        self.counter += 1
        if self.counter == 3:
            self.ui.cap_view.addWidget(self.captha_line)
            self.ui.cap_view.addWidget(self.captha_widget)
        elif self.counter < 3:
            self.ui.captha_layout = QHBoxLayout()
        elif self.counter > 8:
            self.ui.captha_layout.deleteLater()

    def Exit(self):
        self.close()
        sys.exit(app.exec_())

    def echo(self):
        self.linePword.setEchoMode(QLineEdit.EchoMode.Normal)

    def open_eye(self):
        self.btn_pw.setIcon(QIcon('res/eye.png'))

    def visible_captcha(self, visible=True):
        self.ui.cap_viev.setVisible(visible)
        self.ui.cap_edit.setVisible(visible)
        self.ui.capt.setVisible(visible)
        self.ui.btn_reroll.setVisible(visible)
        self.scene.addText(f"CAPTCHA TEST")
# class CapthaController:
#     def __init__(self):
#         self.update()
#
#     def update(self):
#         s = [i for i in ascii_letters]
#         shuffle(s)
#         digits = [str(i) for i in range(10)]
#         shuffle(digits)
#         self.generator = s[:4] + digits[:2]
#         shuffle(self.generator)
#
#     def get_value(self):
#         return self.generator
#
#     def check_captcha(self, s):
#         for i, ch in enumerate(s):
#             try:
#                 if self.generator[i] != s:
#                     return False
#             except IndexError:
#                 return False
#         return True

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    app.exec_()
