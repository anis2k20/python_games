from art import art
class Display:
    def __init__(self,position):
        self.position = position
        try:
            print(art[position])
        except IndexError:
            print("Game Over.")



