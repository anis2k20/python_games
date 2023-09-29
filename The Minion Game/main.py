from itertools import combinations

def minion_game(string):
    vowel = ["a", "e", "i", "o", "u"]

    def stuart(string_list):
        count = 0
        for i in string_list:
            if i.lower()[0] in vowel:
                print(i)
                count += 1
        print(count)


    sub_string = [''.join(l) for i in range(len(string)) for l in combinations(string, i+1)]
    stuart(sub_string)





    def kevin(string_list):
        pass


#[''.join(l) for i in range(len(x)) for l in combinations(x, i+1)]



s = "BANANA"
minion_game(s)