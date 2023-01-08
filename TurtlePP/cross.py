import turtle
t = turtle.Turtle()
s = turtle.Screen()
def cross(a,b,c,d,e,f):
    #a rozmiar
    #b kolor lini
    #c kolor tla
    #d wspolrzedna x
    #e wspolrzedna y
    #f kat rysowania
    a1 = a/4
    a2 = a/4*3/2
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
    for i in range(4):  
        t.forward(a2)
        t.right(90)
        t.forward(a1)
        t.right(90)
        t.forward(a2)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(-600,600)

