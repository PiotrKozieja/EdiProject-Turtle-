def trefoil(a,b,c,d,e,f):
    #a rozmiar
    #b kolor lini
    #c kolor tla
    #d wspolrzedna x
    #e wspolrzedna y
    #f kat rysowania
    import turtle
    t = turtle.Turtle()
    ####
    t.speed(100)
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
    for i in range(3):
      t.circle(a/3,240)
      t.right(120)
    t.end_fill()
    t.penup()
    t.goto(-1000,-1000)

