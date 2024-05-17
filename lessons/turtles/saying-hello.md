# Saying Hello

Tina's already said hello but you can tell her your name and she'll say hello to you.

<iframe src="//player.vimeo.com/video/107445354?title=0&amp;byline=0&amp;portrait=0" width="600" height="338" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

First, find the line where Tina says `"Why, hello there!"`.  Next, change it so that she's saying hello to you.  My name is Elliott, so I'd change what she says to `"Why, hello Elliott!"`

```python.run
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

tina.penup()
tina.forward(20)
tina.write("Why, hello there!")
tina.backward(20)

```


The program you wrote above is great for people that have the same name as you, but what if someone has a different name?  We can write a program that asks for your name with the `input` function, so that Tina can get it right for anyone's name.  Run this program and enter your name:

```python.run
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

your_name = input("What's your name?")

tina.penup()
tina.forward(20)
tina.write("Why, hello, " + your_name + "!")
tina.backward(20)
```

The `input` function is what makes the program ask you for your name.  Whatever you type in is then stored in a `variable`.  Tina uses this variable to remember and then say your name!

We can teach Tina to say anything we want using `input`.  Can you add `input` to this program so that anyone who runs it can tell Tina what to say?

```python.run
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

say_what = "What should I say?"

tina.penup()
tina.forward(20)
tina.write(say_what)
tina.backward(20)

```

Hint: the `say_what` variable is what Tina says in this program. How can we use `input` like we did above that the program will ask whoever runs the program what the variable should be?


---

Thanks to Trinket.io for providing this assignment, 
part of their [Hour of Python](https://hourofpython.com/a-visual-introduction-to-python/) 
course.
