from ipaddress import collapse_addresses
import turtle
import time

col=["yellow","red","white","orange","blue","green"]

t = turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("black")
t.speed(30)

for i in range(200):
    t.color(col[i%6])
    t.forward(i*4)
    t.left(150)
    t.width(2)
time.sleep(5)