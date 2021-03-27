import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.25
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.20
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_click():
    window.after_cancel(timer)
    ticker_label.config(text="")
    title_label.config(fg=GREEN, text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_click():
    global REPS
    if REPS == 0:
        start_timer()


def start_timer():
    global REPS
    REPS += 1
    if REPS > 8:
        reset_click()
    elif REPS == 8:
        title_label.config(fg=RED, text="Long Break")
        ticker_label.config(text="Hurray WELL DONE")
        count_down(0, LONG_BREAK_MIN * 60)
    elif REPS % 2 == 1:
        title_label.config(fg=GREEN, text="Work")
        count_down(0, WORK_MIN * 60)
    elif REPS % 2 == 0:
        title_label.config(fg=PINK, text="Short Break")
        ticks = ""
        for _ in range(math.floor(REPS / 2)):
            ticks = ticks + "✔"
        ticker_label.config(text=ticks)
        window.attributes('-topmost', 1) #this brings the wondow to top of screen if it is not minimised
        count_down(0, SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time, max_time):
    if time == max_time:
        start_timer()
    minutes = math.floor(time / 60)
    seconds = math.floor(time % 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    if time < max_time:
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        global timer
        timer = window.after(1000, count_down, time + 1, max_time)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pamodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 39, "bold"))
title_label.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = tkinter.Button(text="Start", command=start_click)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="reset", command=reset_click)
reset_button.grid(row=2, column=2)

ticker_label = tkinter.Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
ticker_label.grid(row=2, column=1)

window.mainloop()
