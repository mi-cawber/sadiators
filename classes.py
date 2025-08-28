import random, pickle, os

class sadiator:
    def __init__(self, name):

        #demographic stuff
        self.name = name

        #play-related stuff
        self.wins = 0
        self.losses = 0
        self.card = 0 # for in-game
        self.rw = 0 # 'rounds won', for in-game
        
        # create save file
        self.create_save_file()

    # creates save file for sadiator
    def create_save_file(self):
        if not os.path.exists(f'/home/joshua/sadiators/saved_data/{self.name}.pkl'):
            with open(f'saved_data/sadiator_data/{self.name}.pkl', 'w'): 
                pass # null operation?

# function for saving sadiator attributes to file
def save_data(sadiator):
    # save data
    with open(f'/home/joshua/sadiators/saved_data/{sadiator.name}.pkl', 'wb') as f:
        pickle.dump(sadiator, f)

# function for loading sadiator attributes to file
def load_data(path):
    # load data
    with open(path, 'rb') as f:
        return pickle.load(f)

# actually restores the load data
def load_sadiator(name):
    return load_data(f'/home/joshua/sadiators/saved_data/{name}.pkl')

# this is the main mechanisms
def play_game(player1,player2):

    print(f'starting a new game between {player1.name} and {player2.name}')
    # ensure the players don't have a .card value or .rw value
    player1.card = 0
    player2.card = 0
    player1.rw = 0 
    player2.rw = 0

    # control flow
    light = False
    
    while not light:

        # give each player a 'card'
        # value is between 1-10
        player1.card = random.randint(1,10)
        player2.card = random.randint(1,10)
        print(f'{player1.name} has a {player1.card}')
        print(f'{player2.name} has a {player2.card}')

        # this block is to see whose value is bigger
        # see if player 1 has higher value
        if player1.card > player2.card:
            player1.rw += 1
            print(f'{player1.name} = {player1.rw} rounds won')

            # check for win condition
            if player1.rw == 2:
                print(f'{player1.name} wins.')
                player1.wins += 1
                player2.losses += 1

                # stop iterating
                light = True
                break

            continue # if win condition not met, continue

        # see if player 2 has higher value
        if player2.card > player1.card:
            player2.rw += 1
            print(f'{player2.name} = {player2.rw} rounds won')

            # check for win condition
            if player2.rw == 2:
                print(f'{player2.name} wins.')
                player2.wins += 1
                player1.losses += 1

                # stop iterating
                light = True
                break

            continue # if win condition not met, continue

        # if the cards are equal, move one
        if player1.card == player2.card:
            print(f'players had equal cards...')
            continue
