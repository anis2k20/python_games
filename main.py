import random

NEAR = 4
container = []
# first_chance---------------------
def first_chance():
    # check consecutive
    def check_consecutive(c):
        return sorted(c) == list(range(min(c),max(c)+1))

    # input function--------------
    def input_func(x):
        my_values = []
        for i in range(x):
            n = int(input("Enter value: "))
            my_values.append(n)

        is_consecutive = check_consecutive(my_values)
        print(type(is_consecutive))
        if is_consecutive is True:
            container.append(my_values)
            second_chance()
        else:
            disqualified()



    print("Your turn.")
    input_amount = int(input("How many number do you want as a input?: "))

    if input_amount<4:
        input_func(input_amount)

    elif input_amount>=4:
        disqualified()





# Second chance---------------------
def second_chance():
    print("I am second chance")



# disqualified----------------------
def disqualified():
    print("You are disqualified")



# Game initial point----------------
print("Player 2 is computer.")
ask = input("Do you want to play 21 Number Game? (Y/N): ").lower()
choice = input("Do you want first chance or second chance(F/S): ").lower()

if choice == "f":
    first_chance()
elif choice == "s":
    second_chance()

# Testing Section------------
print(container)
