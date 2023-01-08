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
t.speed(10000)
s = turtle.Screen()
color = ["mediumblue","royalblue","blueviolet","violet"]
c1 = random.choice(color)
c2 = random.choice(color)
c3 = random.choice(color)
c4 = random.choice(color)
c5 = random.choice(color)
c6 = random.choice(color)

trefoil(100,color[1],color[1],-400,200,0)
trefoil(100,color[0],color[1],-200,100,20)
trefoil(100,color[3],color[1],0,150,0)
trefoil(150,color[0],color[1],200,200,40)
trefoil(110,color[1],color[1],400,100,0)
trefoil(160,color[3],color[1],0,350,50)
trefoil(100,color[0],color[1],-250,300,10)
#
#####
trefoil(110,color[2],color[2],-200,200,50)
trefoil(70,color[3],color[1],400,200,50)
trefoil(110,color[3],color[1],-100,200,50)
trefoil(130,color[0],color[1],0,300,50)
trefoil(110,color[3],color[1],-400,300,50)
trefoil(110,color[3],color[0],-300,200,40)
trefoil(200,color[3],color[0],200,300,20)
trefoil(180,color[3],color[0],-200,350,50)

####
rhombus(500,color[2],color[1],300,-100,5)
rhombus(300,color[3],color[1],-300,-200,-5)
rhombus(700,color[2],color[0],-100,-100,0)
rhombus(250,color[3],color[1],-100,-350,20)
rhombus(400,color[3],color[1],500,-200,-10)
rhombus(550,color[3],color[0],-400,-150,20)
right(500,color[3],color[0],-100,-700,250)
square(300,color[3],color[0],-100,-400,60)
cross(70,color[3],color[3],208,-10,0)
trefoil(320,color[3],color[1],300,280,50)
name(150,400)




turtle.done()