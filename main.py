import random

HOW_MANY_TIME_IT_RUN = 5
container = []
# first_chance---------------------
def first_chance(c):
    global HOW_MANY_TIME_IT_RUN

    # check consecutive
    def check_consecutive(c):
        return sorted(c) == list(range(min(c),max(c)+1))

    if c == "f":
        HOW_MANY_TIME_IT_RUN -= 1
        # input function--------------
        def input_func(x):
            my_values = []
            for i in range(x):
                n = int(input("Enter value: "))
                my_values.append(n)

            is_consecutive = check_consecutive(my_values)

            if is_consecutive is True:
                container.append(my_values)
                if HOW_MANY_TIME_IT_RUN >=0:
                    second_chance(x)
            else:
                disqualified()

        # finish line check----------
        if HOW_MANY_TIME_IT_RUN >= 0:
            print("Your turn.")
            input_amount = int(input("How many number do you want as a input?: "))

            if input_amount < 4:
                input_func(input_amount)

            elif input_amount >= 4:
                disqualified()

    # when I choose 2nd turn player
    else:
        HOW_MANY_TIME_IT_RUN -= 1
        my_values = []
        for i in range(4-c):
            n = int(input("Enter value: "))
            my_values.append(n)
        is_consecutive = check_consecutive(my_values)
        if is_consecutive is True:
            container.append(my_values)
            print(container)
            if HOW_MANY_TIME_IT_RUN>=1:
                second_chance("s")

        else:
            disqualified()


# Second chance---------------------
def second_chance(c):
    if c == "s":
        values = []
        if not container:
            last_element = 0
        else:
            last_element = container[-1][-1]
        y = random.randint(1,3)
        for i in range(y):
            last_element += 1
            values.append(last_element)
        container.append(values)
        print(container)
        # first_chance(y)

        # Game finish line---------------
        if HOW_MANY_TIME_IT_RUN >= 1:
            first_chance(y)


    # when I am choose 1st turn player
    else:
        input_amount = 4-c
        values = []
        last_element = container[-1][-1]

        for i in range(input_amount):
            last_element += 1
            values.append(last_element)
        container.append(values)
        print(container)


        # Game finish line---------------
        if HOW_MANY_TIME_IT_RUN >= 1:
            first_chance("f")




# disqualified----------------------
def disqualified():
    print("You are disqualified")






# Game initial point----------------
print("Player 2 is computer.")
ask = input("Do you want to play 21 Number Game? (Y/N): ").lower()
choice = input("Do you want first chance or second chance(F/S): ").lower()

if choice == "f":
    first_chance(choice)
elif choice == "s":
    second_chance(choice)


# finish line check------------
# if HOW_MANY_TIME_IT_RUN>1:
#     print("Your turn.")
#     input_amount = int(input("How many number do you want as a input?: "))
#
#     if input_amount<4:
#         input_func(input_amount)
#
#     elif input_amount>=4:
#         disqualified()
# else:
#     print("Game over")

# Testing Section------------
print(container)
