# Iterating over Iterables

Here is the first simple list that you learned about earlier. 

```python 
things_to_buy = [ 'apples','oranges','bread','milk']
```

This variable, `things_to_buy` is interesting, because it is a list of
strings, but the strings are also a list, a list of letters. And in Python, 
lists and strings are a lot a like. So, let's learn more about them both. 

Both lists and strings are "iterables". Iteration means taking things one at a
time, and "iterating" a list means that we will get the first thing in the
list, then the second, and on, until there is nothing left in the list. We have
seen iteration before, with loops. Here are two loops, 
one iterating over a list, and another iterating over a string. 


```python.run


things_to_buy = [ 'apples','oranges','bread','milk']

print("Things to buy:")
for things in things_to_buy:
    print(things)

print("\nLetters in a string")
for letter in "Hello!":
    print(letter)

# Now change the program so that, in the second loop, 
# the program prints an 'x' instead of an 'l'

```

## Iterables

The for loop, which looks like `for <variable> in <iterable>` works by taking each one of the 
things in the iterable, assigning it to the variable, then running the code in the body
of the loop. 

But, then you wonder, what does the code we first used for loops do? The one with `range()`
in it?

Well, `range()` is an iterable!. But it isn't a string or a list. It doesn't have anything in it. 
It just gives you the next number. But, we can turn it into a list that does have things in it. Here is
how: 

```python.run

# Turn a range() into a list:

l = list(range(5, 10))
print(l)

```

::: tip 
The reason that range() is not a list is that if you had a big range, like range(1_000_000_000), 
Python would have to store a billion numbers, and would run out of memory. But range() doesn't actually store all of those numebrs, it just counts up by 1, so it doesn't take a lot of memory )
:::


Then you put something inside `list()`, list will try to iterate the thing, and then take each 
item and put it into a list. A string, like 'Hello World' is not a list, but we can turn it into 
a list. 


```python.run

# Turn a stringinto a list:

l = list("Hello World!")
print(l)

```

You can turn a string into a list. The first way breaks the list into letters ( which programmers call "characters". The second way breaks the list at a specific character. 

```python.run

# A list of letters
l = list('adefibhgc')
print(l)

# split a string at the comma character
s = 'One,Two,Three,Four'
l = s.split(',')


```

## Sorting

Wait, those letters are out of order. Let's put them back in order. There are two ways: 

```python.run

l = list('adefibhgc')
l.sort()
print(l)
print()

l = list('adefibhgc')
l = sorted(l)
print(l)
```

## Adding To Lists

You can add items to lists with `.append()`, and concatenate lists ( put them
together) with `+`:

```python.run

l = []

l.append('item 1')
l.append('item 2')
l.append('item 3')

l  = l + ['item 4', 'item 5']

print(l)


# Try adding more items to the list!

```

# Show Us Your Lists!

Now, you can write a program. Here is what your program should do. 

* Start with a string that has friend names, with spaces between the friend names, like
this, but with real names: `'foo bar baz'`. Split the list into a string.
* Ask the user for new friend names three times, and add those names to the list
* Sort the list
* Print out each name on a seperate line. 


```python.run:height='600'

```










