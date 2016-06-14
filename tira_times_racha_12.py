import random

with open('players.txt', 'r') as f:
    jogadores = f.readlines()

bottom = jogadores[0:3]
meio = jogadores[3:9]
top = jogadores[9:12]

print bottom
print meio
print top

for grupo in (bottom, meio, top):
    random.shuffle(grupo)

for i in range(3):
    print "Time " + str(i+1)
    print bottom[i] + meio[2*i] + meio[2*i+1] + top[i]
