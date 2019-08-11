import turtle
from random import randint
scr=turtle.Screen()
t=turtle.Turtle()
t.penup()
t.setx(-100)
t.sety(100)
t.pendown()
sides=randint(3, 10)
for i in range(sides):
    t.forward(100)
    t.right(180-(((sides-2)*180)/sides))
scr.exitonclick()
#https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.forward