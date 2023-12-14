import random
class Game:
    card_rank = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
    card_identity = ['Clubs','Hearts','Spades','Diamond']

    def __init__(self):
        self.user1 = input("Enter first user name: ")
        self.user2 = input("Enter second user name: ")
        print("Game begining...")

    def card_make(self):
        card_rank = random.choice(self.card_rank)
        card_identity = random.choice(self.card_identity)
        card = [card_rank, card_identity]
        return card

    def compare(self,card1,card2):
        card1_index = self.card_rank.index(card1)
        card2_index = self.card_rank.index(card2)
        if card1_index>card2_index:
            return f'{self.user1} is winner'
        elif card2_index>card1_index:
            return f'{self.user2} is winner'
        else:
            return "Both are same"

game = Game()
card1 = game.card_make()
card2 = game.card_make()
print(f'First player card: {card1[0]} of {card1[1]}')
print(f'Second player card: {card2[0]} of {card2[1]}')
winner = game.compare(card1[0],card2[0])
print(f"Winner: {winner}")
