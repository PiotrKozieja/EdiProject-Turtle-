import turtle
import random

mike = turtle.Turtle()
mike.color('green')
turtle.bgcolor('black')
colors = ["purple" , "green" , "orange" , "cyan"]
mike.speed(50)

for i in range(10):
    for i in range(2):
        mike.forward(100)
        mike.right(60)
        mike.forward(100)
        mike.right(120)
    mike.right(36)
    mike.color(random.choice(colors))

turtle.done()



######
###circle
#t = turtle.Turtle()
#  
#  
#r = 50
#t.circle(r)