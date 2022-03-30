class Person:
    def __init__(self, name):
        self.name = name


    def talk(self):
        print (f"hi i'm {self.name}")
        


john = Person('john')
john.talk()

bob = Person('bob')
bob.talk()

sarah = Person('Sarah')
sarah.talk()

mary = Person('mary')
mary.talk()