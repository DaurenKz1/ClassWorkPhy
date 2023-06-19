from random import randint
class Train:
    source = None
    destination = None
    datetime = None
    number = None

    def __init__(self, kassa, sourse, destination, datetime):
        self.source = sourse
        self.destination = destination
        self.datetime = datetime    
        self.number = randint(1, 100)
        self.kassa = kassa

    def go(self, passenger):
        ticket = self.kassa.get_ticket(passenger, self.number, self.datetime)
        if ticket:
            if ticket.train_id == self.number and ticket.datetime == self.datetime:
                 print(f'Вы поехали из {self.source} в {self.destination}\nПриехали')
                 self.kassa.delete_ticket(ticket)
            else:
                print("У Вас билет не на этот поезд")
print("Train")
