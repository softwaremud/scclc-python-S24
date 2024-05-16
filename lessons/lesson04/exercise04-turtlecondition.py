#  Bonus Turtle Program:
#  Challenge 1: what does this program do?
#  Challenge 2: can you modify this program to allow a user to draw a square?
#  Challenge 3: Can you modify this program to allow the user to draw a hexagon 
#               (6 sides, 60 degrees each)

import turtle

options = {
  "1" : "triangle",
  "2" : "rectangle"
}

t = turtle.Turtle()
print("What shape would you like to draw?")
shapeInput= input(options)



if shapeInput == "1":
  print("Lets draw a "+ options[shapeInput])
  # draw a triangle
  t.forward(100)
  t.left(120)
  t.forward(100)
  t.left(120)
  t.forward(100)
  t.left(120)
elif shapeInput == "2":
  print("Lets draw a "+ options[shapeInput])
 
  # draw a rectangle
  t.forward(50)
  t.left(90)
  t.forward(100)
  t.left(90)
  t.forward(50)
  t.left(90)
  t.forward(100)
 
else:
  print("sorry i don’t know how to draw a " + str(shapeInput))



