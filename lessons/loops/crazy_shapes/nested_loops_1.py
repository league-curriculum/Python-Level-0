import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)

left = 20

for i in range(6):
  for forward in range(-50,50,10):
    tina.forward(forward)
    tina.left(left)