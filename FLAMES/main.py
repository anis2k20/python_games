def remove_common_char(f,s):
    x = [i for i in f if i not in s]
    y = [j for j in s if j not in f]
    return x+y

f_player_name = input("Enter 1st Person Name: ").lower()
s_player_name = input("Enter 2nd Person Name: ").lower()
unique_char = len(remove_common_char(f_player_name,s_player_name))
COUNT = unique_char

flames = ['F','L','A','M','E','S']

i = 0
for j in range(len(flames)):
    c,t=0,0
    for char in flames:
        t += len(char)
        c = t + i
        if c==COUNT:
            index = flames.index(char)
            i = len(flames[index+1:])
            flames.pop(index)
            break

def rel(x):
    if x =="E":
        return("Enemies")
    elif x == "F":
        return("Friends")
    elif x == "L":
        return("Lovers")
    elif x == "A":
        return("Affectionate")
    elif x == "M":
        return("Marriage")
    elif x == "S":
        return("Siblings")

print(f"Relationship Status : {rel(flames[0])}")






