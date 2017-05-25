from playable_is_end_case import playable_is_end_case
from playable_non_end_case_rank import playable_non_end_case_rank
import numpy as np
''' 
Divide playable cards into end cases and non end cases.  Play non-end case cards before end case cards.  For non end
case cards play the card which corresponds to the card lane where you require the most cards from others to be 
played before you get to your end case.  For End cases, play the card which will allow the fewest number of cards 
for others to play.  If you have a 2hearts and ace hearts, the 2 of hearts is considered an endcase card (It's an 
endcase card that allows 0 other people's cards to be played).
'''

def adam_best_alg(pgs):
    if len(pgs['playable_cards']) is 0:
        return (None, None)
    elif len(pgs['playable_cards']) is 1:
        ret_card = pgs['playable_cards'][0]
        return ret_card
    else:
        end_case_list = []
        play_rank_list = []
        for card in pgs['playable_cards']:
            is_end_case,inverse_play_rank = playable_is_end_case(card, pgs['player_hand'])
            end_case_list.append(is_end_case)
            play_rank_list.append(inverse_play_rank)

    non_end_case_playable_cards = [x[1] for x in enumerate(pgs['playable_cards']) if not end_case_list[x[0]]]


    if len(non_end_case_playable_cards) is not 0:
        if len(non_end_case_playable_cards) is 1:
            ret_card = non_end_case_playable_cards[0]
            return ret_card
        else:
            non_end_case_rank_list = []
            for card in non_end_case_playable_cards:
                non_end_case_rank_list.append(playable_non_end_case_rank(card, pgs['player_hand']))
            ret_card = non_end_case_playable_cards[np.argmax(non_end_case_rank_list)]
            return ret_card
    else:
        end_case_playable_cards = [x[1] for x in enumerate(pgs['playable_cards']) if end_case_list[x[0]]]
        end_case_play_rank = [play_rank_list[x[0]] for x in enumerate(pgs['playable_cards']) if end_case_list[x[0]]]
        ret_card = end_case_playable_cards[np.argmin(end_case_play_rank)]
        return ret_card