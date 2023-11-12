import random

tries = int(input("Enter number of tries: "))

is_running = True
count = 0

def secret_num_generator():
    # num = [1,2,0,3]
    secret_code = random.sample(range(10),4)

    if secret_code[0]==0:
        n = [i for i in range(1,10) if i not in secret_code]
        secret_code[0] = random.choice(n)

        return secret_code
    else:
        return secret_code

secret_code = secret_num_generator()

# print(secret_code)

while is_running:
    count += 1
    cow = 0
    bull = 0
    # guess check function--------
    def check(guess,secret_code):
        global cow,bull
        s_code = secret_code
        #cows condition--------
        for i in set(guess):
            if i in str(secret_code):
                cow += 1

        #bulls condition..........
        for i in range(4):
            if guess[i] == str(s_code[i]):
                bull += 1


        print(f"The cow is: {cow}\nThe bull is: {bull}")


    # user guess------------
    guess = input("Enter your guess: ")

    check(str(guess),secret_code)


    # game end condition------------
    if tries == count:
        print("You reached total tries.")
        is_running = False