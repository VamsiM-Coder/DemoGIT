class Vehicle1:
    def start(self):
        print("Vehicle 1 is started.")

class Vehicle2:
    def start(self):
        print("Vehicle 2 is started.")
        
class Vehicle3(Vehicle1, Vehicle2):
    def start(self):
        Vehicle2.start(self)
    
obj = Vehicle3()
obj.start()            