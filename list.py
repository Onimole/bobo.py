#finding the largest number in a list

numbers =[54,43,12,67,90] 
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print (max)
