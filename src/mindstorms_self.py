import turtle

def draw_shapes():
        window = turtle.Screen()
        window.bgcolor("black")

        draw_square()
        draw_circle()
        draw_triangle()

        window.exitonclick()

def draw_square():
        brad = turtle.Turtle()
        brad.shape("turtle")
        brad.color("green")
        brad.speed("slow")

        count = 1
        while(count<5):
            brad.forward(100)
            brad.right(90)
            count = count+1
           
def draw_circle():
        angie=turtle.Turtle()
        angie.shape("arrow")
        angie.color("yellow")
        angie.circle(100)

def draw_triangle():
        tria = turtle.Turtle()
        tria.shape("triangle")
        tria.color("blue")
        tria.left(180)
        i=0
        while(i<3):
            tria.forward(100)
            tria.left(120)
            i = i+1

draw_shapes()
