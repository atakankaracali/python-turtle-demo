import imp
from turtle import *
import time
speed(10.2)
color('cyan')
title("COVID")
bgcolor('black')
b = 200
while b > 0:
    left(b)
    forward(b*3)
    b = b-1
time.sleep(5)    