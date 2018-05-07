a = int(input("Nhap chieu dai canh a(10-50):"))
from turtle import*
# test:
# color("black", "red")
# begin_fill()
# circle(80)
# end_fill()

screensize(10000, 10000)
speed(-1)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i, fav in enumerate(colors):
    color(fav, fav)
    begin_fill()
    for i in range(2):
        forward(a)
        left(90)
        forward(2 * a)
        left(90)
    end_fill()
    penup()
    forward(a)
    pendown()

mainloop()
