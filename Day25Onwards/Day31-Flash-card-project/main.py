import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


# ---------------------------Flip card--------------------------------#

def flip_card():
    global current_card
    canvas.itemconfig(card_title, text='English',fill="White")
    canvas.itemconfig(card_word, text=f"{current_card['English']}",fill="White")
    canvas.itemconfig(card_background,image=card_back_img)


# -----------------Window Setup and Main Code---------------------------#
window = tkinter.Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer=window.after(3000, func=flip_card)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file="./images/card_front.png")
card_back_img = tkinter.PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

# ---------------------------Handling data from the csv--------------#
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data =pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")
#print(to_learn)


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card)
    canvas.itemconfig(card_title, text="French",fill="Black")
    canvas.itemconfig(card_word, text=current_card['French'],fill="Black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer = window.after(3000,func=flip_card)


# -----------------------is_known Deletion ---------------------------#
def is_known():
    global current_card
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv",index=False)
    next_card()



# ---------------------------unknown button ---------------------------#
cross_image = tkinter.PhotoImage(file="./images/wrong.png")
unknown_button = tkinter.Button(image=cross_image, highlightthickness=0, command=next_card,bd=0)
unknown_button.grid(row=1, column=0)

# ---------------------------known button ---------------------------#
tick_image = tkinter.PhotoImage(file="./images/right.png")
known_button = tkinter.Button(image=tick_image, highlightthickness=0, command=is_known,bd=0)
known_button.grid(row=1, column=1)

# ---------------------------mainloop end ---------------------------#
next_card()

window.mainloop()
