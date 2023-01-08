import turtle
t = turtle.Turtle()
s = turtle.Screen()

def square(a,b,c,d,e,f):
    #a rozmiar
    #b kolor lini
    #c kolor tla
    #d wspolrzedna x
    #e wspolrzedna y
    #f kat rysowania
    import turtle
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor("black")
    t.penup()
    t.pensize(5)
    t.goto(d,e)
    t.pendown()
    t.color(b)
    t.fillcolor(c)
    t.right(f)
    #######
    t.speed(10)

    t.begin_fill()
    ########
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.left(90)
    t.end_fill()

#square(100,"blue","orange",-100,100,20)