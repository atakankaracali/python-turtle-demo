from ipaddress import collapse_addresses
import turtle
import time

w = turtle.Screen()
w.title("Sprial Helix")
w.bgcolor("black")

colors=["red","purple","blue","green","orange","yellow"]

t = turtle.Pen()
t.speed(100)

for x in range(360):
    color = colors[x % len(colors)]
    t.pencolor(color)
    t.width(x / 100+1)
    t.forward(x)
    t.left(59)

turtle.done()
#time.sleep(5)