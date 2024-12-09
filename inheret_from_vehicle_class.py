# creating vahicle Class


class Vehicle:
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage 
    # geting speed of the vehicle
    def get_speed(self):
        print("The maximum speed is {}".format(self.max_speed))
    
    def get_mileage(self):
        print("this car give us {}".format(self.mileage))
        
    def get_name(self):
        print("The name is {}".format(self.name))        
    
# this class inherits all the methods from the Vehicle class     
class Bus(Vehicle):
    pass
        
   
def main():
    bus1 = Bus("BRT", 80, 23)
    #vehicle = Vehicle()
    
    bus1.get_name( )
    bus1.get_mileage()
    bus1.get_speed()
main()         
