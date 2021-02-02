import turtle
n=int(input("請問你想畫幾邊形"))
alex=turtle.Turtle()
for i in range(n):
    alex.forward(100)
    alex.left(360/n)
