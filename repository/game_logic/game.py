def create_player(name="AI"):
    player = {"name":name, "hand":[],"won_pile":[]}
    return player


def init_game():
    player1 = create_player("p1")
    player2 = create_player()
    deck = create_deck()
    deck = shuffle(deck)
    player1["hand"] = deck[0:26]
    player2["hand"] = deck[26:]
    game_dict = {"deck":deck,"player_1":player1,"player_2":player2}
    return game_dict


def play_round(player_1, player_2):
    card1 = player_1["hand"][0]
    card2 = player_2["hand"][0]
    winner = compare_cards(card1,card2)
    if winner == "p1":
        player_1["won_pile"].append(card1)
        player_1["won_pile"].append(card2)
    elif winner == "p2":
        player_2["won_pile"].append(card1)
        player_2["won_pile"].append(card2)
    elif winner == "WAR":
        return None
    return None



