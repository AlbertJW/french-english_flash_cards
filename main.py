import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
INDEX = 0

#  import data
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")

word_list = data.to_dict(orient="records")
removed_words = []


#  create button functions
def check_button():
    root.after_cancel(3000)
    word_list.remove(word_list[INDEX])
    new_data = pd.DataFrame(word_list)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global INDEX, flip_timer
    root.after_cancel(flip_timer)
    INDEX = random.randint(0, len(word_list))
    # cross_button["state"] = "disabled"
    # check_button["state"] = "disabled"
    canvas.itemconfig(flash_image, image=flashcard_front)
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=word_list[INDEX]["French"], fill="black")
    # cross_button["state"] = "normal"
    # check_button["state"] = "normal"
    flip_timer = root.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(flash_image, image=flashcard_back)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word_list[INDEX]["English"], fill="white")


#  Window
root = tk.Tk()
root.title("Flashy")
root.resizable(False, False)
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = root.after(3000, func=flip_card)

#  Canvas

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_front = tk.PhotoImage(file="images/card_front.png")
flashcard_back = tk.PhotoImage(file="images/card_back.png")
flash_image = canvas.create_image(400, 263, image=flashcard_front)
lang_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#  Buttons

cross_button = tk.Button(root, command=next_card, highlightthickness=0,
                         bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, borderwidth=0)
cross_image = tk.PhotoImage(file="images/wrong.png")
cross_button.config(image=cross_image, width="100", height="100")
cross_button.grid(column=0, row=1)

check_button = tk.Button(root, command=check_button, highlightthickness=0,
                         bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, borderwidth=0)
check_image = tk.PhotoImage(file="images/right.png")
check_button.config(image=check_image, width="100", height="100")
check_button.grid(column=1, row=1)

next_card()

root.mainloop()
