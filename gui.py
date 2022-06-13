import sys
import logging
from random import randint

from PyQt5 import uic, QtWidgets
from PyQt5.Qt import *


logging.basicConfig(level=logging.INFO)
# logging.disable(logging.INFO)


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
        self.close()
        self.ui = AuthWindow()
        self.ui.show()

    def transit(self):
        self.ui.close()
        self.ui = SellerWindow()
        self.ui.show()

    def get_employee(self):
        self.label_name.setText('Смирнова Ульяна Гордеевна')
        self.label_role.setText('Продавец')
        self.pixmap = QPixmap('res/Смирнова.jpeg')
        self.label_avatar.setPixmap(self.pixmap)


class TransitionToSupervisorWindow(QMainWindow):
    def __init__(self):
        super(TransitionToSupervisorWindow, self).__init__()
        self.ui = uic.loadUi("forms/Transition.ui", self)
        self.setWindowTitle("Инфо")
        self.setWindowIcon(QIcon('res/logo.ico'))
        self.ui.btn_transit.clicked.connect(self.transit)
        self.ui.btn_exit.clicked.connect(self.exit)
        self.get_employee()

    def exit(self):
        self.close()
        self.ui = AuthWindow()
        self.ui.show()

    def transit(self):
        self.ui.close()
        self.ui = SupervisorWindow()
        self.ui.show()

    def get_employee(self):
        self.label_name.setText('Игнатов Кассиан Васильевич')
        self.label_role.setText('Старший смены')
        self.pixmap = QPixmap('res/Игнатов.jpg')
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
        self.close()
        self.ui = AuthWindow()
        self.ui.show()

    def transit(self):
        self.ui.close()
        self.ui = AdminWindow()
        self.ui.show()

    def get_employee(self):
        self.label_name.setText('Федоров Федор Федорович')
        self.label_role.setText('Администратор')
        self.pixmap = QPixmap('res/Федоров.jpeg')
        self.label_avatar.setPixmap(self.pixmap)


class AuthWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = uic.loadUi("forms/auth.ui", self)
        self.setWindowIcon(QIcon('res/logo.ico'))
        self.setWindowTitle('Авторизация')
        self.btn_pw.setIcon(QIcon('res/eye.png'))
        self.btn_pw.setIconSize(QSize(16, 16))
        self.btn_reroll.setIcon(QIcon('res/Change.ico'))
        self.btn_reroll.setIconSize(QSize(16, 16))
        self.ui.btn_pw.clicked.connect(self.echo)
        self.pixmap = QPixmap('res/logo.png')
        self.pic_lbl.setPixmap(self.pixmap)
        self.scene = QGraphicsScene(0, 0, 300, 40)
        self.ui.cap_viev.setScene(self.scene)
        self.ui.btn_pw.clicked.connect(self.vis_pas)

        self.ui.btn_ext.clicked.connect(self.exit)
        self.visible_captcha(False)
        self.ui.enter_btn.clicked.connect(self.enter)
        self.ui.enter_btn.clicked.connect(self.counter_test)

        self.count_try_entry = 0
        self.now_captcha = None

    def enter(self):
        if self.ui.linelgn.text() == '1':
            rand_num = randint(0, 2)
            if rand_num == 0:
                self.ui.close()
                self.ui = TransitionToAdminWindow()
                self.ui.show()
            elif rand_num == 1:
                self.ui.close()
                self.ui = TransitionToSellerWindow()
                self.ui.show()
            else:
                self.ui.close()
                self.ui = TransitionToSupervisorWindow()
                self.ui.show()

    def vis_pas(self):
        ed = self.ui.linePword
        if self.vis_pas:
            self.vis_pas = False
            ed.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.vis_pas = True
            ed.setEchoMode(QtWidgets.QLineEdit.Password)

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

    def exit(self):
        self.close()
        sys.exit(app.exec_())

    def echo(self):
        self.linePword.setEchoMode(QLineEdit.EchoMode.Normal)

    def visible_captcha(self, visible=True):
        self.ui.cap_viev.setVisible(visible)
        self.ui.cap_edit.setVisible(visible)
        self.ui.capt.setVisible(visible)
        self.ui.btn_reroll.setVisible(visible)
        self.scene.addText(f"CAPTCHA TEST")


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
        self.close()
        self.ui = AuthWindow()
        self.ui.show()

    def order(self):
        self.ui = OrderWindow()
        self.ui.show()

    def get_employee(self):
        self.label_name.setText('Смирнова Ульяна Гордеевна')
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
        self.close()
        self.ui = AuthWindow()
        self.ui.show()

    def order(self):
        self.ui = OrderWindow()
        self.ui.show()

    def acc_prod(self):
        self.ui = ProductWindow()
        self.ui.show()

    def get_employee(self):
        self.label_name.setText('Игнатов Кассиан Васильевич')
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
        self.close()
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
        self.label_name.setText('Федоров Федор Федорович')
        self.label_role.setText('Администратор')


class ProductWindow(QtWidgets.QWidget):
    def __init__(self):
        super(ProductWindow, self).__init__()
        self.ui = uic.loadUi("forms/ProductWindow.ui", self)
        self.window().setWindowTitle("Принять товар")
        self.btn_exit.clicked.connect(self.exit)
        self.setWindowIcon(QIcon('res/logo.ico'))

    def exit(self):
        self.ui.close()


class MaterialDataWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MaterialDataWindow, self).__init__()
        self.ui = uic.loadUi("forms/MaterialDataWindow.ui", self)
        self.window().setWindowTitle("Данные о расходных материалах")
        self.btn_exit.clicked.connect(self.exit)
        self.setWindowIcon(QIcon('res/logo.ico'))

    def exit(self):
        self.ui.close()


class ReportWindow(QtWidgets.QWidget):
    def __init__(self):
        super(ReportWindow, self).__init__()
        self.ui = uic.loadUi("forms/ReportWindow.ui", self)
        self.window().setWindowTitle("Сформировать отчёт")
        self.btn_exit.clicked.connect(self.exit)
        self.setWindowIcon(QIcon('res/logo.ico'))

    def exit(self):
        self.ui.close()


class EntranceHistoryWindow(QtWidgets.QWidget):
    def __init__(self):
        super(EntranceHistoryWindow, self).__init__()
        self.ui = uic.loadUi("forms/EntranceHistoryWindow.ui", self)
        self.window().setWindowTitle("История входов")
        self.btn_exit.clicked.connect(self.exit)
        self.setWindowIcon(QIcon('res/logo.ico'))

    def exit(self):
        self.ui.close()


class OrderWindow(QtWidgets.QWidget):
    def __init__(self):
        super(OrderWindow, self).__init__()
        self.ui = uic.loadUi("forms/OrderWindow.ui", self)
        self.window().setWindowTitle("Сформировать заказ")
        self.btn_exit.clicked.connect(self.exit)
        self.setWindowIcon(QIcon('res/logo.ico'))

    def exit(self):
        self.ui.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    sys.exit(app.exec_())
