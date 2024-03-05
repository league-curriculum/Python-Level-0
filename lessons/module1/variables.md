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

```python.run

# Make the numbers add to 15

x = 10
y =   # Finish the line with the right string

assert x + y == 15, "The sum should be 15"

print("Yeah! 🎉")
```


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

```python.run

# Make the numbers add to 15

x = "Hello "
y =   # Finish the line with the right number

assert x + y == "Hello World"
print("Yeah! "+x+y+" 🎉")

```

One important things about strings is that you have to surround them with quotes, but
you can use single or double quotes. The reason is that if you string has one kind of
quote, it has to be surrounded with the other kind. 

```python

s1 = "this is a string"
s2 = 'this is also a string'

s3 = "He said 'this is a string' "
s4 = 'He said "this is a string" '
```

This string program doesn't work! change it so it does. 


```python.run

s1 = like strings
s2 = these letters are in bob's string

s3 = Bob said "I really like strings"
s4 = Bob 'likes' strings

print(s1)
print(s2)
print(s3)
print(s4)

```


But, sometimes, even using two kinds of strings doesn't work well, like if you 
have a string that has both kinds of quotes in it, like:

```
I can't decide if I like " or ' more
```

What do you do then? You can "escape" the quotes with a '\\', which turns off
the quotes quotiness. So you'd type this: 


```python 
s = "I can\'t decide if I like \" or \' more"
```



# Turtle Variables

We can use variables to store commands for our turtle. Let's start with a program that we created 
earlier, but update it to use variables. 

```python.run


import turtle
tina = turtle.Turtle()
tina.shape("turtle")

forward = # Amount to move forward
left = # amount to turn left


# In the lines below, use the variables 
# instead of numbers. 

tina.forward(50)
tina.left(90)

tina.forward(50)
tina.left(90)

tina.forward(50)
tina.left(90)

tina.forward(50)
tina.left(90)

# Now, try changing the values for 
# forward and left and see what new 
# shapes Tina draws. 
```

