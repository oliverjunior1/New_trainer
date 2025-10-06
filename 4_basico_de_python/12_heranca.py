class Dog:
    def sound(self):
        print("dog sound")

class Labraddor(Dog):
    def sound(self):
        print("Woof")

class Pincher(Dog):
    def sound(self):
        print("Nhac Nhac Nhac")

dogs = [Dog(), Labraddor(), Pincher()]

for x in dogs:
    x.sound()