# def remove_common_char(f,s):
#     x = [i for i in f if i not in s]
#     y = [j for j in s if j not in f]
#     return x+y
#
# f_player_name = input("Enter 1st Person Name: ").lower()
# s_player_name = input("Enter 2nd Person Name: ").lower()
# unique_char = len(remove_common_char(f_player_name,s_player_name))

flames = ['F','L','A','M','E','S']
COUNT = 4
c = 0
track = 0
def cutting():
    global c,track
    for i in flames:
        c += len(i)+track
        try:
            if c%3==0:
                x = flames.pop(c)
                track = len(flames[3:])
        except IndexError:
            print("Index out of range")

while len(flames)>1:
    cutting()
    print(flames)
    print(track)



