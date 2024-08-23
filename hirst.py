import colorgram
import random
import turtle 

tim = turtle.Turtle()
tim.hideturtle()
turtle.colormode(255)
list_of_colors = [(235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12)]
dot_count = 100
tim.speed("fastest")
tim.penup()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for i in range(1, dot_count + 1):
    tim.dot(20, random.choice(list_of_colors))
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(55)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle.Screen()
screen.exitonclick()