from words import word_list
import random

TOTAL_CHANCES = 10

random_word = random.choice(word_list).lower()
print(random_word)
print(f"The word hints is: {random_word[0]} _ _ _ {random_word[-1]}")

def user_guess():
    flag = 0
    for i in range(TOTAL_CHANCES):
        user_guess = input("Enter guessing latter: ")

        if flag<5:
            if user_guess == random_word[flag]:
                print("Correct")
                flag+=1
            else:
                print("Wrong")
        if flag==5:
            print(f"You win, The word was {random_word}.")
            return False
        elif i==9 and flag!=5:
            print(f"You loss, The word was {random_word}.")
            return False

user_guess()



