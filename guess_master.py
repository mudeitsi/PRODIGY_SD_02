from tkinter import *
import random

# Create a new window
window = Tk()

# Set the dimensions of the created window
window.geometry("600x400")

# Set the background color of the window
window.config(bg="#6761a8")

window.resizable(width=False, height=False)

# Set Window Title
window.title('GuessMaster Guessing Game')

# Left Frame and its contents (Moved to top-left)
leftFrame = Frame(window, width=200, height=400)
leftFrame.grid(row=0, column=0, padx=10, pady=2, sticky="nw")

Label(leftFrame, text="Instructions:").grid(row=0, column=0, padx=10, pady=2)

Instruct = Label(leftFrame, text="1 Click on Play Game to start\n2. Guess a number.\n")
Instruct.grid(row=1, column=0, padx=10, pady=2)

try:
    imageEx = PhotoImage(file='image.gif')
    Label(leftFrame, image=imageEx).grid(row=2, column=0, padx=10, pady=2)
except:
    print("Image not found")

# Right Frame and its contents (Moved to far right)
rightFrame = Frame(window, width=200, height=400)
rightFrame.grid(row=0, column=1, padx=10, pady=2, sticky="ne")

# Configure column weights for both frames
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# Existing components in the right label
title = Label(rightFrame, text="GuessMaster", font=("Quantum Sans Serif", 24), fg="#fffcbd", bg="#065569")
title.grid(row=0, column=0, padx=10, pady=2)

result = Label(rightFrame, text="Click on Play Game to start a new game",
               font=("Raleway", 12, "normal", "italic"), fg="White", bg="#065569", justify=LEFT)
result.grid(row=1, column=0, padx=10, pady=2)

circleCanvas = Canvas(rightFrame, width=100, height=100, bg='white')
circleCanvas.grid(row=2, column=0, padx=10, pady=2)

btnFrame = Frame(rightFrame, width=200, height=200)
btnFrame.grid(row=3, column=0, padx=10, pady=2)

colorLog = Text(rightFrame, width=30, height=10, takefocus=0)
colorLog.grid(row=4, column=0, padx=10, pady=2)


TARGET = random.randint(0, 100)
RETRIES = 0

def update_result(text):
    result.configure(text=text)

def new_game():
    global TARGET, RETRIES
    TARGET = random.randint(0, 100)
    RETRIES = 0
    update_result(text="I am thinking of a number between\n 1 and 100")

def play_game():
    global RETRIES

    choice = int(number_form.get())

    if choice != TARGET:
        RETRIES += 1

        result = "Wrong Guess!! Try Again"
        hint = "The number is more than {}" if TARGET > choice else "The number is less than {}"
        result += "\n\nHINT:\n" + hint.format(choice)

    else:
        result = "You guessed right after {} retries".format(RETRIES)
        guess_button.configure(state='disabled')
        result += "\n" + "Click on Play Game to start a new game"

    update_result(result)

# Play Button
play_button = Button(window, text="Play Game", font=("Raleway", 14, "bold"), fg="Black", bg="white", command=new_game)
play_button.place(x=10, y=320)

# Exit Button
exit_button = Button(window, text="Exit Game", font=("Raleway", 14), fg="White", bg="#b82741", command=exit)
exit_button.place(x=150, y=320)

# Entry Fields
guessed_number = StringVar()
number_form = Entry(window, font=("Raleway", 11), textvariable=guessed_number)
number_form.place(x=70, y=150)

# Guess Button
guess_button = Button(window, text="Guess", font=("Raleway", 13), state='normal', fg="black", bg="white",
                         command=play_game)
guess_button.place(x=90, y=180)

# Start the window
window.mainloop()
