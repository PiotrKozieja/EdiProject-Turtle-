import turtle
t = turtle.Turtle()
s = turtle.Screen()
def right(a,b,c,d,e,f):
    #a rozmiar
    #b kolor lini
    #c kolor tla
    #d wspolrzedna x
    #e wspolrzedna y
    #f kat rysowania
    import turtle
    t = turtle.Turtle()
    t.speed(10)
    s = turtle.Screen()
    s.bgcolor("black")
    t.penup()
    t.pensize(5)
    t.goto(d,e)
    t.pendown()
    t.color(b)
    t.fillcolor(c)
    t.right(f)
    t.begin_fill()
    t.penup()
    t.goto(d,e)
    t.pendown()
    t.right(90)
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.goto(d,e)
    t.end_fill()

