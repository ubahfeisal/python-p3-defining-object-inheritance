class Vehicle:
    def __init__(self, wheel_size, wheel_number): #initializing method
        self.wheel_number = wheel_number
        self.wheel_size = wheel_size
        
    def go(self): #instance method
        return "vrrrrrrrooom!"
    
    def fill_up_tank(self): #instance method
        return "filling up!"
    
toyota = Vehicle(20,10) #object Toyota
print(toyota.go())
print(toyota.fill_up_tank())