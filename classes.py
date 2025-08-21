import random

class sadiator:
    def __init__(self, name, sex, age = 20):

        #demographic stuff
        self.name = name
        self.sex = sex
        self.age = age

        #play-related stuff
        self.ticket = None
        self.lucky_days = 0
        self.xp = 0
        self.wins = 0
        self.losses = 0
        self.level = 1
        self.card = 0
        #for in-game
        self.rw = 0

# maybe too simple to be its own function but it looks prettier.
# this will generate either 0 or 1
def ticket_gen(sadiators):

    for sadiator in sadiators:
        sadiator.ticket = random.randint(0,1)

def play_card(sadiators):
    #make empty card
    play_card = []

    for sadiator in sadiators:
        if sadiator.ticket == 1:
            play_card.append(sadiator)
            continue
        if sadiator.ticket == 0:
            sadiator.lucky_days += 1
            continue

    return play_card

# this is the main mechanisms
def play_game(player1,player2):

    #ensure the players don't have a .card value or .rw value
    player1.card = 0
    player2.card = 0
    player1.rw = 0 
    player2.rw = 0

    #control flow
    light = False
    
    while not light:

        #give each player a 'card'
        player1.card = random.randint(1,10)
        player2.card = random.randint(1,10)

        #this block is to see whose value is bigger
        if player1.card > player2.card:
            player1.rw += 1
            
            #check for win condition
            if player1.rw == 2:
                player1.wins += 1
                player2.losses += 1
                light = True
                break

            continue

        if player2.card > player1.card:
            player2.rw += 1
            
            #check for win condition
            if player2.rw == 2:
                player2.wins += 1
                player1.losses += 1
                light = True
                break

            continue

        if player1.card == player2.card:
            continue







