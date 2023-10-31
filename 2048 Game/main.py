import numpy as np
import random
# How to play
print("'U' or 'u': UP \t||\t'D' or 'd': DOWN\t||\t'L' or 'l': 'LEFT'\t||\t'R' or 'r': 'RIGHT'")

def start_game():
    # 4x4 block display------------
    class mat_blueprint:
        def __init__(self):
            self.mat = [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]


    class RandomPos:
         def __new__(self):
            return random.sample(range(0,3),2)
    r_p1 = RandomPos()
    r_p2 = RandomPos()

    mat = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],

    ]

    # Matrix initialization -------------
    for r in range(4):
       for c in range(4):
            if r_p1[0] == r and r_p1[1]== c:
                mat[r][c] = 2
            elif r_p2[0] == r and r_p2[1]== c:
                mat[r][c] = 2
            else:
                mat[r][c] = 0
    print(np.matrix(mat))
    print("\n")
    # End Matrix initialization -----------

    # Functionality------------------------
    def up():
        new_pos = RandomPos()
        new_mat = mat_blueprint().mat

        print(np.matrix(new_mat))


    up()






start_game()