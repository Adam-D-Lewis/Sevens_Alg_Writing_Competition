from split_by_lane import split_by_lane
from return_suits import return_suits

def playable_non_end_case_rank(non_end_case_playable_card, hand):
    necp_card = non_end_case_playable_card
    hand_by_lane = split_by_lane(hand)

    suits = return_suits()
    suit_index = suits.index(necp_card.suit)
    suit_hbl = hand_by_lane[suit_index]  # suit hand by lane (hbl)
    suit_lane = suit_hbl[0]

    if necp_card.value < 7:
        return necp_card.value-suit_hbl[0][0].value-len(suit_hbl[0])+1
    elif necp_card.value is 7:
        if len(suit_hbl[0]) is 0:
            lower_val = 0
        else:
            lower_val = suit_hbl[0][0].value
        return suit_hbl[1][-1].value - lower_val - len(suit_hbl[0]) - len(suit_hbl[1]) + 1
    else:
        return suit_hbl[1][-1].value-necp_card.value-len(suit_hbl[1]) + 1