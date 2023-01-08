import turtle

# utwórz obiekt Turtle
t = turtle.Turtle()

# ustaw szybkość rysowania
t.speed(10)

# ustaw pozycję początkową
t.penup()
t.goto(-100, 0)
t.pendown()

# narysuj krzyż
for i in range(4):
    t.forward(60)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(60)
    t.left(90)

# zakończ program
turtle.done()