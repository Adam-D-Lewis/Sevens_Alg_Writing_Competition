from is_logic_valid_play import is_logic_valid_play
# This function checks if the card_played is able to be played based on if the previous necessary cards have been played.  It also checks if the player contained the card_played in his hand.
def is_valid_play(card_played, gs):
    if card_played is None:
        return True
    else:

        #player must have that card in hand, and it must be playable
        #check if player had that card in hand
        in_hand = False
        for card in gs['player_hands'][gs['player_turn']-1]:
            if card_played == card:
                in_hand = True
                break
        if in_hand == False:
            return False

        #code below only runs if card is in player's hand
        return is_logic_valid_play(card_played, gs)

