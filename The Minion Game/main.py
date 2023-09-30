from itertools import combinations
from itertools import permutations

def minion_game(string):
    vowel = ["a", "e", "i", "o", "u"]

    perms = set()
    stuart = []

    for i in range(1, len(string) + 1):
        for c in permutations(string, i):
            perms.add("".join(c))
    count = 0
    for i in perms:
        if i in string:
            if i[0].lower() in vowel:
                if i in string:
                    pass
            else:
                stuart.append(i)


    for i in (sorted(stuart,key=len)):
        if i in string:
            count += string.count(i)

    print(count)



    # for c in perms:
    #     if c[0].lower() in vowel:
    #         count +=1
    #         print(c)
    # print(count)




    # def stuart(string_list):
    #     count = 0
    #     # print(string_list)
    #     for i in string_list:
    #         if i.lower()[0] in vowel:
    #             print(i)
    #             count += 1
    #     print(count)


    # l=[]
    # [l.append(i) for i in sub_string if i not in l]
    # stuart(l)


#[''.join(l) for i in range(len(x)) for l in combinations(x, i+1)]



s = "BANANA"
minion_game(s)