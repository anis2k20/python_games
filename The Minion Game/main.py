
from itertools import permutations
import re

def minion_game(string):
    vowel = ["a", "e", "i", "o", "u"]

    perms = set()
    stuart = []
    kevin = []
    stuart_score = 0
    kevin_score = 0

    for i in range(1, len(string) + 1):
        for c in permutations(string, i):
            perms.add("".join(c))

    for i in perms:
        if i in string:
            if i[0].lower() in vowel:
                if i in string:
                    kevin.append(i)
            else:
                stuart.append(i)

    # calculation for STUART-----------
    for i in (sorted(stuart,key=len)):
        regex = f"(?={i})"
        res = len(re.findall(regex, string))
        stuart_score += res

    #calculation for KEVIN-----------
    for i in (sorted(kevin,key=len)):
        regex = f"(?={i})"
        res = len(re.findall(regex, string))
        kevin_score += res

    if stuart_score>kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print(f"Kevin {kevin_score}")

s = "BANANA"
minion_game(s)