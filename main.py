import classes as c

# let's create a couple of players
Paul = c.sadiator('Paul', 'Male', 2)
Sadia = c.sadiator('Sadia', 'Female', 2)

sadiators = [Paul, Sadia]

# we need to generate tickets for them
for sadiator in sadiators:
    sadiator.ticket = c.t_gen()

# we should make a 'fight card'
fight_card = []

for sadiator in sadiators:
    if sadiator.ticket == 1:
        fight_card.append(sadiator)
        continue
    if sadiator.ticket == 0:
        sadiator.lucky_days += 1
        continue
