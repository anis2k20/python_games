import random

print("Colors: Red(R), Green(G), Blue(B), Yellow(Y), Orange(O), Purple(P)")
colors = ['R', 'G', 'B', 'Y', 'O', 'P']
random_color = random.sample(colors,4)
# print(random_color)

attempt = 10

def game_status():

    for i in range(attempt):
        match_color = 0
        exact_match = 0

        user_input = list(input("Enter 4 colors without space: ").upper())
        temp = user_input
        for latter in set(user_input):
            if latter in random_color:
                match_color += 1
                if random_color.index(latter) == temp.index(latter):
                    exact_match += 1

        print("Match color: ",match_color)
        print("Exact match",exact_match)


# Game status running status----------
        if exact_match==4:
            print("You win.")
            return False
        else:
            print("You loss")

game_status()

