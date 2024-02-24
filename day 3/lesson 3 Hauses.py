from turtle import *
import turtle as t
import turtle 
import math
speed(500)
width(7)
color("blue")
#we want to draw a house
#step 1 draw a square

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
forward(75)



color("green")

left(90)
forward(115)
right(90)
forward(50)
right(90)
forward(115)
left(90)


color("blue")

forward(75)
left(90)
forward(200)
color("red")
left(50)
forward(130)
left(79)
forward(130)

color("blue")

left(51)
forward(145)
left(90)

penup()
goto(55,70)
pendown()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

penup()
goto(185,70)
pendown()

left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

penup()
goto(-250,0)
pendown()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
forward(75)



color("green")

left(90)
forward(115)
right(90)
forward(50)
right(90)
forward(115)
left(90)


color("blue")

forward(75)
left(90)
forward(200)
color("red")
left(50)
forward(130)
left(79)
forward(130)

color("blue")

left(51)
forward(145)
left(90)

penup()
goto(-65,70)
pendown()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

penup()
goto(-190,70)
pendown()

left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

penup()
goto(0,-300)
pendown()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
forward(75)



color("green")

left(90)
forward(115)
right(90)
forward(50)
right(90)
forward(115)
left(90)


color("blue")

forward(75)
left(90)
forward(200)
color("red")
left(50)
forward(130)
left(79)
forward(130)

color("blue")

left(51)
forward(145)
left(90)

penup()
goto(55,-225)
pendown()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

penup()
goto(185,-225)
pendown()

left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

penup()
goto(280,220)
pendown()

#მზე და ვარსკვლავები
color("yellow")

left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(5)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
left(15)
forward(8)
left(15)
forward(8)
left(15)
forward(8)
left(12)
forward(8)
left(12)
forward(8)
right(10)

penup()
goto(-280,250)
pendown()

#stars

forward(10)
left(180)
forward(5)
left(90)
forward(10)
left(180)
forward(20)

penup()
goto(-320,250)
pendown()

forward(10)
left(180)
forward(5)
left(90)
forward(10)
left(180)
forward(20)

penup()
goto(-360,250)
pendown()

forward(10)
left(180)
forward(5)
left(90)
forward(10)
left(180)
forward(20)

penup()
goto(-220,250)
pendown()

right(90)
forward(10)
left(180)
forward(5)
left(90)
forward(10)
left(180)
forward(20)

penup()
goto(-80,250)
pendown()

right(90)
forward(10)
left(180)
forward(5)
left(90)
forward(10)
left(180)
forward(20)

penup()
goto(-40,250)
pendown()

left(90)
right(90)
forward(10)
left(180)
forward(5)
left(90)
forward(10)
left(180)
forward(20)

penup()
goto(0,250)
pendown()

left(90)
forward(10)
left(180)
forward(5)
left(90)
forward(10)
left(180)
forward(20)

penup()
goto(30,250)
pendown()

left(90)
forward(10)
left(180)
forward(5)
left(90)
forward(10)
left(180)
forward(20)

penup()
goto(160,250)
pendown()

left(90)
forward(10)
left(180)
forward(5)
left(90)
forward(10)
left(180)
forward(20)

penup()
goto(200,250)
pendown()

left(90)
forward(10)
left(180)
forward(5)
left(90)
forward(10)
left(180)
forward(20)

#Garden

color("Black")

penup()
goto(-90,-250)
pendown()

left(91)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

color("green")
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(190)

#Tree
# Function to draw rectangle 
t = turtle.Turtle()

def drawRectangle(t, width, height, color): 
    t.fillcolor(color) 
    t.begin_fill() 
    t.forward(width) 
    t.left(90) 
    t.forward(height) 
    t.left(90) 
    t.forward(width) 
    t.left(90) 
    t.forward(height) 
    t.left(90) 
    t.end_fill() 
  
      
# Function to draw triangle     
def drawTriangle(t, length, color): 
    t.fillcolor(color) 
    t.begin_fill() 
    t.forward(length) 
    t.left(135) 
    t.forward(length / math.sqrt(2)) 
    t.left(90) 
    t.forward(length / math.sqrt(2)) 
    t.left(135) 
    t.end_fill() 
  
# reating turtle object 
tip = turtle.Turtle() 
tip.color ("black") 
tip.shape ("turtle") 
tip.speed (100) 
  
  
# Tree base 
tip.penup() 
tip.goto(-200, -250) 
tip.pendown() 
drawRectangle(tip, 20, 48, "brown") 
  
  
# Tree top 
tip.penup() 
tip.goto(-235, -202) 
tip.pendown() 
drawTriangle(tip, 90, "lightgreen") 
tip.penup() 
tip.goto(-230, -160) 
tip.pendown() 
drawTriangle(tip, 80, "lightgreen") 
tip.penup() 
tip.goto(-224, -120) 
tip.pendown() 
drawTriangle(tip, 70, "lightgreen")
pendown()

# Drawing a 4 hause

#Drawing a Square
penup()
goto(400,150)
pendown()
color("green")
forward(200)
left(270)
forward(200)
left(270)
forward(200)
left(270)
forward(200)
left(270)
forward(200)

#Square
penup()
goto(480,-50)
pendown()
color("red")
left(90)
forward(100)
left(270)
forward(50)
left(270)
forward(100)

# Drawing a Window
penup()
goto(415,45)
pendown()
color("blue")
forward(40)
left(90)
forward(40)
left(90)

forward(40)
left(90)
forward(40)
left(90)

# 2 Window
penup()
goto(550,45)
pendown()

color("blue")
forward(40)
left(90)
forward(40)
left(90)

forward(40)
left(90)
forward(40)
left(90)

#roof

penup()
goto(400,155)
pendown()

color = "red"
left(150)
forward(150)
left(253)
forward(177)

exitonclick()