from return_suits import *
def split_by_lane(cards):
    ''' 
    :param cards: must be sorted by suit and then number if they aren't cards.sort(key = lambda card: (card.suit, card.value))
    :return:
    '''
    suits = return_suits()
    lanes = [[[],[]] for _ in range(len(suits))]

    for card in cards:
        suit_index = suits.index(card.suit)
        if card.value < 7:
            lanes[suit_index][0].append(card)
        else:
            lanes[suit_index][1].append(card)

    return lanes
