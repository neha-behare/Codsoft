import tkinter as tk
import random

# Game Options
options = ["Rock", "Paper", "Scissors"]

# Score Tracking
user_score = 0
computer_score = 0

# Game Logic
def determine_winner(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(options)
    user_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!", fg="blue")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text="You win!", fg="green")
        user_score += 1
    else:
        result_label.config(text="You lose!", fg="red")
        computer_score += 1

    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Setup UI
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x350")
window.config(bg="#f0f0f0")

title_label = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

user_choice_label = tk.Label(window, text="You chose: ", font=("Arial", 12), bg="#f0f0f0")
user_choice_label.pack()

computer_choice_label = tk.Label(window, text="Computer chose: ", font=("Arial", 12), bg="#f0f0f0")
computer_choice_label.pack()

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), bg="#f0f0f0")
result_label.pack(pady=10)

score_label = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Arial", 12), bg="#f0f0f0")
score_label.pack(pady=10)

button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: determine_winner("Rock"))
paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: determine_winner("Paper"))
scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: determine_winner("Scissors"))

rock_button.grid(row=0, column=0, padx=10, pady=10)
paper_button.grid(row=0, column=1, padx=10, pady=10)
scissors_button.grid(row=0, column=2, padx=10, pady=10)

quit_button = tk.Button(window, text="Quit Game", command=window.destroy, bg="red", fg="white")
quit_button.pack(pady=10)

window.mainloop()
