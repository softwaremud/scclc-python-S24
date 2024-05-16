#Example 2 - Functions can call functions!
# We have 1 function that draws 1 tiny square
# We have another function which repeats the first function!
import turtle
sam = turtle.Turtle()
sam.shape("triangle")

def drawTinySquare(sam):
  sam.pendown()
  for i in range(0,4):
      sam.forward(10)
      sam.left(90)


def drawManySquares(sam, count):
  sam.pendown()
  for i in range(0, count):
      sam.penup()
      sam.forward(25)
      drawTinySquare(sam)

    
drawManySquares(sam, 3)




