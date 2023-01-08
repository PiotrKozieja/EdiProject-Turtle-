import turtle
import random
colors = ["mediumblue","royalblue","blueviolet","violet"]
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
xr = 900
yr=400
t.speed(10)
for i in range(4):
    x= random.randint(-xr,xr)
    y= random.randint(-yr,yr)
    t.color(random.choice(colors))
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.goto(x,y)
for j in range(4):
    x= random.randint(-xr,xr)
    y= random.randint(-yr,yr)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(random.choice(colors))
    for k in range(4):       
        t.forward(100)
        t.right(90)
    
for l in range(4):
    x= random.randint(-xr,xr)
    y= random.randint(-yr,yr)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(random.choice(colors))
    for m in range(4):
        t.forward(60)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(60)
        t.left(90)
t.right(45)        
for n in range(4):   
    x= random.randint(-xr,xr)
    y= random.randint(-yr,yr)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(random.choice(colors))
    for o in range(4):
        t.forward(100)
        t.right(90)
t.left(225)
for p in range(4):
    x= random.randint(-xr,xr)
    y= random.randint(-yr,yr)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(random.choice(colors))
    for i in range(3):
        t.circle(50,240)
        t.right(120)
turtle.done()