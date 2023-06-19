from random import randint
from datetime import date

class Person:
    balance = 0
    iin = 0
    birth_date = ""
    first_name = ""
    last_name = ""
    order = False

    def __init__(self, name, last_name, birth_date):
        self.first_name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.iin = randint(100000000000, 999999999999)

    def show_info(self):
        info = f"""Человек: {self.first_name} {self.last_name},
        Дата рождения: {self.birth_date},
        ИИН: {self.iin}, денег: {self.balance}"""
        print(info)

    def earn(self, amount):
        self.balance += amount

    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        return 0

class Order:
    hotel_name = ""
    id = 0
    room = 0
    date_from = 0
    date_to = 0
    visitor_name = ""
    visitor_iin = 0

    def __init__(self, hotel_name, rooom, date_from, date_to, visitor_name):
        self.hotel_name = hotel_name
        self.room = rooom
        self.date_from = date_from
        self.date_to = date_to
        self.visitor_name = visitor_name
        self.visitor_iin = randint((100000000000, 999999999999))

    def show_info(self):
        info = f"""Отель: {self.hotel_name},
        Номер комнаты: {self.room},
        Дата: {self.date_from} - {self.date_to}
        Имя гостя: {self.visitor_name}, ИИН гостя: {self.visitor_iin}"""
        print(info)

class Room:
    number = 0
    bedrooms = 0
    order: Order = False

    def __init__(self, number, bedrooms, order):
        self.number = number
        self.bedrooms = 2 if number == 0 else 1
        self.order = False

    def is_empty(self, date=None):
        if date is None:
            date = date.today()
        if self.order is None or date < self.order.date_from or date > self.order.date_to:
            return True

    def show_info(self):
        info = f"""Номер комнаты: {self.number}
        Кол-во спален: {self.bedrooms}
        Бронь: {'Нет' if self.order is None else 'Да'}
        """

class Hotel:
    name = ""
    balance = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_price(self, date_from,_date_to):
        price_per_day = 100
        days = (_date_to - date_from).days + 1
        result = price_per_day * days
        return result
