import random

# this is the game
def play_game(player1,player2):

    print(f'starting a new game between {player1.name} and {player2.name}')
    # ensure the players don't have a .card value or .rw value
    player1.card = 0
    player2.card = 0
    player1.rw = 0 
    player2.rw = 0
    
    # stalemate == players have equal valued cards
    stalemate = 0 
    
    # tracks total rounds per game
    rounds = 0

    # control flow
    light = False
    
    while not light:

        # give each player a 'card'
        player1.card = random.randint(1,10)
        player2.card = random.randint(1,10)
        print(f'{player1.name} has a {player1.card}')
        print(f'{player2.name} has a {player2.card}')

        # see who has larger value
        if player1.card > player2.card:
            player1.rw += 1
            print(f'{player1.name} = {player1.rw} rounds won')

            rounds += 1

            if player1.rw == 2:
                print(f'{player1.name} wins.')
                player1.wins += 1
                player2.losses += 1

                light = True

        if player2.card > player1.card:
            player2.rw += 1
            print(f'{player2.name} = {player2.rw} rounds won')
            
            rounds += 1

            if player2.rw == 2:
                print(f'{player2.name} wins.')
                player2.wins += 1
                player1.losses += 1

                light = True

        # stalemate
        if player1.card == player2.card:

            stalemate += 1
            rounds += 1

            print(f'players had equal cards...')

    return rounds, stalemate
