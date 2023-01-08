import turtle

# utwórz obiekt turtle
t = turtle.Turtle()

# przesuń się do punktu (-200, 200)
t.penup()
t.goto(-200, 200)
t.pendown()

# narysuj kwadrat za pomocą 4 prostych linii
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

# wyświetl rysunek
turtle.done()