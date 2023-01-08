import turtle
def name(xp,yp):
    t = turtle.Turtle()
    s = turtle.Screen()
    t.speed(100)
    t.pensize(2)
    t.speed(2)
    s.bgcolor("black")
    t.pencolor("violet")
    t.penup()
    t.speed(200)
    t.setpos(xp,yp)
    t.left(90)
    #ZZISS1-1112
    #xp+30,yp -100
    #z
    t.goto(xp+30,yp -70)
    t.pendown()
    t.right(90)
    t.forward(20)
    t.goto(xp+30,yp -100)
    t.forward(20)
    t.penup()
    #z
    t.left(90)
    t.goto(xp+60,yp -70)
    t.pendown()
    t.right(90)
    t.forward(20)
    t.goto(xp+60,yp -100)
    t.forward(20)
    t.penup()
    #i
    
    t.goto(xp+95,yp-100)
    t.pendown()
    t.left(90)
    t.forward(30)
    t.penup()
    

    #s
    t.goto(xp+107,yp-70)
    t.pendown()
    t.left(270)
    t.forward(10)
    t.circle(-7,180)
    t.forward(2)
    t.circle(8,180)
    t.forward(10)
    t.penup()

    #s
    t.goto(xp+137,yp-70)
    t.right(270)
    t.pendown()
    t.left(270)
    t.forward(10)
    t.circle(-7,180)
    t.forward(2)
    t.circle(8,180)
    t.forward(10)
    t.penup()
    t.goto(100,100)

    #1
    t.goto(xp+165,yp-75)
    t.pendown()
    t.goto(xp+165+10,yp-70)
    t.right(90)
    t.forward(30)
    t.penup()
    t.goto(100,100)

    #-
    t.goto(xp+190,yp-85)
    t.left(90)
    t.pendown()
    t.forward(30)
    t.penup()

    #1
    t.goto(xp+230,yp-75)
    t.pendown()
    t.goto(xp+230+10,yp-70)
    t.right(90)
    t.forward(30)
    t.penup()
    t.goto(100,100)

    #1
    t.goto(xp+250,yp-75)
    t.pendown()
    t.goto(xp+250+10,yp-70)
    t.forward(30)
    t.penup()
    t.goto(100,100)


    #1
    t.goto(xp+270,yp-75)
    t.pendown()
    t.goto(xp+270+10,yp-70)
    t.forward(30)
    t.penup()
    t.goto(100,100) 
    t.penup()


    #2
    t.goto(xp+290,yp-80)
    t.right(180)
    t.pendown()
    t.circle(-10,250)
    t.goto(xp+290,yp-100)
    t.goto(xp+310,yp-100)
    t.penup()
    t.goto(100,100)
    











name(-400,350)
turtle.done()