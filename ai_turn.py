import random as rand

def ai_turn(pgs):
    # returns a random playable card
    if len(pgs['playable_cards']) is 0:
        return (None, None)
    elif len(pgs['playable_cards']) is 1:
        ret_card = pgs['playable_cards'][0]
        return ret_card
    else:
        card_index = rand.randint(0, len(pgs['playable_cards']) - 1)
        return pgs['playable_cards'][card_index]