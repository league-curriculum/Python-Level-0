# Shapes and Colors

Here is the program we created to make squares with loops. Try modifying this 
program to make other shapes. Try some of these things:

* Change the number of sides
* Change the angle the turtle turns ( the `left` variable )
  * Try numbers that are even sections of a cirle, like 60, 45, 90 or 40
  * Try numbers that aren't even seconds of a circle, like 172 or 43


```python.run
import turtle 
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)

forward = 50
left = 90
sides = 4

def side(turtle, forward, left):
  turtle.forward(forward)
  turtle.left(left)

for i in range(sides):
  side(tina, forward, left)
```

Here are some more ideas for you. You can put a loop inside a loop! Try this
program. 

```python.run
import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)

left = 20

for i in range(6):
  for forward in range(-50,50,10):
    tina.forward(forward)
    tina.left(left)
```

Here is another crazy program: 


```python.run
import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)

forward = 50


def side(turtle, forward, left):
  turtle.forward(forward)
  turtle.left(left)


def make_shape(turtle, forward, left, sides):
  for i in range(sides):
    side(turtle, forward, left)

for sides in range(4, 9):
  left = 360 / sides
  make_shape(tina, forward, left, sides)
```

Now try creating your own crazy progam. This time, you will start from an empty
file, so copy parts from other programs to get started. 

```python.run:height='600'

```


Now we can get to writing a more complex program. Use what you know about Tina the Turtle from previous programs, and what you've just learned about loops to write the program below. Read the comments for hints about what you should do. 

```python.run
import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new 
# name for the turtle
my_turtle = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')

# Set your turtle's speed using .speed(2)

# Set your turtle's color using .color('green') 
# and .pencolor('blue')

# Move your turtle forward using .forward(100)
# TEST    Did your turtle move forward?

# Move your turtle left or right using .left(90) 
# or .right(90)

# Now put the forward and left/right code into a for 
# loop to repeat 4 times.
# TEST    Did your turtle draw a square?

# Move your turtle to a new place on the 
# screen using .goto(x, y) x=0 and y=0 is the 
# center of the screen

# Have your turtle draw a circle using 
# .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?

# Add color to your shape by adding .begin_fill() 
# before drawing the circle
# and .end_fill() below

# Draw 3 more shapes with different fill colors!

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
```



