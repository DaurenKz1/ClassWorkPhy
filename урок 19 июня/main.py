from person import Person
from ticket import Ticket
from kassa import Kassa
from train import Train


dude = Person("Ilon", "Kask", "1994-06-25")
dude.earn(25000)
dude.pay(3500)
dude.show_info()

tmp_ticket = Ticket(23, "Алматы", "Ташкент", "2023-06-16 07:59", dude)

kassa = Kassa()


tmp_train = Train('Алматы', "Анталия", '2023-06-16 20:00')
kassa.buy_ticket(dude, 'Алматы', 'Анталия', tmp_train)
dude.ticket.show()
tmp_train.go(dude)


