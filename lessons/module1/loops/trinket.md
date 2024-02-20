# Loops for Easy Squares

Here is how some students solve the last exercise, using variables to draw a square. 

```python
import turtle
tina = turtle.Turtle()
tina.shape("turtle")

forward = 50
left = 90

tina.forward(forward)
tina.left(left)

tina.forward(forward)
tina.left(left)

tina.forward(forward)
tina.left(left)

tina.forward(forward)
tina.left(left)

```


Notice that there is a lot of repetition in this program. Can we make this
program shorter by getting rid of the repetition? Yes, we can, with loops.  A
loop is a bit of code that causes the computer to do something multiple
times. Here is a loop for printing "Hello!" mutiple times. How many times do
you think it will print?

```python.run

for i in range(4):
    print("Hello!")

# Now change the program to make 
# it print hello 6 times. 
```

Let's look at that in more detail:

```python
for i in range(4):
    print("Hello!")
```

The first line in the loop defines the loop and tells us how many times to do
the body of the loop. The body of the loop, the ` print("Hello!")` part,  is
indented. The ``range`` part will run the number of times inside the
parenthesis, in this case 4. 

The `i` part is also special; it is a variable. So, you could print it out too. 

```python
for i in range(4):
    print("Hello!", i)
```



## Make a Better Square. 

Here is our way of solving the square exercise. Can you edit this
program to make it much better, by replacing the repetition with a loop?

```python.run
import turtle
tina = turtle.Turtle()
tina.shape("turtle")

forward = 50
left = 90

tina.forward(forward)
tina.left(left)

tina.forward(forward)
tina.left(left)

tina.forward(forward)
tina.left(left)

tina.forward(forward)
tina.left(left)
```

Once you have used a loop to help Tony make a square, try making other shapes,
like a triangle, a pentagon, or a hexagon, or maybe even a ... hendecagon.
(if you can figure out what that is. )


## Badgers Badgers Badgers

Use for loops (you will need more than one) to print the following lyrics from the Badger Song. You can only use the words “Badger”, “Mushroom” and “Snake” once each in your code.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pzagBTcYsYQ?si=m3Vc66lQ4PhMfiFO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Print 2 verses of the song as follows:

```
Badger, Badger, Badger, Badger, Badger, Badger, Badger,Badger, 
Badger,Badger, Badger, Badger, Mushroom, Mushroom

Badger, Badger, Badger,Badger, Badger, Badger, Badger,Badger, 
Badger, Badger, Badger, Badger, Mushroom, Mushroom

A Snake!!!
```

Or maybe: 🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🍄🍄 🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🍄🍄 🐍



```python.run:height='600'

```




## More about range

Another interesting things with the loops is that `range` can have more than
one number in it. If we put in two numbers, the values of `i` will go from
the first number to _one minus_ the second number, so if you want to print
out the numbers 4, 5, 6, 7, you would use `range(4,8)`:


```python 
for i in range(4, 7):
    print("Hello!", i)
```

Try that yourself. Write a program to print "Hello" next to all of the
numbers from 10 to 20:

```python.run
# Change me to print Hello for the 
# numbers from 10 to 20

for i in range(4):
    print("Hello!")
```

But there are more interesting things about `range()`: It can take a _third_
number, and all three of the numbers can be negative or positive. So you
could also type `range(10,20, 2)` or `range(20,10,-1)`. Let's explore `range
()` to figure out what the third number does. 

```python.run

# Change me so range() has three numbers, 
# and try to figure out what the third
# number does. What happens if you make 
# some of the numbers negative?

# HINT: If the third number is negative, 
# the first number should be *bigger* than
# the second, but if the third number is positive, 
# it should be smaller. 

for i in range(10):
    print("Hello!", i)
```
