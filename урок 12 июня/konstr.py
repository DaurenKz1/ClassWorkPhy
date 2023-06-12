class Kettle():
    material = ""
    color = ""
    volume = 2.4
    water = 0

    def __init__(self, material, color="red", volume = 1,water = 0):
        self.material = material
        self.color = color
        self.volume = volume
        self.water = water

        
    
    def fill(self, liters=None):
        if liters is None:
            self.water = self.volume
        elif self.water + liters > self.volume:
            extra_water = self.water + liters - self.volume
            print(f"Вылилось {extra_water} ")
            self.water = self.volume
        else:
            self.water += liters
        print("Теперь в чайнике: ",self.water,"л")   


    def pour_out(self, liters=None):
        if liters is None:
            self.water = 0
        elif liters > self.water:
            extra_water = liters - self.water
            print(f"Лишнее {extra_water} ")
            self.water = 0
        else:
            self.water -= liters
        print("Теперь в чайнике: ",self.water,"л") 
    
my_kettle = Kettle("steel", "red", 2.4,2.4)
#other_kettle = Kettle("wood","gray",18)
#print(my_kettle.material)
#my_kettle.fill(0.7)
#my_kettle.fill(0.7)
#my_kettle.fill(0.7)
#my_kettle.fill(0.7)

my_kettle.pour_out(0.7)
my_kettle.pour_out(0.7)
my_kettle.pour_out(0.7)
my_kettle.pour_out(0.7)