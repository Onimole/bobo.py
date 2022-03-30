class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age


    def person(self):
        person = f'my name is {self.name} and my age is {self.age}'
        return person
details = Person("bobo",25)
print (details.person())
