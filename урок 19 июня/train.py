from random import randint
class Train:
    source = None
    destination = None
    datetime = None
    number = None

    def __init__(self, sourse, destination, datetime):
        self.source = sourse
        self.destination = destination
        self.datetime = datetime    
        self.number = randint(1, 100)

    def go(self, passenger):
        if passenger.ticket:
            if passenger.ticket.train_id == self.number and \
                passenger.ticket.datetime == self.datetime:
                    print(f'Вы поехали из {self.source} в {self.destination}\nПриехали')
                    passenger.ticket = False
            else:
                print("У Вас билет не на этот поезд")
        else:
            print("У Вас нет билета")
print("Train")