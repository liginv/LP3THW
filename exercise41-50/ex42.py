# Animals is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# Dog has-a object called Animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name

# Cat has-a object called Animal
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a name
        self.name = name

# Person is-a class
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        #  Person has-a pet of some kind
        self.pet = None

# Employee has-a object called Person
class Employee(Person):

    def __init__(self, name, salary):
        # ?? hmm what is this strange magic?
        super(Employee, self).__init__()
        # Employee has-a salary
        self.salary = salary

# Fish is-a class
class Fish(object):
    pass

# Salmon has-a object Fish
class Salmon(Fish):
    pass

# Halibut has-a object Fish
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet satan
mary.pet = satan

# frank is-a employee; has-a salary
frank = Employee("Frank", 120000)

# frank has-a pet rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# coruse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()