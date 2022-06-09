from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.Qt import *
import sys


class TransitionWindow(QMainWindow):
    def __init__(self):
        super(TransitionWindow, self).__init__()
        self.ui = uic.loadUi("forms/Transition.ui", self)
        self.setWindowTitle("Эм, а как назвать-то?")
        self.setWindowIcon(QIcon('res/logo.ico'))
        self.ui.btn_transit.clicked.connect(self.transit)
        self.ui.btn_exit.clicked.connect(self.exit)
        self.get_employee()

    def exit(self):
        self.ui = AuthorizationWindow(self)
        self.ui.show()

    def transit(self):
        self.ui = SellerWindow(self)
        self.ui.show()

    def get_employee(self):
        """
        Промежуточный вариант.
        Данные должны браться из БД.
        """
        self.label_name.setText('Валентин Стрыкало')
        self.label_role.setText('Продавец')
        self.pixmap = QPixmap('res/Федоров.jpeg')
        self.label_avatar.setPixmap(self.pixmap)


class AuthorizationWindow(QMainWindow):
    def __init__(self):
        super(AuthorizationWindow, self).__init__()
        self.ui = uic.loadUi("forms/Authorization.ui", self)


class SellerWindow(QMainWindow):
    def __init__(self):
        super(SellerWindow, self).__init__()
        self.ui = uic.loadUi("forms/Seller.ui", self)
        self.window().setWindowTitle("Продавец")
        self.setWindowIcon(QIcon('res/logo.ico'))
        self.ui.btn_to_order.clicked.connect(self.order)
        self.ui.btn_exit.clicked.connect(self.exit)
        self.get_employee()
        self.timer_bar()

    def exit(self):
        self.ui = AuthorizationWindow(self)
        self.ui.show()

    def order(self):
        self.ui = OrderWindow(self)
        self.ui.show()

    def get_employee(self):
        """
        Промежуточный вариант.
        Данные должны браться из БД.
        """
        self.label_name.setText('Валентин Стрыкало')
        self.label_role.setText('Продавец')

    def timer_bar(self):




"""
class Builder:
    def __init__(self):
        self.gui = None

    def create_gui(self):
        self.gui = TransitionWindow(self)
"""

"""
Пока главным окном формируется транзитное
"""
app = QApplication(sys.argv)
if __name__ == "__main__":
    mwin = SellerWindow()
    mwin.show()
    sys.exit(app.exec_())