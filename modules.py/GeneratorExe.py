#Write a program to print a random value from the list 
# [Phil, Cam, Luke, Lily, jay, Cameron, Michelle].
from random import choice
from random import shuffle
from random import randrange

names = ["phil", "cam", "luke", "lily", "jay", "cameron", "michelle"]

print(choice(names))

shuffle (names)
print(names)

integers = [randrange(pow(10, 9), pow(10, 10)) for _ in range(4)]
print(integers)