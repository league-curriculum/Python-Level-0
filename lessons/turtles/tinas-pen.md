# Tina's Pen

Turtles like Tina have a pen that draws when they move.  We can tell them to pick the pen up, so that they can move without drawing a line.  Then we can tell them to put the pen down, and they'll draw again.  We tell them this with the `penup()` and `pendown()` commands.

```python.run
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

tina.penup()
tina.goto(0,100)

tina.write("I don't draw when my pen is up!")

tina.goto(0,50)
tina.pendown()

tina.write("I do draw when my pen is down!")

tina.goto(-50,50)
```


---

Thanks to Trinket.io for providing this assignment, 
part of their [Hour of Python](https://hourofpython.com/a-visual-introduction-to-python/) 
course.