# 2) what if we do a while loop to make the turtle move left, but we 
# want them to turn around when they hit the edge of the screen?   
# How would you handle each of the screen’s 4 sides?

import turtle

tina = turtle.Turtle()
tina.shape("turtle")

while True:
  tina.forward(1)
  print(tina.pos())
  if (tina.pos()[0] > 200):
	tina.left(144)

