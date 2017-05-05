import random
# from adam_best_alg import adam_best_alg
from ai_turn import ai_turn

def human_turn(partial_gs):
    # # first available card
    # return partial_gs['playable_cards'][0]

    # use the same strategy as the ai
    return ai_turn(partial_gs)
