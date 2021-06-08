import random


class GuessTheNumber:
    # generate random number from 1 - 100, instantiate tries to 1,
    # continue loop until user input matches the generated number
    generated_number = random.randint(1, 100)
    user_input = int(input("Guess the number: "))
    tries = 1
    while user_input != generated_number:
        if user_input < generated_number:
            print("Go higher")
            user_input = int(input("Guess the number: "))
            tries += 1
            break
        elif user_input == generated_number:
            print("Hurray, you guessed right")
        else:
            print("Go lower")
            user_input = int(input("Guess the number: "))
            tries += 1
    if tries == 7:
        input("You have exhausted your tries. Subscribe for more. \n Press any key to exit!")
