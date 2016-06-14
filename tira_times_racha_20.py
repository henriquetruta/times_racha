import random

with open('players.txt', 'r') as f:
    jogadores = f.readlines()

bottom = jogadores[0:4]
meio = jogadores[4:16]
top = jogadores[16:20]

print bottom
print meio
print top

for grupo in (bottom, meio, top):
    random.shuffle(grupo)

for i in range(4):
    print "Time " + str(i+1)
    print bottom[i] + meio[3*i] + meio[3*i+1] + meio[3*i+2] + top[i]
