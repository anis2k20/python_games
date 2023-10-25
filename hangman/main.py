from art import art
from words import word_list
import random
from display import Display

random_word = random.choice(word_list)
word_length = len(random_word)

# random word hints
underscore = ""
print(random_word)
for i in range(word_length-2):
    underscore += "_ "

# End random word hints

# latter matching code
def word_match():
    attempt=10
    comparing_word = ""
    dash_count = len(random_word)
    word_travers = 0
    HANG = 0

    print(f"Word hint: {random_word[0]} {underscore} {random_word[-1]}")
    for i in range(attempt):
        display = Display(HANG)
        # user input

        user_input = input("Enter guessing latter: ").lower()
        try:
            if user_input == random_word[word_travers].lower():
                comparing_word += user_input

                dash_count -= 1
                word_travers +=1
                dash=""
                for i in range(dash_count):
                    dash +="_ "
                print(f"{random_word[:word_travers]} {dash}")

            else:
                HANG += 1

        except IndexError:
            print("Game Over.")
            if comparing_word.lower() == random_word.lower():
                print("You win!")
            else:
                print("You Loss!")

    print("Game Over.")
    if comparing_word.lower() == random_word.lower():
        print("You win!")
    else:
        print("You Loss!")


    # print("Game Over.")
    # if comparing_word == random_word:
    #     print("You win!")
    # else:
    #     print("You Loss!")



art_instruction = word_match()

# print(art_instruction)



