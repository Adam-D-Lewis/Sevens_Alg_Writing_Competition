def win_condition(gs):
    '''win_condition(gs):
        takes game state as imput and exports a bool to indicate if the win_condition has been met'''

    for hand in gs['player_hands']:
        if len(hand) == 0:
            return True
    return False
