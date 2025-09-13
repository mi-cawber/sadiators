import pickle, os

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

