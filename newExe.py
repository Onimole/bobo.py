#Q2. Create a non-parameterized constructor and set the default values for the following attributes:

#make = “Aud”

#model = “SQ”

#doors = 4

#wheels = 4

class Cars:
    def __init__(self):
        self.make = "Aud"
        self.model = "SQ"
        self.doors = 4
        self.wheels = 4
    def all_value (self):
        return f"{self.make}, {self.model}, {self.doors}, {self.wheels}"
car1 = Cars()
print (car1.all_value())