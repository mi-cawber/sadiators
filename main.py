import classes as c

# let's create a couple of sadiators
Paul = c.sadiator('Paul', 'Male', 2)
Sadia = c.sadiator('Sadia', 'Female', 2)
Klob = c.sadiator('Klob', 'Unknown', 5)
Nugget = c.sadiator('Nugget', 'Male', 2)

sadiators = [Paul, Sadia, Klob, Nugget]

# we need to generate tickets for them
c.ticket_gen(sadiators)

# we should make a 'fight card'
play_card = c.play_card(sadiators)


c.play_game(Paul,Klob)


print(Paul.wins)
