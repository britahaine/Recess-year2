class Bird:
    def fly(self):
        print("bird flies in the sky")
        
class Eagle(Bird):
    def fly(self):
        print("eagle flies at high altitude")   
        
class Sparrow(Bird):
    def fly(self):
        print("sparrow flies at a low altitude")  
        #how polymophsm works
def flight_test(bird):
    bird.fly() 
eagle1=Eagle()
sparrow1=Sparrow()  

flight_test(eagle1)
flight_test(sparrow1)
              