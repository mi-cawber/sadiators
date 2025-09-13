import classes as c
import game as g

# create sadiator objects
joshua = c.load_sadiator('joshua')
walt = c.load_sadiator('walt')

# play the game
# returns number of rounds and stalemates (players had equal cards)
rounds, stalemates = g.play_game(joshua, walt)

# checks if game set record for highest rounds/stalemates
with open('most_rounds.txt', 'r') as f:
    m_rounds = f.readline()
    m_rounds = int(m_rounds)

with open('most_stalemates.txt', 'r') as f:
    m_stalemates = f.readline()
    m_stalemates = int(m_stalemates)

if rounds > m_rounds:
    with open('most_rounds.txt', 'w') as f:
        f.write(str(rounds))

if stalemates > m_stalemates:
    with open('most_stalemates.txt', 'w') as f:
        f.write(str(stalemates))

# save the data
c.save_data(joshua)
c.save_data(walt)

with open('wins.txt', 'w') as f:
    f.write(f'Joshua wins: {joshua.wins}\n')
    f.write(f'Walt wins: {walt.wins}\n')
