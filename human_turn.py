import random
from adam_best_alg import adam_best_alg
from ai_turn import ai_turn

def human_turn(partial_gs):
    # # first available card
    # return partial_gs['playable_cards'][0]

    # play a random card
    card_index = random.randint(0, len(partial_gs['playable_cards'])-1)
    return partial_gs['playable_cards'][card_index]

    # # use the same strategy as the ai
    # return ai_turn(partial_gs)

    # # use my best algorithm
    # return adam_best_alg(partial_gs)