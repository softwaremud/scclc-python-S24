# From the last exercises, we can incorporate lists! 
#  what does the following code do?

import turtle
tina = turtle.Turtle()
tina.shape("turtle")

colors = ["red","blue","yellow", "orange","black","pink"]
for i in range(0,5):
	tina.color(colors[i])
	tina.forward(200)
	tina.left(170)

