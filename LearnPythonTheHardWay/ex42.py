## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## Name is-a Cat
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self, name, salary):
        ## Employee is-a person, hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## winky is-a Cat
winky = Cat("Winky")

## Mary is-a Person
mary = Person("Mary", 130000)

## Mary has-a winky
mary.pet = winky

## Frank is-a Employee
frank = Employee("Frank", 120000)

## Frank has-a rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
