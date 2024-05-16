Go to http://hourofpython.com / Pick “Number of Things Challenge”  
It’s our last class!
Check out the class (and notes) at: https://github.com/softwaremud/sccl-python-S24

## 1: take the 5 point star we drew last week and incorporate it in a function.  Can you modify this program to draw 3 different 5-point stars in different places on the screen?

```
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
```


## 2: what if we do a while loop to make the turtle move left, but we want them to turn around when they hit the edge of the screen?  How would you handle each of the screen’s 4 sides?

```
import turtle

tina = turtle.Turtle()
tina.shape("turtle")

while True:
  tina.forward(1)
  print(tina.pos())
  if (tina.pos()[0] > 200):
	tina.left(144)
```

## 3: This code shows a class.  The class has a function that knows how to make a star with different segments.

Can you modify the program to: capture the number of segments and different angles?

```
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
```
