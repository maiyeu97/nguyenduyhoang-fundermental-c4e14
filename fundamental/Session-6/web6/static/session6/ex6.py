from turtle import *

def draw_star(x, y, length):
    pos()
    (x, y)
    for i in range(5):
        forward(length)
        right(144)
        forward(length)
speed(-1)
color('red')
for i in range(1000):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(100, 200)
    draw_star(x, y, length)
mainloop()
