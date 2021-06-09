import random
import utils as utils


class GuessTheNumber:
    # generate random number from 1 - 100, instantiate tries to 1,
    # continue loop until user input matches the generated number
    generated_number = random.randint(1, 100)
    full_name = input("Enter a username to play\n")
    print("Hello, " + full_name + "\nWelcome to the guessing Game. My name is Nina, your CLI guide :)")

    try:
        selected_option = int(input("Press 1 and hit Enter to start game, \n"))
        print("A number has been generated from the range of 1 to 100. You have 3 attempts")
        user_input = int(input("Guess the number: \n"))
        tries = 0

        if selected_option == 1:
            # utils.guess_engine(u_input, answer, tries)
            # while user_input != generated_number:
            while tries != 2:
                # if tries != 2:
                if user_input < generated_number:
                    print("Go higher")
                    user_input = int(input("Guess the number: "))
                    tries += 1
                elif user_input > generated_number:
                    print("Go lower")
                    user_input = int(input("Guess the number: "))
                    tries += 1
                elif user_input == generated_number:
                    print("Congratulations, you guess right! :)")
            input("Oops, you didnt get the answer and have exhausted your tries. \n Press any key to exit!")
        else:
            print("Okay! Come play with me some other time. Bye :)")
    except:
        raise TypeError("Only integers are allowed")
