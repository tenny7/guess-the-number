import random
import utils as u
import message as e


class GuessTheNumber:
    # generate random number from 1 - 100, instantiate tries to 1,
    # continue loop until user input matches the generated number
    generated_number = random.randint(1, 100)
    full_name = input("Enter a username to play\n")
    print("Hello, " + full_name + "\nWelcome to the guessing Game. My name is Nina, your CLI guide :)")

    try:
        selected_option = int(input("Press 1 and hit Enter to start game, \n"))
        u.guess_engine(selected_option, generated_number)
    except TypeError:
        print(e.integer_only())
