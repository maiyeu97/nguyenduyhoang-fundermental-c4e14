from turtle import*

def draw_square(colors, length):
    color(colors)
    for i in range(4):
        forward(length)
        left(90)
def draw_square(colors):
    for i in range(30):
        draw_square(i * 5, 'red')
        left(17)
        penup()
        forward(i * 2)
        pendown()
mainloop()
