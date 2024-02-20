# Variables

A variable is a way to store information, like a box where you can put
something for using later. Variables have names, which is like a label on the
box. You can set or change change the contents of the box with the '=',
which we call the 'assignment operator'.

Here is an examples of assigning a variable: 

```python
tony = turtle.Turtle()
```

Surprise! You've been using variables all along! Here the name of the variable 
is `tony` and the contents of the variable, like the contents of a box, is a turtle. 


Here are some more examples, storing numnbers into variables 

```python
apples = 10
oranges = 6
```

How many fruits do we have? We can add them: 

```python 
print(apples+oranges)
16
```

Since variables can hold numbers, and we can add numbers, so we can add the variables to get the answer. 

Try it yourself. But first, notice the last line, which has `assert` on it, which means, 
'complain if this is not true'. The assert will produce an error message if
 your variables don't add to 15.  Make the variables add to 15 to make the
 `assert` happy, then try making it unhappy by making them add to any other
 number, just to see whan an error looks like. We will sometimes use `assert`
 to check if your answers are correct. 

{{ trinket("variables_int.py", width="100%", height="250", embed_type="python") | safe }}


We've already seen addition, but we can also subtract, multiply and divide.
However, multiplication and division use symbols that are a little different
from what you are used to:

* Multiplication uses "*", so `10*5 == 50`
* Division uses "/", so `50/5 == 10`

For instance: 

```python 
pizza_slices = 16
people = 4
pizza_per_person = pizza_slices / 4

assert pizza_per_person == 4 # What is this????

```

## Strings

In Python, there are many different types of things we can put in the
variable, including numbers and words, which we will call "text"
or "strings".

It might seem weird that words are called "strings" but it's not if you think
about it like a computer, which is that it is made of letters, one after the other, like a friendship bracelet. 

<img src="https://i.pinimg.com/originals/86/47/ce/8647ce37cd76a5188c04be03d8969ad5.jpg" alt="Friendship Bracelet" width="200"/>

Strings work a bit differently than numbers; when we add them, they are _concatenated_ which means "combined end to end"

```python 
h = "Hello"
s = " "
w = "World"
print(h+s+w)
Hello World
```

Now, try the same thing we did with numbers, but with strings: 

{{ trinket("variables_str.py", width="100%", height="250", embed_type="python") | safe }}


We can use variables to store commands for our turtle. Let's start with a program that we created 
earlier, but update it to use variables. 

{{ trinket("turtle_var.py", width="100%", height="500", embed_type="python") | safe }}