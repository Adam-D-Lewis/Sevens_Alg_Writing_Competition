Sevens Algorithm
------------------------------------------------------------
We'll be competing to see who can get the highest win percentage after 1,000,000 games.  The computer players will select one of their playable cards AT RANDOM.  This way everyone can compete.

How to Play Sevens
---------------------------------
Many of you have never played sevens, but rest assured it is a very simple game and you will get the hang of it in no time.  A good explanation of how to play can be found at "http://www.classicgamesandpuzzles.com/Sevens.html" but I suggest actually playing a few rounds to get a good sense of strategies you might want to try.

You can download a sevens game for android at "https://play.google.com/store/apps/details?id=com.game.sevencentre".  You can download a sevens game for iOS at "https://itunes.apple.com/us/app/sevens-card-game/id926091764?mt=8"  Note that some versions of the game allow you to pass 3 times even if you could play.  In the version of the game that we'll play, you must play if you have a playable card on your turn.

Instructions for Algorithm Writers
------------------------------------
Just write a new human_turn.py file that takes the partial game state as an input and returns one of the playable cards.

The partial game state (pgs or partial_gs) is a dictionary with the following keys: cards_played, player_turn, player_hand, playable_cards, and table.
    The cards_played value is a n by 4 numpy array with each row corresponding to players 1-4 each playing a card or passing.  For example to see what the 1st card played by the 4th player, you could enter the following, pgs['cards_played'][0][3].
    The player_turn is just the player number of the current player (1 indexed).  For example, if you are the 4th player to play, then in your player algorithm pgs['player_turn']  would return 4.
    pgs['player_hand'] returns a list of every card currently in your hand sorted by suit and subsorted by number.  For example, pgs['player_hand'][0] might return [[2, 'clubs'], [8, 'clubs']]
    pgs['playable_cards'] will return a list of the cards in your hand which are playable on that turn.  If the length of this list is 1, you should probably just return that card instead of running through your entire algorithm.
    pgs['table'] returns a list of length 4 with each element consisting of a list of cards of a certain suit that have been played, and are thus currently on the table. To see what the lowest and highest card of the diamond suit you could enter the following pgs['table'][1][0] (lowest card) & and pgs['table'][1][-1] (highest card).

Modules Needed
--------------
The only module that I use that isn't part of the standard library is matplotlib.  I just plot the results in main.py.  If you don't want to install matplotlib then you can just comment out those lines.

Cards
------
Each card is a named tuple.  They were made to remind you of how you might say the name of the card.  For example, the 4 of clubs would be given by [4, 'clubs'].  If a card were stored in the variable "card" then you could access its value and suit in the following manner:  card.value (or card[0]) and card.suit (or card[1]).  The card values go from 1-13 with 13 representing the King in conventional face cards, 12 representing the Queen, 11 the Jack, and 1 the Ace.

Card Sorting (Suit Order)
-------------------------
Cards are sorted by suit and then subsorted by ascending value within the suit.  The suit order from first to last is clubs, diamonds, hearts, spades.

This file will detail what each file in the code does.

main.py
--------
This file runs the number of games specified by the num_games variable.  It then plots the human player's win fraction.  This is the file you'll run when testing your algorithm.

single_game.py
--------------
The bulk of the game mechanics are in this file.  The comments in the file are pretty good so walk through it for additional details.

Files which might be useful when creating your player algorithm
---------------------------------------------------------------
---------------------------------------------------------------
ai_turn - this is the ai algorithm that you'll be competing against.  It just randomly selects and plays a playable card.

is_valid_play - checks if a card is in the current player's hand and is valid based on the game logic

is_logic_valid_play - checks if a card is valid to play based on the game logic (what cards have been played previouslY)  For example, this function checks to make sure the 7 of hearts has been played before the 8 of hearts.

return_suits - returns the suit order in a list ['clubs', 'diamonds', 'hearts', 'spades'] (I'm using it kind of like a global variable)

win_condition - returns True if any player has 0 cards in his or her hand.

PyCharm Installation
---------------------
If you want an IDE for Python and don't have one, I've found PyCharm Community Edition to be easy to install, free, and a good IDE for python.
