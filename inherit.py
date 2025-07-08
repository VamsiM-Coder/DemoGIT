class Vehicle1:
    def start(self):
        print("Vehicle 1 is started.")

class Vehicle2:
    def start(self):
        print("Vehicle 2 is started.")
        
class Vehicle3(Vehicle1, Vehicle2):
    def start(self):
        Vehicle2.start(self)

class Bike(Vehicle1):
    def start(self):
        super().start()
        print("Bike is Movingg..")        
        
    
obj1 = Vehicle3()
obj1.start() 
print("--------")
obj2 = Bike()
obj2.start()           