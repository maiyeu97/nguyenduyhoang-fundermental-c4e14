from turtle import*
width(6)
screensize(1000,1000)
n = int(input("nhap so:"))
for i in range(n):
     if i% 2 == 0:
         color('green')
         forward(100)
     else:
         color('red')
         forward(100)
mainloop()
