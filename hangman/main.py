from art import art
from words import word_list
import random

random_word = random.choice(word_list)
word_length = len(random_word)

# random word hints
underscore = ""
print(random_word)
for i in range(word_length-2):
    underscore += "_ "
print(f"Word hint: {random_word[0]} {underscore} {random_word[-1]}")
# End random word hints

# latter matching code
def word_match():
    attempt=10

    dash_count = len(random_word)
    word_travers = 0
    for i in range(attempt):
        # user input
        user_input = input("Enter guessing latter: ")


        if user_input == random_word[word_travers]:
            dash_count -= 1
            word_travers +=1
            dash=""
            for i in range(dash_count):
                dash +="_ "
            print(f"{random_word[:word_travers]} {dash}")

        else:
            print("not exist")


art_instruction = word_match()
# print(art_instruction)



