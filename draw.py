import turtle
turtle.home()

#Make functions here bcuz python is dumb
def makeBackground():
    turtle.color("green")
    turtle.dot(500)

def makeSeedPod():
    turtle.color("yellow")
    turtle.dot(100)
def makeMark():
    color = turtle.color()
    turtle.color("red")
    turtle.dot(20)
    turtle.color('black')
#begin cooking
turtle.color("green")
turtle.dot(1250)

turtle.goto(-500,100)
turtle.color("blue")
turtle.begin_fill()
turtle.fillcolor("blue")
turtle.setheading(0)
turtle.forward(1000)
turtle.setheading(90)
turtle.forward(300)
turtle.setheading(180)
turtle.forward(1000)
turtle.setheading(270)
turtle.forward(300)
turtle.end_fill()

turtle.goto(-400,400)
turtle.color("yellow")
turtle.dot(300)
turtle.penup()

turtle.home()
turtle.pendown()
turtle.color("black")
turtle.pensize(10)
turtle.setheading(270)
turtle.forward(300)
turtle.pensize(1)

turtle.home()
def makePedal(scale,heading):
    turtle.setheading(heading)
    turtle.color("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(200 * scale,90 )
    makeMark()
    turtle.color("white")
    turtle.circle(20 * scale,90)
    makeMark()
    turtle.color("white")
    turtle.circle(200 * scale,90)
    makeMark()
    turtle.color("white")
    turtle.circle(20 * scale,90)
    makeMark()
    turtle.color("white")
    turtle.end_fill()

def makeFlower():
    for i in range(6):
        makePedal(.5,60 * i + 3 )

    turtle.home()
    turtle.color("red")
    turtle.dot(50)

makeFlower()



#wrap up drawing
turtle.hideturtle()
turtle.exitonclick()

