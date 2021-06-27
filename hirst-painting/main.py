# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

import random
# print(rgb_colors)
import turtle as t

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     my_colors = (r, g, b)
#     return my_colors

tim.penup()
tim.hideturtle()
color_list = [(250, 248, 242), (241, 242, 246), (239, 249, 244), (249, 241, 246), (229, 215, 105), (148, 82, 43),
              (204, 160, 99), (113, 165, 208), (176, 176, 24), (33, 92, 157), (110, 176, 127), (13, 36, 92),
              (191, 92, 106), (68, 42, 24), (191, 139, 151), (54, 120, 28), (96, 186, 53), (194, 92, 74), (106, 33, 55),
              (180, 206, 168), (26, 95, 26), (102, 121, 168), (247, 169, 173), (26, 54, 110), (244, 173, 162),
              (156, 190, 237), (139, 82, 92), (75, 31, 45), (100, 61, 21), (107, 49, 26)]

tim.setheading(225)
tim.fd(300)

tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(30, random.choice(color_list))
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)

screen.exitonclick()
