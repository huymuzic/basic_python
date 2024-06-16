class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def slumber(self):
        print("This animal is sleeping")

class Rabbit(Animal):

    def run(self):
        print("This rabbit is running")

class Fish(Animal):

    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    
    def fly(self):
        print("This hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.slumber()

rabbit.run()
fish.swim()
hawk.fly()

# multilevel inheritance = when a derived (child) class inherits another derived (child) class

class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Dog(Animal):

    def bark(self):
        print("This dog is barking")
    
dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()

# multiple inheritance = when a child class is derived from more than one parent class

class Prey:

    def flee(self):
        print("This animal is fleeing")

class Predator:

    def hunt(self):
        print("This predator is hunting")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# # rabbit.flee()
# # hawk.hunt()
# fish.flee()
# fish.hunt()

