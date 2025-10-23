from random import randint


def create_card(rank, suite):
    try:
        value = int(rank)
    except ValueError:
        match rank:
            case "J":
                value = 11
            case "Q":
                value = 12
            case "K":
                value = 13
            case "A":
                value = 14
    card = {"rank":rank, "suite":suite,"value":value}
    return card


def compare_cards(p1_card, p2_card):
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p1_card["value"] < p2_card["value"]:
        return "p2"
    else:
        return "WAR"

def create_deck():
    suits = ["H","C","D","S"]
    ranks = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    deck = []
    for suite in suits:
        for rank in ranks:
            card = create_card(rank, suite)
            deck.append(card)
    return deck

def shuffle(deck):
    for i in range(1000):
        index1 = randint(0,51)
        index2 = randint(0,51)
        deck[index1],deck[index2] = deck[index2],deck[index1]
    return deck








