import random

class sadiator:
    def __init__(self, name, sex, strength):
        self.name = name
        self.sex = sex
        self.health = 10
        self.strength = strength
        self.xp = 0
        self.ticket = None
        self.lucky_days = 0

# maybe too simple to be its own function but it looks prettier.
# this will generate either 0 or 1
def t_gen():
    return random.randint(0,1)
