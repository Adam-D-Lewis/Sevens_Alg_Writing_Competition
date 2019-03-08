import random
from adam_best_alg import adam_best_alg
# from farthest_from_seven_alg import farthest_from_seven_alg
from ai_turn import ai_turn

def human_turn(partial_gs):
    # #farthest_from_seven_alg
    # return farthest_from_seven_alg(partial_gs)

    #adam_best_alg
    return adam_best_alg(partial_gs)

    # # first available card
    # return partial_gs['playable_cards'][0]

    # # use the same strategy as the ai
    # return ai_turn(partial_gs)
