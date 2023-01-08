import turtle
import random
from square import square
from trefoil import trefoil
from right import right
from rhombus import rhombus
from square import square
from cross import cross
from IMIELAST import name

t = turtle.Turtle()
s = turtle.Screen()
color = ["mediumblue","royalblue","blueviolet","violet"]
c1 = random.choice(color)
c2 = random.choice(color)
c3 = random.choice(color)
c4 = random.choice(color)
c5 = random.choice(color)
c6 = random.choice(color)
square(100,c1,c2,-400,100,0)
cross(100,c2,c3,-200,100,0)
trefoil(100,c3,c4,0,100,0)
right(100,c4,c5,100,100,0)
rhombus(100,c5,c6,300,100,0)
name(150,400)
turtle.done()

