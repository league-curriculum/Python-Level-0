# Functions

A function is like a recipe, a series of steps that the computer will follow.
But we've been giving the compter steps to follow a long! What is different
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

With a function, we can stop repeatig ourselves. Let's make a function for addition: 

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


Try running this program and see what you get.

{{ trinket("simple_add.py", width="100%", height="600", embed_type="python") | safe }}


Now re-write the program to multiply the two numbers. 


{{ trinket("simple_mult.py", width="100%", height="600", embed_type="python") | safe }}


Re-write it again to multiply three numbers. 


{{ trinket("mult3.py", width="100%", height="600", embed_type="python") | safe }}




Have fun!