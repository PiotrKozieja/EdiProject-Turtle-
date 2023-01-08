import turtle
xp = -500 ###bylo 400
yp = 350  #### bylo 350
xk = 0
yk = 350
t = turtle.Turtle()
s = turtle.Screen()
t.pensize(5)
t.speed(2)
s.bgcolor("black")
t.pencolor("blue")
t.penup()
t.speed(200)
t.setpos(xp,yp)
#######litera p
t.pendown()
t.forward(220)
t.circle(-50,180)
t.forward(100)  ###########odstep 80px
t.penup()       #############yp -170 stala dolna linia
t.goto(xp+100,yp)
t.pendown()
t.left(90)
t.forward(170)
t.penup()
t.setpos(xp+180,yp-170)   ####170 bylo
############litera i
t.pendown()
t.right(180)
t.forward(50)
t.penup()
t.setpos(xp+285,yp-145) ### do o wiec nie mierzyc 
t.pendown()
t.circle(25,360)
t.penup()
t.setpos(xp+340,yp-170)
t.pendown()
t.forward(170)
t.penup()
#########kreska od t
t.goto(xp+310,yp-90)
t.pendown()
t.right(90)
t.forward(60)
#####r
t.penup()
t.goto(xp+390,yp-170)   ##xp bylo
t.left(90)
t.pendown()
t.forward(50)
t.penup()
t.goto(xp+390,yp-140)
t.pendown()
t.circle(-20,90)
t.forward(50)
t.penup()
t.goto(xp,yp)
#t.penup()
#t.goto(xp+100, yp-190)
#t.pendown()
#t.forward(360)
###############Piotr^^^^########
#####k
t.penup()
t.goto(xk, yk)
t.pendown()
t.right(90)
t.forward(170)
t.penup()
t.goto(xk,yk-120) #100
t.pendown()
t.goto(xk+80,yk-170)
t.penup()
t.goto(xk,yk-120) ###100 
t.pendown()
t.goto(xk+80,yk)
t.penup()
######o
t.goto(xk+100,yk-147)
t.pendown()
t.circle(25,360)
t.penup()
#####z
t.goto(xk+180,yk-120)
t.pendown()
t.left(90)
t.forward(50)
t.goto(xk+180,yk-170)
t.forward(50)
t.penup()
####i
t.goto(xk+260,yk-170)
t.pendown()
t.left(90)
t.forward(50)
t.penup()
####e
t.goto(xk+330,yk-170)
t.pendown()
t.goto(xk+320,yk-170)
t.pendown()
t.left(90)
t.circle(-25,180)
t.circle(-12,180)
t.forward(25)
t.penup()
###j
t.goto(xk+365,yk-120)
t.pendown()
t.left(90)
t.forward(90)
t.circle(-12,270)
t.forward(100)
t.left(90)
t.penup()
####a
t.goto(xk+420,yk-170)
t.right(90)
t.pendown()
t.circle(25,360)
t.penup()
t.goto(xk+446,yk-120)
t.right(90)
t.pendown()
t.forward(50)
t.penup()
####kropki nad i, j
t.goto(xk+260,yk-100)
t.left(90)
t.pendown()
t.circle(1,360)
t.penup()

###j
t.goto(xk+365,yk-100)
t.pendown()
t.left(90)
t.circle(1,360)






turtle.done()
