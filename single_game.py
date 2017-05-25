# singleGame.py
import collections
from itertools import product
import random
from win_condition import win_condition
from is_valid_play import is_valid_play
import copy
from return_suits import return_suits

def single_game(human_turn, ai_turn):
    # I use this function to deal out the cards later.
    def grouper(iterable, n, fillvalue=None):
        """Collect data into fixed-length chunks or blocks"""
        # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
        args = [iter(iterable)] * n
        return zip(*args)

    # initialize game variables
    suits = return_suits()
    values = range(1, 14)
    numPlayers = 4
    numCards = len(suits)*len(values)

    # Create Deck
    Card = collections.namedtuple('Card', 'value suit')

    deck = [Card(v, s) for v, s in product(values, suits)]
    #The player who is dealt the starting_flag card will become player 1 and plays first.
    starting_flag = deck[deck.index((2, 'clubs'))]

    random.shuffle(deck)

    if numCards % numPlayers is not 0:
        raise ValueError("Hey, your number of players isn't divisible by the number of players")
    hand_iterators = grouper(deck, 13)
    deck = list(map(list, hand_iterators))
    for start_index, hand in enumerate(deck):
        if starting_flag in hand:
            break

    # make the player with the starting_flag card Player 1 (determined by being at the beginning of deck)
    deck.insert(0, deck.pop(start_index))

    #sort each players hand
    for hand in deck:
        hand.sort(key = lambda card: (card.suit, card.value))

    #Assign the human_player a random play order (Player 1-4)
    human_player_turn_order = random.randint(1, 4)

    # initialize game state (dictionary with 3 elements: 1) all cards played (and who played them) 2) what cards each player has in their hand 3) who's turn it is
    gs = {'cards_played': [], 'player_hands': deck, 'player_turn': 0}
    table = [[] for _ in range(4)]

    while win_condition(gs) is False:
        # update player_turn
        if gs['player_turn'] == numPlayers:
            gs['player_turn'] = 1
        else:
            gs['player_turn'] += 1

        # determine which of the current player's cards are playable
        current_player_hand = gs['player_hands'][gs['player_turn']-1]
        playable_cards = []
        playable_cards_copy = []
        for card in current_player_hand:
            if is_valid_play(card, gs):
                playable_cards.append(card)
                playable_cards_copy.append(card)

        # if the player has at least one playable card, then create the partial game state to pass to the player algorithms (partial game state because you don't get to know what cards the other players are holding).  If the player has 0 playable cards, then just have them return a (None, None) card which represents them passing.
        if len(playable_cards) is not 0:
            if not 'partial_gs' in locals():
                partial_gs = {'cards_played': copy.deepcopy(gs['cards_played']), 'player_turn': copy.deepcopy(gs['player_turn']), 'player_hand': copy.deepcopy(current_player_hand), 'playable_cards': copy.deepcopy(playable_cards), 'table': copy.deepcopy(table)}
                pgs_hands = copy.deepcopy(gs['player_hands'])
                partial_gs_copy = copy.deepcopy(partial_gs)

            #update partial_gs and its copy
            partial_gs_copy['player_hand'] = gs['player_hands'][gs['player_turn']-1]
            partial_gs_copy['playable_cards'] = playable_cards_copy
            partial_gs['player_hand'] = pgs_hands[gs['player_turn']-1]
            partial_gs['playable_cards'] = playable_cards

            if partial_gs != partial_gs_copy:
                print('They tried to cheat!')
                partial_gs = {'cards_played': copy.deepcopy(gs['cards_played']), 'player_turn': copy.deepcopy(gs['player_turn']), 'player_hand': copy.deepcopy(current_player_hand), 'playable_cards': copy.deepcopy(playable_cards), 'table': copy.deepcopy(table)}

            # ask which card to play from computer algorithm (or human)
            # if they try to play an unplayable card, then just play the first appropriate card, if none are available then return None
            if gs['player_turn'] == human_player_turn_order:
                card_played = human_turn(partial_gs)
            else:
                card_played = ai_turn(partial_gs)

            # if they try to submit an invalid card, then just play the first playable card
            if not is_valid_play(card_played, gs):
                card_played = playable_cards_copy[0]

            # remove the card from their hand
            gs['player_hands'][gs['player_turn']-1].remove(card_played)
            pgs_hands[gs['player_turn']-1].remove(card_played)


            # place the card on the table in the appropriate position
            suit_index = suits.index(card_played[1])
            if card_played[0] >= 7:
                table[suit_index].append(card_played)
            else:
                table[suit_index].insert(0, card_played)
        else:
            card_played = (None, None)

        # add their card to the cards_played list
        if gs['player_turn'] != 1:
            gs['cards_played'][-1].append(card_played)
        else:
            gs['cards_played'].append([card_played])

    # determine if the human won
    human_won = gs['player_turn'] is human_player_turn_order
    return human_won
