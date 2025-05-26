from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass #has no implementation
    
class car(Vehicle):
    def start(self):
        print("car engine starts")
        
class Bike(Vehicle):
    def start(self):
        print("bike engine starts") 
car1=car()      
bik1=Bike() 
car1.start()
bik1.start()