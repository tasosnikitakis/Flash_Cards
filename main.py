#----------------------------------------IMPORTS AND CONSTANTS---------------------------------------
from tkinter import *
from tkinter import messagebox
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
import random
import time


KNOWN_WORDS = -1
UNKNOWN_WORDS = 0
to_learn_data = []
foreign_word = ""
local_word = ""

try:
    pandas_data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    pandas_data = pd.read_csv("data/french_words.csv")
dictionary_data = pandas_data.to_dict(orient="records")
#-----------------------------------------CLOSE FUNCTION-------------------------------------
def close_program():
    window.destroy()

#-----------------------------------------FLASH CARD GENERATOR-------------------------------------
def card_generator():
    global KNOWN_WORDS
    global foreign_word
    global local_word
    global flip_timer
    global to_learn_data
    window.after_cancel(flip_timer)
    KNOWN_WORDS += 1
    try:
        random_pair = random.choice(dictionary_data)
        foreign_word = random_pair["French"]
        local_word = random_pair["English"]
        label_known.config(text=f"Unknown Words: {KNOWN_WORDS}")
        canvas.itemconfig(language_text, text="French", fill="black")
        canvas.itemconfig(card_image, image=card_front_image)
        canvas.itemconfig(word_text, text=f"{foreign_word}", fill="black")
        dictionary_data.remove(random_pair)
        flip_timer = window.after(5000, func=flip_card)
    except IndexError:
        messagebox.showinfo(title="Τέλος Άσκησης", message="Πάτα ΟΚ για έξοδο")
        close_program()
    return local_word, foreign_word, KNOWN_WORDS


#-----------------------------------------FLASH CARD REMOVER-------------------------------------
def card_remover():
    global UNKNOWN_WORDS
    global foreign_word
    global local_word
    global flip_timer
    window.after_cancel(flip_timer)
    UNKNOWN_WORDS += 1
    random_pair = random.choice(dictionary_data)
    foreign_word = random_pair["French"]
    local_word = random_pair["English"]
    label_unknown.config(text=f"Unknown Words: {UNKNOWN_WORDS}")
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(word_text, text=f"{foreign_word}", fill="black")
    flip_timer = window.after(5000, func=flip_card)
    to_learn_data.append(random_pair)
    dictionary_data.remove(random_pair)
    pandas_to_learn = pd.DataFrame(to_learn_data)
    pandas_to_learn.to_csv("data/words_to_learn.csv", index=0)
    return local_word, foreign_word, UNKNOWN_WORDS


#------------------------------------------------------FLIP MECHANISM--------------------------
def flip_card():
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{local_word}", fill="white")


#----------------------------------------GUI SETUP----------------------------------------------
#window setup
window = Tk()
window.title("Flash Cards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
flip_timer = window.after(5000, func=flip_card)


#images
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

label_known = Label(text=f"Known Words: {KNOWN_WORDS}", bg=BACKGROUND_COLOR, font=("Arial", 14, "bold"))
label_unknown = Label(text=f"Unknown Words: {UNKNOWN_WORDS}", bg=BACKGROUND_COLOR, font=("Arial", 14, "bold"))
label_known.grid(column=0, row=2)
label_unknown.grid(column=1, row=2)


#canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)
language_text = canvas.create_text(400, 150, text="language", fill="black", font=("Arial", 24, "italic"))
word_text = canvas.create_text(400, 263, text="word", fill="black", font=("Arial", 60, "bold"))


#buttons
Right_Button = Button(image=right_image, highlightthickness=0, command=card_generator)
Right_Button.grid(column=0, row=1)
Wrong_Button = Button(image=wrong_image, highlightthickness=0, command=card_remover)
Wrong_Button.grid(column=1, row=1)


card_generator()

window.mainloop()