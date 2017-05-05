def is_logic_valid_play(card_played, gs):
    # This function checks if the card_played is able to be played based on if the previous necessary cards have been played.  It does NOT check if hte player contained the card_played in his hand.

    #7's always playable, if greater than 7 then playable if lower card (same suit) has been played, if less than 7 then playable if higher card, same suit has been played
    if card_played[0] < 7:
        # check if the previous required card has been played
        for round in gs['cards_played']:
            for card in round:
                if card[0] == card_played[0]+1 and card[1] == card_played[1]:
                    return True
    elif card_played[0] == 7:
        #sevens always playable
        return True
    elif card_played[0] > 7:
        # check if the previous required card has been played
        for round in gs['cards_played']:
            for card in round:
                if card[0] == card_played[0]-1 and card[1] == card_played[1]:
                    return True

    return False
