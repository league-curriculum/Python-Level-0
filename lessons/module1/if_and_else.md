# Making Choices with If and Else

All programming languages have a way of making choices, doing one thing or
the other. In Python we can make choices with `if`, `elif` and `else`. Here is
a simple program to tell you if a number is bigger than 10:

```python.run


while True: # This loop will run until the 'break'

    num = input("Enter a number:")
    num = int(num) # Make the input an integer

    if num == 0:
        break # Exit the loop if the number is 0
    
    if num > 10:
        print("It's big!")
    else:
        print("It's small")


```

Let's use the if statement to write a program to greet your friend. You might
want to look at earlier programs for clues 

```python.run

# Make a list of your friends, by adding 
# on to this starter list

friends = [ 'friend1','friend2']

# Ask the user's name
name = ...

# Write a loop that iterates over all of your 
# friends, and if the user's name is the same 
# as a friends name, print "Hello Friend"

for friend in ... :
    ...


```

