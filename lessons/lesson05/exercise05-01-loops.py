# Lesson 4 Loops and Functions
# Go to the website: hourofpython.com
# Click on “lowercase challenge”
#  replace the code with the following


import turtle
tina = turtle.Turtle()
tina.shape("turtle")

while True:
  tina.shape("turtle")
  tina.shape("triangle")
  tina.shape("square")

# We can draw something more fun like what will happen if we do this?

while True:
    tina.forward(200)
    tina.left(170)

# But it never stops...  What if we want it to stop?  How about

for i in range(0,10):
    tina.forward(200)
    tina.left(170) 

