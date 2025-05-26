
class Animal:
    def speak(self):
        print("animal makes sound")

class Cat(Animal):
    def sound(self):  
        print("cat makes sound meow")

cat1 = Cat()
cat1.speak()
cat1.sound()