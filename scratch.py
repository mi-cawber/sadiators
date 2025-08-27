import classes as c
import pickle

josh = c.sadiator('josh', 'male')

josh.wins = 5


# this writes byte code to file
with open ('saved_data/sadiator_data/josh.txt', 'wb') as f:
    pickle.dump(josh, f)

# this loads the attribute
with open ('saved_data/sadiator_data/josh.txt', 'rb') as f:
    josh_clone = pickle.load(f)


print(josh_clone.wins)
