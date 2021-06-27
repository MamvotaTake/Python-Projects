import random
from tkinter import *

import pandas
import pyttsx3

BACKGROUND_COLOR = "#B1DDC6"
BLUE_COLOR = "#0054A5"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Learn-Russian.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")

print(to_learn)


def speech():
    engine = pyttsx3.init()

    if radio_state.get() == 1:
        engine.say(current_card["English"])
        engine.runAndWait()
    else:
        engine.say(current_card["French"])
        engine.runAndWait()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Russian", fill="black")
    canvas.itemconfig(card_word, text=current_card["Russian"])
    canvas.itemconfig(card_background_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English / French", fill=BLUE_COLOR)
    canvas.itemconfig(card_word, text=f'{current_card["English"]} / {current_card["French"]}', fill=BLUE_COLOR)
    canvas.itemconfig(card_background_img, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    # score_label.config(title=f"{len(current_card)} / {len(to_learn)}")
    speech()
    next_card()


window = Tk()
window.title("Learn Russian Language")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 35, "bold"))

radio_state = IntVar()
radiobutton1 = Radiobutton(text="English", value=1, fg=BLUE_COLOR, variable=radio_state, command=speech,
                           bg=BACKGROUND_COLOR, font=("Arial", 10, "bold"))
radiobutton2 = Radiobutton(text="French", value=2, fg=BLUE_COLOR, variable=radio_state, command=speech,
                           bg=BACKGROUND_COLOR, font=("Arial", 10, "bold"))
radiobutton1.grid(row=2, column=2)
radiobutton2.grid(row=3, column=2)
# score_label = Label(text="Score", font=("Arial", 20), bg=BACKGROUND_COLOR)
# score_label.grid(row=2, column=2)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

copyrights = Label(text="copyrights © tiripamwepo", font=("Arial", 15), fg=BLUE_COLOR, bg=BACKGROUND_COLOR)
copyrights.grid(column=0, row=4, columnspan=2)
copyrights.config(pady=20)

next_card()

window.mainloop()
