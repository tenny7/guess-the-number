import random, math

secret_number = random.randint(1, 10)

guess_number = None

count = 0
while count < 3:
    count += 1

    guess_number = int(input("Guess the number:  "))

    if guess_number == secret_number:
        print('You won')
        break
    else:
        print('try again')

if count >= 3:
    print("Game over")
