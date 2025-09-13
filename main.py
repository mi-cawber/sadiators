import classes as c

# create sadiator objects
joshua = c.load_sadiator('joshua')
walt = c.load_sadiator('walt')

# play the game
c.play_game(joshua, walt)

# save the data
c.save_data(joshua)
c.save_data(walt)

with open('wins.txt', 'w') as f:
    f.write(f'Joshua wins: {joshua.wins}\n')
    f.write(f'Walt wins: {walt.wins}\n')
