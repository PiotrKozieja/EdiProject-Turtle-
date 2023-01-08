import turtle
x = -100
y = -100
# utwórz obiekt turtle
t = turtle.Turtle()
t.penup()
t.goto(x,y)
t.pendown()
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.goto(x,y)

# wyświetl rysunek
turtle.done()
