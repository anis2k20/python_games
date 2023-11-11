import random

tries = int(input("Enter number of tries: "))

is_running = True
count = 0
def secret_num_generator():
    num = [1,2,0,3]
    secret_code = random.sample(num,4)
    if secret_code[0]==0:
        n = [i for i in range(1,10) if i not in secret_code]
        secret_code[0] = random.choice(n)
        return secret_code
    else:
        return secret_code

secret_code = secret_num_generator()



print(secret_code)
while is_running:
    count += 1
    cow = 0
    bull = 0
    # guess check function--------
    def check(guess,secret_code):
        global cow
        #cows condition--------
        for i in guess:
             if i in secret_code:
                 cow += 1

        print(cow)



    # user guess------------
    guess = int(input("Enter your guess: "))
    check(str(guess),str(secret_code))




    # game end condition------------
    if tries == count:
        is_running = False