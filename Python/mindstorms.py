import turtle

def draw_initals(some_turtle):
    some_turtle.left(70)
    some_turtle.forward(200)
    some_turtle.right(140)
    some_turtle.forward(200)
    some_turtle.right(180)
    some_turtle.forward(100)
    some_turtle.left(70)
    some_turtle.forward(70)
    some_turtle.right(180)
    some_turtle.forward(70)
    some_turtle.right(70)
    some_turtle.forward(100)
    some_turtle.left(160)
    some_turtle.forward(190)
    some_turtle.right(90)
    some_turtle.forward(100)
    some_turtle.right(90)
    some_turtle.forward(50)


    


def draw_triangle(some_turtle):
    some_turtle.forward(100)
    some_turtle.right(90)
    some_turtle.forward(100)
    some_turtle.right(135)
    some_turtle.forward(140)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    Alex = turtle.Turtle()
    Alex.shape("turtle")
    Alex.color("green")
    Alex.speed(10)


    draw_initals(Alex)
    #angie = turtle.Turtle()
    #angie.color("yellow")
    #angie.shape("arrow")
    #angie.circle(100)

    #roxy = turtle.Turtle()
    #roxy.color("black")
    #roxy.shape("triangle")
    
    #draw_triangle(roxy)
     
draw_art()
