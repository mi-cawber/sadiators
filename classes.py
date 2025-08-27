import random, pickle, os

class sadiator:
    def __init__(self, name, sex):

        #demographic stuff
        self.name = name
        self.sex = sex

        #play-related stuff
        self.wins = 0
        self.losses = 0
        self.card = 0 # for in-game
        self.rw = 0 # 'rounds won', for in-game
        
        # create save file
        self.create_save_file()

    # creates save file for sadiator
    def create_save_file(self):
        if not os.path.exists(f'saved_data/sadiator_data/{self.name}.txt'):
            with open(f'saved_data/sadiator_data/{self.name}.txt', 'w'): 
                pass # null operation?

# function for saving sadiator attributes to file
def save_data(sadiator):
    # save data
    with open(f'saved_data/sadiator_data/{sadiator.name}.txt', 'wb') as f:
        pickle.dump(sadiator, f)

# function for loading sadiator attributes to file
def load_data(sadiator):
    # load data
    with open(f'saved_data/sadiator_data/{sadiator.name}.txt', 'rb') as f:
        pickle.load(sadiator, f)

# this is the main mechanisms
def play_game(player1,player2):

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

        # this block is to see whose value is bigger
        # see if player 1 has higher value
        if player1.card > player2.card:
            player1.rw += 1
            continue

        # check for win condition
        if player1.rw == 2:
            player1.wins += 1
            player2.losses += 1

            # stop iterating
            light = True
            break

        # see if player 2 has higher value
        if player2.card > player1.card:
            player2.rw += 1
            continue

        # check for win condition
        if player2.rw == 2:
            player2.wins += 1
            player1.losses += 1

            # stop iterating
            light = True
            break

        # if the cards are equal, move one
        if player1.card == player2.card:
            continue
    
    # save sadiator data
    save_data(player1)
    save_data(player2)
