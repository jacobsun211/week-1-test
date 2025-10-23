from game_logic import game
from utils import deck

if __name__ == '__main__':
    def main():
        deck = init_game()
        deck_of_p1 = deck["player_1"]["hand"]
        deck_of_p2 = deck["player_2"]["hand"]
        while len(deck_of_p1) > 0 and len(deck_of_p2):
            play_round(deck["player_1"], deck["player_2"])
            deck_of_p1.pop(0)
            deck_of_p2.pop(0)
        won_pile_p1 = deck["player_1"]["won_pile"]
        won_pile_p2 = deck["player_2"]["won_pile"]
        if len(won_pile_p1) > len(won_pile_p2):
            print("the winner is:", deck["player_1"]["name"])
        elif len(won_pile_p2) > len(won_pile_p1):
            print("the winner is:", deck["player_2"]["name"])
        else:
            print("DREW, lets do a tie breaker")
            hearts = 0
            for card in won_pile_p1:
                if card["suite"] == "H":
                    hearts += 1
            if hearts >= 7:
                print(f"the winner is {deck["player_1"]["name"]} since he has more hearts")
                print(f"he has {hearts} hearts")
            else:
                print(f"the winner is {deck["player_2"]["name"]} since he has more hearts")
                print(f"he has {13 - hearts} hearts")

    main()
