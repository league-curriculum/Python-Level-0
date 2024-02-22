# Level 0 Project

For your final Level 0 project, you are going to learn the most important lesson
that a programmer can learn:

<p style="text-align: center; font-size: 40px; font-weight: bold; color: red; font-family: 'Comic Sans MS', cursive, sans-serif;">Read The Documentation!</p>


We've been using the Python turtle for all this time, but we haven't read the documentation yet! 

So, for this project, you are going to get to read the documentation to write a new program
that uses some turtle features that we haven't learned yet. 

Your assignment for this project to make a turtle program that draws something, maybe a picture, like a cake or a house, or a ninja start, or a crazy shape. But, your program should also have: 

* a list
* a tuple
* a loop that uses zip
* a loop that uses range

You should also try to include an `if/else` in your program, and ask for input with `input()`


But first, visit the [Python Turtle Library Documentation](https://docs.python.org/3/library/turtle.html)
to see if there is anything you'd like to try. You should especially look at [The Graphics Methods](https://docs.python.org/3/library/turtle.html#turtle-graphics-reference) to see if there are any functions that look interesting, like `stamp()`.


```python.run:height=800

```

Here are some hints with interesting programs that you can study for ideas:

::: details Crazy Turtle Walk
```python
import turtle
tina = turtle.Turtle()
tina.shape("classic")
tina.speed(1000)


moves = [ 50, 100, -100, 40, 70, -45]
turns = ( 90, -45,  0,   90,  -35, 7 )
colors = [ 'red','blue','green',
           'orange','black','yellow' ]

def move_turtle(move, turn, color):
    turtle.color(color)
    turtle.forward(move)
    turtle.left(turn)


for i in range(10):
  for move, turn, color in zip(moves, turns, colors):
      move_turtle(move, turn, color)
  turtle.right(15)

```
:::

::: details Flaming Ninja Star
```python
import random
import turtle

# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["red", "blue", "green", "yellow", "orange"]

def getNextColor(i):
    return colors[i % len(colors)]

window = turtle.Screen()

baseSize = 150  # the size of the black part of the star
flameSize = 80  # the length of the flaming arms

t = turtle.Turtle()
t.shape("turtle")
t.width(2) 
t.speed(0)  


for i in range(25):

    t.pencolor(getRandomColor())
    t.fillcolor(getRandomColor())  

    t.begin_fill()

    t.right(360 / 8) 
    t.forward(64)

    t.left(40) 

    t.forward(flameSize)
    t.right(170) 
    t.forward(flameSize)
    t.right(62) 
    t.forward(baseSize) 

    t.end_fill()

t.hideturtle() # Hide your turtle so you can see the pattern.
```
:::


::: details Yin Yang Program
```python 
from turtle import *

# This program is different because we didn't create a turtle first. The
# command here are for the "default turtle"

def yin(radius, color1, color2):
    width(3)
    color("black")
    fill(True)
    circle(radius/2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius/2., 180)
    color(color1)
    fill(True)
    color(color2)
    left(90)
    up()
    forward(radius*0.375)
    right(90)
    down()
    circle(radius*0.125)
    left(90)
    fill(False)
    up()
    backward(radius*0.375)
    down()
    left(90)

def main():
    reset()
    yin(200, "white", "black")
    yin(200, "black", "white")
    ht()
    return "Done!"


main()
```
:::



