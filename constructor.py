# construtor Exercise
class Dress():
    def __init__(self):
        self.cloth = 'cotton'
        self.type = 'Round Neck'
    def get_details(self):
        return f"Cloth = {self.cloth}\nType = {self.type}"
round_neck = Dress()
print (round_neck.get_details())