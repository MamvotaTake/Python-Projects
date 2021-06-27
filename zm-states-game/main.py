import turtle

import pandas

screen = turtle.Screen()
screen.title("Zimbabwean Provinces and  Cities")
image = "zim_cities_map.gif"
screen.addshape(image)
screen.setup(850, 750)
turtle.shape(image)

data = pandas.read_csv("zim_states.csv")
all_cities = data.city.to_list()

guessed_cities = []
while len(guessed_cities) < 26:
    city_answer = screen.textinput(title=f"{len(guessed_cities)}/28 Cities Correct",
                                   prompt="What's the other cities name?").title()

    # if city_answer == "Exit":
    #     missing_cities = []
    #     for city in all_cities:
    #         if city not in guessed_cities:
    #             missing_cities.append(city)
    #     missing_cities_list = pandas.DataFrame(missing_cities)
    #     missing_cities_list.to_csv("missing_cities_list.csv")
    #     break
    if city_answer == "Exit":
        missing_cities = [city for city in all_cities if city not in guessed_cities]
        missing_cities_list = pandas.DataFrame(missing_cities)
        missing_cities_list.to_csv("missing_cities_list.csv")
        break

    if city_answer in all_cities:
        guessed_cities.append(city_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        city_data = data[data.city == city_answer]
        t.goto(int(city_data.x), int(city_data.y))
        t.write(city_answer)

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(-420, -310)
t.color("blue")
t.write("#REGISTERTOVOTE")
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
# screen.exitonclick()
