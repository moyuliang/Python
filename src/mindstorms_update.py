import turtle

def draw_square(some_turtle):
        for i in range(1,5):
            some_turtle.forward(100)
            some_turtle.right(90)
        
def draw_art():
        window = turtle.Screen()
        window.bgcolor("black")
        #Create the turtle Brad - Draws a sqaure
        brad = turtle.Turtle()
        brad.shape("turtle")
        brad.color("green")
        brad.speed("slow")
        draw_square(brad)
        #Create the turtle Angie - Draws a circle 
        angie=turtle.Turtle()
        angie.shape("arrow")
        angie.color("yellow")
        angie.circle(100)

        window.exitonclick()

draw_art()
