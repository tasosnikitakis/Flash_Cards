#----------------------------------------IMPORTS AND CONSTANTS---------------------------------------
from tkinter import *
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
import random




#-----------------------------------------FLASH CARD GENERATOR-------------------------------------


pandas_data = pd.read_csv("data/french_words.csv")
dictionary_data = pandas_data.to_dict(orient="records")
def card_generator():
    random_pair = random.choice(dictionary_data)
    foreign_word = random_pair["French"]
    local_translation = random_pair["English"]
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(word_text, text=f"{foreign_word}")




#----------------------------------------GUI SETUP----------------------------------------------
#window setup
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#images
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")


#canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)
language_text = canvas.create_text(400, 150, text="language", fill="black", font=("Arial", 24, "italic"))
word_text = canvas.create_text(400, 263, text="word", fill="black", font=("Arial", 60, "bold"))


#buttons
Right_Button = Button(image=right_image, highlightthickness=0, command=card_generator)
Right_Button.grid(column=0, row=1)
Wrong_Button = Button(image=wrong_image, highlightthickness=0, command=card_generator)
Wrong_Button.grid(column=1, row=1)










window.mainloop()