import turtle

#Example 3 - Functions can call functions!
# We have 1 function that draws 1 tiny square
# We have another function which repeats the first function!
sam = turtle.Turtle()
sam.shape("triangle")
sam.penup()
sam.forward(-100)

def drawAShape(sam, numSides):
  sam.pendown()
  if numSides < 3:
      sam.write("i don't know how to draw a shape with " + numSides)
  else:
    length = 250 / numSides
    angle = 360 / numSides
    for i in range(0,numSides):
      sam.forward(length)
      sam.left(angle)
 
#draw a triangle
drawAShape(sam, 3)

sam.penup()
sam.forward(50)

#draw a pentagon
drawAShape(sam, 5)


sam.penup()
sam.forward(50)

#draw a octagon
drawAShape(sam, 8)

