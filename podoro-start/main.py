import math
from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# data = pandas.read_csv("quotes.csv")
#
# quotes_dict = {text: name for (text, name) in data.iterrows()}


# print(quotes_dict)
# random_quotes = random.choice(quotes_dict)
# print(random_quotes)


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_text.config(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
    my_check_mark.config(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        my_text.config(text="Break", font=(FONT_NAME, 40, "bold"), fg=RED, bg=YELLOW)
        my_quote.config(text="“Never give up on something you believe in.”\n – Steve Scalise")

    elif reps % 2 == 0:
        count_down(short_break_sec)
        my_text.config(text="Break", font=(FONT_NAME, 40, "bold"), fg=PINK, bg=YELLOW)
        my_quote.config(text="“If you're too open-minded; your brains will fall out.”\n― Lawrence Ferlinghetti")

    else:
        count_down(work_sec)
        my_text.config(text="Work", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
        my_quote.config(text='“The only time you fail is when you fall down and stay down."\n― Stephen Richards')


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        my_check_mark.config(text=marks, font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Study With Takesure")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=2, row=1)

# Label
my_text = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
my_text.grid(column=2, row=0)

# Button
start_button = Button(text="Start", font=(FONT_NAME, 15), bg="white", padx=2, bd=0, command=start_timer)
start_button.grid(column=1, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 15), bg="white", padx=2, bd=0, command=reset_timer)
reset_button.grid(column=3, row=2)

my_check_mark = Label(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
my_check_mark.grid(column=2, row=3)

my_quote = Label(text="")
my_quote.grid(column=2, row=5)

copyrights = Label(text="copyrights © tiripamwepo", font=(FONT_NAME, 10, "italic"), fg=RED, bg=YELLOW)
copyrights.grid(column=2, row=8)
copyrights.config(pady=20)

window.mainloop()
