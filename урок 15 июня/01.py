#Peson, Ticketr, Kassa, Train
from random import randint

class Person:
    balance = 0
    iin = ""
    birth_date = ""
    first_name = ""
    last_name = ""
    ticket = False

    def __init__(self, name, last_name, birth_date):
       self.first_name = name
       self.last_name = last_name
       self.birth_date = birth_date
       self.iin = randint(100000000000,999999999999)

    def show_info(self):
        info = f"""Человек: {self.first_name} {self.last_name}, 
        Дата Рождения: {self.birth_date},
        ИИН: {self.iin}, денег: {self.balance} """
        print(info)

    def earn(self, amount):
        self.balance += amount

    def spend(self, amount):
        if self.balance >= amount: 
          self.balance -= amount
          return amount
        return 0


class Ticket:
    number = 0
    train_id = 0
    source = ""
    destination = ""
    wagon = 0
    seat = 0
    datetime = ""
    passenger: Person = False

    def __init__(self, trainid, source, destination, datetime, person):
        self.train_id = trainid
        self.source = source
        self.destination = destination
        self.datetime = datetime
        self.passenger = person
        self.number = randint(100000, 999999)
        self.wagon = randint(1, 12)
        self.seat = randint(1, 32)

    def show(self):
        info = f""" Билет номер {self.number}:
        {self.source} - {self.destination}
        Отправление: {self.datetime}, вагон {self.wagon}, место {self.seat}
        Пассажир: {self.passenger.first_name} {self.passenger.last_name},
        ИИН: {self.passenger.iin}, {self.passenger.birth_date} г.р.
        """
        print(info)
    

class Kassa:
    kass_balance = 0
    def get_prcie(self, source, destination):
        price = (len(source) + len(destination)) * 1000
        return price

    def buy_ticket(self, passenger, source, destination, train):
        money = passenger.spend(self.get_prcie(source, destination))
        if money > 0:
            self.kass_balance += money
            ticket = Ticket(train.number, source,destination, train.datetime, passenger)
            passenger.ticket = ticket
            return True
        else:
            return False

class Train:
     source = ""
     destination = ""
     datetime = ""
     number = 0

     def __init__(self, source, destination, datetime):
        self.source = source
        self.destination = destination
        self.datetime = datetime
        self.number = randint(1,100)

     def go(self,passenger):
        if passenger.ticket:
            if passenger.ticket.train_id == self.number and self.datetime and passenger.ticket.datetime:
                print(f'вы поехали из {self.source} в {self.destination} \n Приехали')
            passenger.ticket = False





dude = Person("Ilon", "Kask", "1994-6-25")
dude.earn(25000)
dude.show_info() 

tmp_ticket = Ticket(23, "Алматы", "Пхеньян", "2023-106-16 07:59", dude)


kass = Kassa()


tmp_train = Train("Алматы", "Анталия", "2023-06-16 20:00")
kass.buy_ticket(dude,'Алматы',"Анталия", tmp_train)
dude.ticket.show()
tmp_train.go(dude)