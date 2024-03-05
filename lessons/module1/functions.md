# Functions

A function is like a recipe, a series of steps that the computer will follow.
But we've been giving the compter steps to follow all along! What is different
about a function? The important thing about functions is that they have
names, inputs, and outputs.

Let's imagine that you have this program to add two numbers:

```python 
a = 10
b = 20
c = a + b
print(c)
```

It works! But what if you want to add more than once? You'd have to write something like: 

```python 
a = 10
b = 20
c = a + b
print(c)

a = 5
b = 6
c = a + b
print(c)

```

With a function, we can stop repeating ourselves. Let's make a function for addition: 

```python
def add(a, b):
	c = a + b
	return c

print(add(10,20))
print(add(5,6))
```

Notice that the important part of the addition procedure is now inside the
function. The `def` keyword says that we are going to *def*ine a fuction, and the
variables in the parentheses, `(a,b)` are called the _argument list_. Those are the inputs to 
the function. 

The last line, `return c` is the output from the function. That is the value that we want to print. 

Notice that you've already seen functions, we've been using them all along. Here is
part of the first program we made:

```python
tina = turtle.Turtle()
tina.shape('turtle')
```


Try running this program and see what you get.

```python.run
def add(a, b):
	c = a + b
	return c

print(add(10,20))
print(add(5,6))
```

Now re-write the program to multiply the two numbers. 

```python.run
# Change me to multiply! Be sure to change the
# name of the function. 
def add(a, b):
	c = a + b
	return c

print(add(10,20))
print(add(5,6))
```

You can have a different number of arguments for the input to the function.
Re-write it again to multiply three numbers. 


```python.run
# Change me to multiply, and make it multiply three numbers!
# Be sure to change the name of the function. 
def add(a, b):
	c = a + b
	return c

print(add(10,20))
print(add(5,6))

```

## Make Five Cakes

Earlier we talked about how **functions are like recipes**. In this exercise,
we've already taught Tina the recipe for making a picture of a cake and she's
made three.  Tell her to make more cakes by **calling** the function with
different `x` and `y` locations at the very bottom of the program.  

How many cakes should she make?

```python.run
import turtle
tina=turtle.Turtle()
tina.shape('turtle')

def make_cake(x=0, y=0):
    tina.penup()
    tina.color('pink')
    tina.goto(x, y)
    tina.pendown()
    tina.begin_fill()
    tina.goto(x + 20, y)
    tina.goto(x + 20, y + 20)
    tina.goto(x - 20, y + 20)
    tina.goto(x - 20, y)
    tina.goto(x, y)  
    tina.end_fill()
    tina.goto(x, y + 20)
    tina.color('yellow')
    tina.goto(x, y + 35)
    tina.goto(x, y + 30)
    tina.color('black')
    tina.goto(x, y + 20)
    tina.penup()
    tina.goto(x, y + 10)
    
make_cake(0,0)
make_cake(-100,0)
make_cake(100,0)

```

Hint: The first number in `make_cake()` is **how far left or right** Tina should go, while the second is **how high or low** she should go before starting to draw.

Run this program, then change the program how ever you want. Some things you can try: 
* Change the colors of the cakes
* Make the cakes bigger
* Put the cakes in different places
* Use a loop to make more cakes

## Functions and Loops

Let's update a square function one more time. This time remove the redundancy in
the program with a loop, but also use a function; your loop should run a
function many times, and the function should draw part of the square. 

```python.run
import turtle
tina = turtle.Turtle()
tina.shape("turtle")

forward = 50
left = 90

# First, write a function that performs
# the important part of the code below. 
# Be sure to include the correct arguments
# for the variables. 

# Second, call that function from a loop
# to do it the right number of times. 


tina.forward(forward)
tina.left(left)

tina.forward(forward)
tina.left(left)

tina.forward(forward)
tina.left(left)

tina.forward(forward)
tina.left(left)
```

When your program is correctly drawing a square, try changing the 
variable to see what other shapes you can make. 


---

Thanks to Trinket.io for providing the 5 cakes assignment, part of their
[Hour of Python] (https://hourofpython.com/a-visual-introduction-to-python/) course.


