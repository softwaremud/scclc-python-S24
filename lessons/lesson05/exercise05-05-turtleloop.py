# Example 1 Draw a square function!

import turtle
sam = turtle.Turtle()
sam.shape("square")

def drawASquare(sam):
  sam.pendown()
  for i in range(0,4):
      sam.forward(40)
      sam.left(90)

    
drawASquare(sam)

sam.penup()
sam.forward(150)
sam.pendown()

drawASquare(sam)

