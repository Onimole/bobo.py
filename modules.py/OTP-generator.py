#Generating an otp code
import math, random

OTP = "0123456789"

OTP = "0123456789abcdefghijklmnopqrstuvwxyz"

size = 6

generate_OTP = ""
length = len(OTP)
for _ in range(size):
    generate_OTP += OTP [math.floor(random.random() * length)]
print("your OTP CODE is: ", generate_OTP)