import random

print("Welcome to 21 Number Game!")
ask = input("Do you want to start this game(Y/N): ").lower()

if ask=="y":
    computer_status = 0
    user_status = 0
    all_number = [2]
    is_running = True
    is_gameover = False

    while is_running:
        # number check (exist or not)
        def input_check(num):
            if num in all_number:
                if user_status == 1:
                    print("Sorry! This number already exist, try another one.")
                    try:
                        user_input()

                    except RecursionError:
                        is_gameover = True

                elif computer_status == 1:
                    try:
                        computer_input()
                    except RecursionError:
                        is_gameover = True
            else:
                all_number.append(num)


        # user input--------------------------
        def user_input():
            n = int(input("Enter a number: "))
            input_check(n)

        def taking_input_from_user(n):
            for i in range(n):
                user_input()

        # computer input----------------------
        def computer_input():
            n = random.randint(1,21)
            input_check(n)

        def taking_input_from_computer(n):
            for i in range(n):
                computer_input()

        def first_chance():
            number_of_user_input = int(input("How many number do you want to enter: "))
            taking_input_from_user(number_of_user_input)

        def second_chance():
            num_of_computer_input = random.randint(1, 10)
            taking_input_from_computer(num_of_computer_input)

        # Chance Selector--------------------
        chance = input("Do you want first chance or second chance(F/S): ").lower()

        # def chance_selector(chance):

        if chance == "f":
            user_status = 1
            computer_status = 0
            first_chance()

        elif chance == "s":
            computer_status = 1
            user_status = 0
            second_chance()



        # list display--------------------


        display_list = sorted(all_number)
        print(display_list)

        if len(display_list)>=21:
            print("Game Over.")
            is_running = False






