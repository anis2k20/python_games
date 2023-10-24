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



