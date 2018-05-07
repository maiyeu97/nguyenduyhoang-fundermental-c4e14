from turtle import*

def draw_square(colors, length):
    color(colors)
    for i in range(4):
        forward(length)
        left(90)
draw_square("red", 200)
mainloop()
