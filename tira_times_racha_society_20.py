import random

with open('players.txt', 'r') as f:
    jogadores = f.readlines()

bottom = jogadores[0:3]
meio = jogadores[3:12]
top = jogadores[12:15]
print bottom
print meio
print top

for grupo in (bottom, meio, top):
    random.shuffle(grupo)

for i in range(3):
    print "Time "
    print bottom[i] + meio[3*i] + meio[3*i+1] + meio[3*i+2] + top[i]
