import turtle
tina = turtle.Turtle()
tina.shape('turtle')

your_name = input("What's your name?")

tina.penup()
tina.forward(20)
tina.write("Why, hello, " + your_name + "!")
tina.backward(20)
