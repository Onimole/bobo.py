#guessing game using while loop

secrete_number = 7
guess_count = 0
guess_limits = 3

while guess_count < guess_limits:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secrete_number:
        print ("You Won")
        break
    else:
        print("You Failed")