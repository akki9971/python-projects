
import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)

n = 80
h = 0

while 1:
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1 / n
    t.color(c)
    t.left(30)
    t.forward(20)
    t.right(45)
    t.forward(10)