from split_by_lane import split_by_lane
from return_suits import return_suits

def playable_is_end_case(playable_card, hand):
    '''returns if the card is an endcase and the number of cards which will be playable by other player's after playing 
    it'''
    hand_by_lane = split_by_lane(hand)

    suits = return_suits()
    suit_index = suits.index(playable_card.suit)
    suit_hbl = hand_by_lane[suit_index] #suit hand by lane (hbl)
    if playable_card.value < 7:
        suit_lane = suit_hbl[0]
    else:
        suit_lane = suit_hbl[1]

    playable_is_end_case = False
    helping_others_num = None
    if playable_card.value < 7:
        if playable_card.value is suit_lane[-1].value and suit_lane[-1].value is suit_lane[0].value + len(suit_lane) - 1:
            playable_is_end_case = True
            if playable_card.value == suit_lane[0].value:
                helping_others_num = playable_card.value - 1
            else:
                helping_others_num = 0
    else:
        if playable_card.value is suit_lane[0].value and suit_lane[0].value is suit_lane[-1].value - len(suit_lane) + 1:
            playable_is_end_case = True
            if playable_card.value == suit_lane[-1].value:
                helping_others_num = 13 - playable_card.value
            else:
                helping_others_num = 0

    return playable_is_end_case, helping_others_num
