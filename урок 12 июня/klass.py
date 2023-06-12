
class Kettle():
    material = "steel"
    color = "red"
    volume = 2.4
    water = 0

    def fill(self, liters):
        self.water += liters
        print("Теперь в чайнике: ",self.water,"л")
my_kettle = Kettle()
my_kettle.fill(2)
print(my_kettle.water)












