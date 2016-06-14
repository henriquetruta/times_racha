import random

with open('players.txt', 'r') as f:
    jogadores = f.readlines()

bottom = jogadores[0:4]
meio = jogadores[4:12]
top = jogadores[12:16]

print bottom
print meio
print top

for grupo in (bottom, meio, top):
    random.shuffle(grupo)

for i in range(4):
    print "Time " + str(i+1)
    print bottom[i] + meio[2*i] + meio[2*i+1] + top[i]
