import random
import utils as utils


class GuessTheNumber:
    # generate random number from 1 - 100, instantiate tries to 1,
    # continue loop until user input matches the generated number
    generated_number = random.randint(1, 100)
    full_name = input("What is your name? \n")
    print("Hello, " + full_name + "\nWelcome to the guessing Game.")

    try:
        selected_option = int(input("Press 1 and hit Enter to start game, \n"))
        print("A number has been generated.")
        user_input = int(input("Guess the number: \n "))
        tries = 1

        if selected_option == 1:
            # utils.guess_engine(u_input, answer, tries)
            while user_input != generated_number:
                if user_input < generated_number:
                    print("Go higher")
                    user_input = int(input("Guess the number: "))
                    tries += 1
                elif user_input > generated_number:
                    print("Go lower")
                    user_input = int(input("Guess the number: "))
                    tries += 1
                elif user_input == generated_number:
                    print("Hurray, you guessed right")
                else:
                    print("Try again")
            if tries == 7:
                input("You have exhausted your tries. Subscribe for more. \n Press any key to exit!")
        else:
            print("Okay! See you some other time. :)")

    except:
        raise TypeError("Only integers are allowed")
