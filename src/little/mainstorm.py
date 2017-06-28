import turtle

# use square to draw a circle
def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    # Create the turtle Brad - Draws a sqaure
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed("slow")
    count = 1
    allCount = 360/10
    while(count<allCount):
        brad.right(10)
        draw_square(brad)
        count=count+1
    window.exitonclick()

draw_art()
