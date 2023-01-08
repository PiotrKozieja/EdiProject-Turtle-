import turtle
t = turtle.Turtle()
#t.setpos(1,200)
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("green")
t.speed(0)
#t.goto(1,200)
#t.setpos(1,200)
i = 1

a = 0
b = 0
while True:
    if i ==1:
        t.pencolor("blue")
    else:
        t.pencolor("green")
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    i+=1
    if b == 210:
        break
    t.hideturtle()
    
turtle.done()