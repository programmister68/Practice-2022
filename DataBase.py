import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='admin',
            database='database',
        )

    def getCLient(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM CLIENTS")
        clients = cursor.fetchall()
        for i in clients:
            print(i)
        return clients

    def getOrders(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM REQUESTS")
        requests = cursor.fetchall()
        for i in requests:
            print(i)
        return requests

    def getEmployee(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM EMPLOYEERS")
        employeers = cursor.fetchall()
        for i in employeers:
            print(i)
        return employeers

    def getService(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM SERVICES")
        services = cursor.fetchall()
        for i in services:
            print(i)
        return services

    def getHistory(self):
        cursor = self.connection.cursor()
        cursor.exectue("SELECT * FROM EntryHistory")
        history = cursor.fetchall()
        for i in history:
            print(i)
        return history

    def ClientImport(self, FIO, ID_client, Passport, Datebirth, Addres, Email, Password):
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO client "
            f"(`FIO`,`ID_client`,`Passport`,`Datebirth`,`Addres`,`Email`,`Password`) "
            f"VALUES ('{FIO}','{ID_client}', '{Passport}', '{Datebirth}', '{Addres}', '{Email}', '{Password}')")
        cursor.close()
        self.connection.commit()

    def EmployeeImport(self, ID_Employee, Post, FIO_Employee, Login_Employee, Password_Employee, Last_Login, Status_Login):
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO employee"
            f"(`ID_Employee`, `Post`, `FIO_Employee`, `Login_Employee`, `Password_Employee`, `Last_Login`, `Status_Login`) "
            f"VALUES ('{ID_Employee}', '{Post}', '{FIO_Employee}', '{Login_Employee}', '{Password_Employee}', '{Last_Login}', '{Status_Login}' )")
        cursor.close()
        self.connection.commit()

    def ServiceImport(self, ID_Services, Name_Services, Code_Services, Price_Hour):
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO service"
            f"(`ID_Services`, `Name_Services`, `Code_Services`, `Price_Hour`)"
            f"VALUES ('{ID_Services}', '{Name_Services}', '{Code_Services}', '{Price_Hour}')" )
        cursor.close()
        self.connection.commit()

    def OrdersImport(self, ID_Orders, Code_Orders, Date_Create, Time_Order, ID_Client, Services, Status, Rent_Time):
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO Orders"
            f"(`ID_Orders`, `Code_Orders`, `Date_Create`, `Time_Order`, `ID_Client`, `Services`, `Status`, `Rent_Time`)"
            f"VALUES ('{ID_Orders}', '{Code_Orders}', '{Date_Create}', '{Time_Order}', '{ID_Client}', '{Services}', '{Status}', '{Rent_Time}')"
        )
        cursor.close()
        self.connection.commit()


    def DeleteClient(self):
        cursor = self.connection.cursor()
        cursor.execute("DROP TABLE clients")
        cursor.close()
        self.connection.commit()

    def DeleteOrders(self):
        cursor = self.connection.cursor()
        cursor.execute("DROP TABLE requests")
        cursor.close()
        self.connection.commit()

    def DeleteService(self):
        cursor = self.connection.cursor()
        cursor.execute("DROP TABLE services")
        cursor.close()
        self.connection.commit()

    def DeleteEmployee(self):
        cursor = self.connection.cursor()
        cursor.execute("DROP TABLE employeers")
        cursor.close()
        self.connection.commit()

if __name__ == '__main__':
    D = Database()
    print("All client")
    print("___________________________________________________________________________________________________________")
    D.getCLient()
    print("---------------------------------------------------------------------------------")
    D.insertService("")
