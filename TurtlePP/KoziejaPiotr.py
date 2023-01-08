import turtle
import random

############# CROSS ###############################

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

########### NAME and GROUP ###################

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
    ###p
    t.pendown()
    t.forward(50)
    t.circle(-15,180)
    t.forward(15)
    t.penup()
    t.goto(xp+30,yp)
    t.left(90)
    t.pendown()
    t.forward(50)
    t.penup()
    #i
    t.setpos(xp+50,yp-50)
    t.pendown()
    t.right(180)
    t.forward(15)
    t.penup()
    #o
    t.goto(xp+70,yp-50)
    t.pendown()
    t.right(90)
    t.circle(7,360)
    t.penup()
    #t
    t.goto(xp+90,yp-50)
    t.left(90)
    t.pendown()
    t.forward(50)
    t.penup()
    t.goto(xp+80,yp-25)
    t.right(90)
    t.pendown()
    t.forward(20)
    t.penup()
    ###r
    t.goto(xp+105,yp-50)
    t.left(90)
    t.pendown()
    t.forward(15)
    #r
    t.goto(xp+105,yp-40)
    t.circle(-5,90)
    t.forward(5)
    t.penup()
    t.goto(xp+135,yp-50)
    t.pendown()
    t.left(90)
    t.forward(50)
    t.goto(xp+135,yp-30)
    t.right(90)
    t.circle(-15,90)
    t.forward(5)
    t.penup()
    t.goto(xp+135,yp-30)
    t.pendown()
    t.goto(xp+150,yp)
    t.penup()
    t.goto(xp+165,yp-50)
    t.right(270)
    t.pendown()
    t.circle(7,360)
    t.penup()
    t.goto(xp+180,yp-35)
    t.pendown()
    t.forward(15)
    t.goto(xp+180,yp-50)
    t.forward(15)
    t.penup()
    t.goto(xp+208,yp-50)
    t.left(90)
    t.pendown()
    t.forward(15)
    t.penup()
    t.goto(xp+209,yp-30)
    t.pendown()
    t.circle(1,360)
    t.penup()
    #e
    t.goto(xp+225,yp-50)
    t.pendown()
    t.left(90)
    t.circle(-7,180)
    t.circle(-3,180)
    t.forward(5)
    t.penup()
    ######j
    t.goto(xp+240,yp-35)
    t.left(90)
    t.pendown()
    t.forward(27)
    t.circle(-4,270)
    t.forward(30)
    t.penup()
    t.goto(xp+240,yp-30)
    t.pendown()
    t.circle(1,360)
    t.penup()
    t.goto(xp+255,yp-50)
    t.pendown()
    t.circle(7,360)
    t.penup()
    t.goto(xp+264,yp-50)
    t.left(90)
    t.pendown()
    t.forward(15)
    t.penup()
    
    #ZZISS1-1112
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
    t.penup()
    t.goto(-1000,-1000)
  
############### RHOMBUS ########################

def rhombus(a,b,c,d,e,f):

    #a rozmiar
    #b kolor lini
    #c kolor tla
    #d wspolrzedna x
    #e wspolrzedna y
    #f kat rysowania
    t = turtle.Turtle()
    t.speed(1000)
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
    t.right(45)
    for i in range(4):
        t.forward(a)
        t.right(90)
    t.end_fill()
    t.penup()
    t.goto(-1000,-1000)

############### SQUARE ################

def square(a,b,c,d,e,f):
    
    #a rozmiar
    #b kolor lini
    #c kolor tla
    #d wspolrzedna x
    #e wspolrzedna y
    #f kat rysowania
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
    t.penup()
    t.goto(-1000,-1000)

################ TREFOIL ############

def trefoil(a,b,c,d,e,f):
    #a rozmiar
    #b kolor lini
    #c kolor tla
    #d wspolrzedna x
    #e wspolrzedna y
    #f kat rysowania
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


################# RIGHT ################

def right(a,b,c,d,e,f):
    #a rozmiar
    #b kolor lini
    #c kolor tla
    #d wspolrzedna x
    #e wspolrzedna y
    #f kat rysowania
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
    t.penup()
    t.goto(-1000,-1000)


############### PAINTING ################
for i in range(1):
    t = turtle.Turtle()
    t.speed(10000)
    s = turtle.Screen()
    color = ["mediumblue","royalblue","blueviolet","violet"]
    c1 = random.choice(color)
    c2 = random.choice(color)
    c3 = random.choice(color)
    c4 = random.choice(color)
    c5 = random.choice(color)
    c6 = random.choice(color)

    trefoil(100,color[1],color[1],-400,200,0)
    trefoil(100,color[0],color[1],-200,100,20)
    trefoil(100,color[3],color[1],0,150,0)
    trefoil(150,color[0],color[1],200,200,40)
    trefoil(110,color[1],color[1],400,100,0)
    trefoil(160,color[3],color[1],0,350,50)
    trefoil(100,color[0],color[1],-250,300,10)
    #
    #####
    trefoil(110,color[2],color[2],-200,200,50)
    trefoil(70,color[3],color[1],400,200,50)
    trefoil(110,color[3],color[1],-100,200,50)
    trefoil(130,color[0],color[1],0,300,50)
    trefoil(110,color[3],color[1],-400,300,50)
    trefoil(110,color[3],color[0],-300,200,40)
    trefoil(200,color[3],color[0],200,300,20)
    trefoil(180,color[3],color[0],-200,350,50)

    ####
    rhombus(500,color[2],color[1],300,-100,5)
    rhombus(300,color[3],color[1],-300,-200,-5)
    rhombus(700,color[2],color[0],-100,-100,0)
    rhombus(250,color[3],color[1],-100,-350,20)
    rhombus(400,color[3],color[1],500,-200,-10)
    rhombus(550,color[3],color[0],-400,-150,20)
    right(500,color[3],color[0],-100,-700,250)
    square(300,color[3],color[0],-100,-400,60)
    cross(70,color[3],color[3],208,-10,0)
    trefoil(320,color[3],color[1],300,280,50)
    name(150,400)

turtle.done()