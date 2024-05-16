#3) This code shows a class.  The class has a function that knows how to make a star with different segments.
# Can you modify the program to: capture the number of segments and different angles?

import turtle

tina = turtle.Turtle()
tina.shape("turtle")

class my_shape():
  def __init__(self):
	  self.name = "name"
	  self.color = "black"
	  self.segments = 5
	  self.angle = 144
	
  def draw(self):
	  tina.color(self.color)
	  tina.write(self.name)
	  for i in range(0,self.segments):
  	  tina.forward(100)
  	  tina.left(self.angle)

shape = my_shape()
shape.name = raw_input("What shape should I draw?")
shape.color = raw_input("What color?")
#get segments and angle
# write your code here

shape.draw()

