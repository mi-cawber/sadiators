import functions as f

# create sadiator objects
joshua = f.load_character('joshua')
walt = f.load_character('walt')

# play the game
# returns number of rounds and stalemates (players had equal cards)
rounds, stalemates = g.play_game(joshua, walt)

# checks if game set record for highest rounds/stalemates
with open('/home/joshua/sadiators/most_rounds.txt', 'r') as r:
    m_rounds = r.readline()
    m_rounds = int(m_rounds)

with open('/home/joshua/sadiators/most_stalemates.txt', 'r') as r:
    m_stalemates = r.readline()
    m_stalemates = int(m_stalemates)

if rounds > m_rounds:
    with open('/home/joshua/sadiators/most_rounds.txt', 'w') as w:
        w.write(str(rounds))

if stalemates > m_stalemates:
    with open('/home/joshua/sadiators/most_stalemates.txt', 'w') as w:
        w.write(str(stalemates))

# save the data
f.save_data(joshua)
f.save_data(walt)

with open('/home/joshua/sadiators/wins.txt', 'w') as w:
    w.write(f'Joshua wins: {joshua.wins}\n')
    w.write(f'Walt wins: {walt.wins}\n')
