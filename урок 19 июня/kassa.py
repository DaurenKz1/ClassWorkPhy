from ticket import Ticket
class Kassa:
    balance = 0


    def get_price(self, source, destination):
        price = (len(source) + len(destination))*1000
        return price

    def buy_ticket(self, passenger, source, destination, train):
        money = passenger.pay(self.get_price(source, destination))
        if money > 0:
            self.balance += money
            ticket = Ticket(train.number, source, destination, train.datetime, passenger)
            passenger.ticket = ticket
            return True
        else:
            return False
print("Kassa")
