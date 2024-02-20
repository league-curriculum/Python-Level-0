# More Functions

Functions allow code to be executed without copying and pasting the same code
in multiple places. Using functions means writing less code (and therefore
potentially fewer mistakes) and makes the code more maintainable (if there
is an error it only has to be fixed in the function and not in each place
where the code is duplicated).

All functions have the following format:

```python
def <function name>(<input_variable_1>, <input_variable_2>):
```

* 'def' tells the computer the following code is the start of a function
    definition
* \<function name> is the name of the function. This name is used to
    execute the code in the function, also know as calling the function.
* \<input_variable_1> is an input variable. They are optional. There can be
    no input variables or there can be several. If there is more than 1 input
    variable, they're separated by commas.
* '()' open and close parenthesis are always right after the function name.
    If there are any input variables they go between the parenthesis
* ':" the colon is always at the end, just like for, if, elif, and else
  

 ```python.run
def function_1(var1, var2):
    # Only the indented lines of code are executed. Lines that 
    # aren't indented do not get executed when the function 
    # is called.
    print('function_1:')
    print('  var1='+str(var1))
    print('  var2='+str(var2))

def function_2(var1, var2, var3):
    print('function_2:')
    print('  var1='+str(var1))
    print('  var2='+str(var2))
    print('  var3='+str(var3))

function_1('dog', 'cat')
function_2('horse', 'badger', 'mushroom')

```



Any one of the input variables can have default values. These values are
applied when the function is called without a value for the input variable.
Once a default value is set for an input variable all other input variables
that come afterwards must also have default values.

```python.run
def function_3(var1, var2, var3='default value'):
    print('function_3:')
    print('  var1='+str(var1))
    print('  var2='+str(var2))
    print('  var3='+str(var3))

function_3('a','b')

```

A function can return a value with the return keyword. When return is used,
the function ends immediately and no further lines of code are executed. The
returned value can be saved in a variable when the function is called: `return_var = function_4(10)`

```python.run
def function_4(var1):
    print('function_4:')
    print('  var1='+str(var1))

    return var1 * var1 * var1

    # Code after return is not executed
    print('This line is not executed')

r = function_4(3)
print(r)
```


To use a function write the function's name and put the same number of inputs
listed in the function definition. The inputs can either be a value like `1`,
`20.5`, ``"text"`` or a variable.

```python.run


def function_1(var1, var2):
    # Only the indented lines of code are executed. Lines that 
    # aren't indented do not get executed when the function 
    # is called.
    print('function_1:')
    print('  var1='+str(var1))
    print('  var2='+str(var2))

text_variable = 'hello'
function_1(1, text_variable)

# Functions can also be called using the input 
# variable from the function definition. This 
# makes the function call more descriptive. 

# It's possible to only label some of the 
# inputs of a function call, but once an 
# input variable is labeled all the inputs 
# that come after must also be labeled. For 
# example:
#
#function_2(7, var2=8, var3=9)   # works
#function_2(var1=4, var2=5, 6)   # doesn't work

def function_2(var1, var2, var3):
    print()
    print('function_2:')
    print('  var1='+str(var1))
    print('  var2='+str(var2))
    print('  var3='+str(var3))

function_2(var1=1, var2=2, var3=3)


# Calling function_3 with 2 input variables 
# (3rd takes the default value)

def function_3(var1, var2, var3='default value'):
    print()
    print('function_3:')
    print('  var1='+str(var1))
    print('  var2='+str(var2))
    print('  var3='+str(var3))

function_3('one', 'two')

# Calling function_3 with 3 input variables
function_3('one', 'two', 'three')

# Calling function_4 and saving the return 
# value in a variable

def function_4(var1):
    print()
    print('function_4:')
    print('  var1='+str(var1))
    
    return var1 * var1 * var1

return_var = function_4(10)
print('Value returned by function_4 is: ' + str(return_var))

```


Now, you write a program with some functions. You should have a function to do
each of these things:

* Ask the user to enter the user's name,  using `input()`. If the user enters
  no name, change the user's name to 'NoName'. 

* Check if the user's name is "bob" and if it is, print "Hi Bob!"

* Call the first function to get the user's name, then call the second
  function to check it. Call the function using named parameters, like
  the way we called `function_2()`


One of you functions should have a default parameter. 


```python.run:height='600'

# Function to Ask the user to enter the user's 
# name,  using `input()`. If the user enters
# no name, change the user's name to 'NoName'. 

def ...


# Function to check if the user's name is 
# "bob" and if it is, print "Hi Bob!"

def ...


# Function to call the first function to get 
# the user's name, then call the second
# function to check it. Call the function 
# using named parameters, like the way we called `function_2()`



```






