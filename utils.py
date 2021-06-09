import message as m


def guess_engine(selected_option, generated_number):
    print("A number has been generated from the range of 1 to 100. You have 5 attempts")
    user_input = int(input("Guess the number: \n"))
    tries = 0

    if selected_option == 1:
        while tries != 4:
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
        input(m.game_over_info())
    else:
        print("Okay! Come play with me some other time. Bye :)")
