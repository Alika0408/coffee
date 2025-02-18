import sys
import sqlite3
from PyQt6 import QtWidgets, uic


class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(CoffeeApp, self).__init__()
        uic.loadUi('main.ui', self)
        self.load_coffee_data()
        self.refreshButton.clicked.connect(self.load_coffee_data)

    def load_coffee_data(self):
        self.coffeeTable.setRowCount(0)

        # Подключение к базе данных
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()

        # Получение данных о кофе
        cursor.execute("SELECT * FROM coffee")
        coffee_data = cursor.fetchall()

        # Закрытие соединения
        conn.close()

        # Отображение данных в интерфейсе
        for coffee in coffee_data:
            self.display_coffee(coffee)

    def display_coffee(self, coffee):
        row_position = self.coffeeTable.rowCount()
        self.coffeeTable.insertRow(row_position)

        # Заполняем ячейки данными о кофе
        self.coffeeTable.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(coffee[0])))  # ID
        self.coffeeTable.setItem(row_position, 1, QtWidgets.QTableWidgetItem(coffee[1]))  # Название сорта
        self.coffeeTable.setItem(row_position, 2, QtWidgets.QTableWidgetItem(coffee[2]))  # Степень обжарки
        self.coffeeTable.setItem(row_position, 3, QtWidgets.QTableWidgetItem(coffee[3]))  # Молотый/в зернах
        self.coffeeTable.setItem(row_position, 4, QtWidgets.QTableWidgetItem(coffee[4]))  # Описание вкуса
        self.coffeeTable.setItem(row_position, 5, QtWidgets.QTableWidgetItem(f"{coffee[5]:.2f}"))  # Цена
        self.coffeeTable.setItem(row_position, 6, QtWidgets.QTableWidgetItem(coffee[6]))  # Объем упаковки


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
