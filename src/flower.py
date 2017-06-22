import turtle

# Draws a diamond
def draw_Diamond(some_turtle):
    for i in range(1, 3):
        some_turtle.forward(50)
        some_turtle.right(50)
        some_turtle.forward(50)
        some_turtle.right(130)

# Draws a flower
def draw_flower():
    window = turtle.Screen()
    window.bgcolor("black")
    # Draws a diamond
    tria = turtle.Turtle()
    tria.shape("turtle")
    tria.color("yellow")
    tria.speed(9)
    for i in range(1,37):
        tria.right(10)
        draw_Diamond(tria)
    tria.right(90)
    tria.forward(150)
    window.exitonclick()

draw_flower()
