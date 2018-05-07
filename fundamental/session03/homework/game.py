import random

power = ['battery', 'correct', 'horse', 'staple', 'victory', 'professional']
system = random.SystemRandom()
fav = system.choice(power)
# print(fav)
Transgender1 = list(fav)
# print (Transgender1)
random.shuffle(Transgender1,random.random)
# print(Transgender1)
title = ''.join(map(str, Transgender1))
print("Sort the word into the correct word!")
print(title)
fav1 = str(fav)
aswer = fav1
aswer = True
while True:
    aswer = str(input("Answer:"))
    if aswer != fav1:
        print("Try again:")
    else:
        print("Bingo")
        break
