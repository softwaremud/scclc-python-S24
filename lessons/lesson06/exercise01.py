# 1) take the 5 point star we drew last week and incorporate it in a
# function.  Can you modify this program to draw 3 different 5-point 
# stars in different places on the screen?

import turtle

tina = turtle.Turtle()
tina.shape("turtle")

def draw_a_star():  
  for i in range(0,5):
  	tina.forward(200)
  	tina.left(144)
   
tina.penup()  
tina.setx(10)
tina.sety(10)
tina.pendown()
draw_a_star()

tina.penup()  
tina.setx(-100)
tina.sety(-100)
tina.pendown()
draw_a_star()

