Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> import turtle

def move():
  window=turtle.Screen()
  window.bgcolor("red")
  dog=turtle.Turtle()
  for i in range(36):
    dog.speed(50)
    for count in range(4):
      dog.forward(100)
      dog.right(90)
    dog.right(10)

  ani=turtle.Turtle()
  ani.color("blue")
  ani.shape("turtle")
  ani.speed(10)
  ani.circle(100)

  anim=turtle.Turtle()

  anim.color("yellow")
  anim.shape("turtle")
  for i in range(3):
    anim.forward(50)
    anim.left(120)
  window.exitonclick()

move()
