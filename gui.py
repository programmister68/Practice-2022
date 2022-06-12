from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.Qt import *
import sys
from DataBase import Database


class TransitionToSellerWindow(QMainWindow):
    def __init__(self):
        super(TransitionToSellerWindow, self).__init__()
        self.ui = uic.loadUi("forms/Transition.ui", self)
        self.setWindowTitle("Инфо")
        self.setWindowIcon(QIcon('res/logo.ico'))
        self.ui.btn_transit.clicked.connect(self.transit)
        self.ui.btn_exit.clicked.connect(self.exit)
        self.get_employee()

    def exit(self):
        self.ui.close()
        self.ui = AuthWindow()
        self.ui.show()

    def transit(self):
        self.ui.close()
        self.ui = SellerWindow()
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


class TransitionToSupervisiorWindow(QMainWindow):
    def __init__(self):
        super(TransitionToSupervisiorWindow, self).__init__()
        self.ui = uic.loadUi("forms/Transition.ui", self)
        self.setWindowTitle("Инфо")
        self.setWindowIcon(QIcon('res/logo.ico'))
        self.ui.btn_transit.clicked.connect(self.transit)
        self.ui.btn_exit.clicked.connect(self.exit)
        self.get_employee()

    def exit(self):
        self.ui.close()
        self.ui = AuthWindow()
        self.ui.show()

    def transit(self):
        self.ui.close()
        self.ui = SupervisorWindow()
        self.ui.show()

    def get_employee(self):
        """
        Промежуточный вариант.
        Данные должны браться из БД.
        """
        self.label_name.setText('Валентин Стрыкало')
        self.label_role.setText('Старший смены')
        self.pixmap = QPixmap('res/Федоров.jpeg')
        self.label_avatar.setPixmap(self.pixmap)


class TransitionToAdminWindow(QMainWindow):
    def __init__(self):
        super(TransitionToAdminWindow, self).__init__()
        self.ui = uic.loadUi("forms/Transition.ui", self)
        self.setWindowTitle("Инфо")
        self.setWindowIcon(QIcon('res/logo.ico'))
        self.ui.btn_transit.clicked.connect(self.transit)
        self.ui.btn_exit.clicked.connect(self.exit)
        self.get_employee()

    def exit(self):
        self.ui.close()
        self.ui = AuthWindow()
        self.ui.show()

    def transit(self):
        self.ui.close()
        self.ui = AdminWindow()
        self.ui.show()

    def get_employee(self):
        """
        Промежуточный вариант.
        Данные должны браться из БД.
        """
        self.label_name.setText('Валентин Стрыкало')
        self.label_role.setText('Администратор')
        self.pixmap = QPixmap('res/Федоров.jpeg')
        self.label_avatar.setPixmap(self.pixmap)


class AuthWindow(QMainWindow):
    def __init__(self):
        super(AuthWindow, self).__init__()
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

    def exit(self):
        self.ui.close()
        self.ui = AuthWindow()
        self.ui.show()

    def order(self):
        self.ui = OrderWindow()
        self.ui.show()

    def get_employee(self):
        """
        Промежуточный вариант.
        Данные должны браться из БД.
        """
        self.label_name.setText('Валентин Стрыкало')
        self.label_role.setText('Продавец')


class SupervisorWindow(QMainWindow):
    def __init__(self):
        super(SupervisorWindow, self).__init__()
        self.ui = uic.loadUi("forms/Supervisor.ui", self)
        self.window().setWindowTitle("Старший смены")
        self.setWindowIcon(QIcon('res/logo.ico'))
        self.ui.btn_to_order.clicked.connect(self.order)
        self.ui.btn_exit.clicked.connect(self.exit)
        self.ui.btn_acc_prod.clicked.connect(self.acc_prod)
        self.get_employee()

    def exit(self):
        self.ui.close()
        self.ui = AuthWindow()
        self.ui.show()

    def order(self):
        self.ui = OrderWindow()
        self.ui.show()

    def acc_prod(self):
        self.ui = ProductWindow()
        self.ui.show()

    def get_employee(self):
        """
        Промежуточный вариант.
        Данные должны браться из БД.
        """
        self.label_name.setText('Валентин Стрыкало')
        self.label_role.setText('Старший смены')


class AdminWindow(QMainWindow):
    def __init__(self):
        super(AdminWindow, self).__init__()
        self.ui = uic.loadUi("forms/Admin.ui", self)
        self.window().setWindowTitle("Администратор")
        self.setWindowIcon(QIcon('res/logo.ico'))
        self.ui.btn_mat_data.clicked.connect(self.mat_data)
        self.ui.btn_exit.clicked.connect(self.exit)
        self.ui.btn_history.clicked.connect(self.history)
        self.ui.btn_report.clicked.connect(self.report_order)
        self.get_employee()

    def exit(self):
        self.ui.close()
        self.ui = AuthWindow()
        self.ui.show()

    def mat_data(self):
        self.ui = MaterialDataWindow()
        self.ui.show()

    def history(self):
        self.ui = EntranceHistoryWindow()
        self.ui.show()

    def report_order(self):
        self.ui = ReportWindow()
        self.ui.show()

    def get_employee(self):
        """
        Промежуточный вариант.
        Данные должны браться из БД.
        """
        self.label_name.setText('Валентин Стрыкало')
        self.label_role.setText('Администратор')


class ProductWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        pass


class MaterialDataWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        pass


class ReportWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        pass


class EntranceHistoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        pass


class OrderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        pass


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
    mwin = TransitionWindow()
    mwin.show()
    sys.exit(app.exec_())
