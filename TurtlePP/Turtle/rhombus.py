import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("green")
#########
t.right(45)
for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()