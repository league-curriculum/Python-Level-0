# Going in Circles

Tina can make circles of different sizes.  Circles make it easy to make funny faces:

```python.run
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

tina.penup()
tina.goto(30,-150)
tina.pendown()

tina.circle(130)

tina.penup()
tina.goto(0,0)
tina.pendown()

tina.circle(20)
tina.circle(10)

tina.penup()
tina.forward(60)
tina.right(45)
tina.pendown()

tina.circle(30)
tina.circle(10)

tina.penup()
tina.right(90)
tina.forward(90)
tina.pendown()

tina.circle(40)

tina.penup()
tina.goto(25,-25)
```

Can you make more funny faces in this image?

Turtles can also `fill` in circles with colors, which can be very helpful for drawing.

```python.run
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

tina.penup()
tina.begin_fill()
tina.color('green')
tina.goto(30,-150)
tina.pendown()

tina.circle(130)

tina.penup()
tina.end_fill()
tina.color('white')
tina.goto(0,0)
tina.begin_fill()
tina.pendown()

tina.circle(20)

tina.penup()
tina.end_fill()
tina.begin_fill()
tina.color('black')
tina.pendown()

tina.circle(10)

tina.penup()
tina.end_fill()
tina.forward(60)
tina.right(45)
tina.begin_fill()
tina.color('white')
tina.pendown()

tina.circle(30)

tina.penup()
tina.end_fill()
tina.begin_fill()
tina.color('black')
tina.pendown()

tina.circle(10)

tina.penup()
tina.end_fill()
tina.right(90)
tina.forward(90)
tina.begin_fill()
tina.color('maroon')
tina.pendown()

tina.circle(40)

tina.penup()
tina.end_fill()
tina.goto(25,-25)
```
---

Thanks to Trinket.io for providing this assignment, 
part of their [Hour of Python](https://hourofpython.com/a-visual-introduction-to-python/) 
course.