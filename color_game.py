import random
import tkinter as tk
from tkinter import messagebox

def play_game(event=None):
    global machine_color, attempts_left, games_won, games_lost
    user_color = color_entry.get().lower()

    if user_color not in colors:
        messagebox.showerror("Error", "Invalid color. Please choose from the list.")
        return

    if user_color == machine_color:
        messagebox.showinfo("Success", f"You won the game!\nAttempts used: {attempts - attempts_left + 1}")
        games_won += 1
        reset_game()
    else:
        attempts_left -= 1
        if attempts_left == 0:
            messagebox.showerror("Game Over", f"You lost! The correct color was: {machine_color}")
            games_lost += 1
            reset_game()
        else:
            messagebox.showwarning("Try Again", f"Wrong guess! Attempts left: {attempts_left}")

def reset_game():
    global machine_color, attempts_left
    machine_color = random.choice(colors)
    attempts_left = attempts
    color_entry.delete(0, tk.END)

def show_scoreboard(event=None):
    messagebox.showinfo("Score Board", f"Games Won: {games_won}\nGames Lost: {games_lost}\nPlayer Name: {player_name}")

def start_game(event=None):
    global player_name
    player_name = name_entry.get()
    if not player_name:
        messagebox.showerror("Error", "Please enter your name.")
        return
    main_frame.pack_forget()
    game_frame.pack(padx=20, pady=20)
    reset_game()

def exit_game(event=None):
    root.quit()

colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']
attempts = 5
attempts_left = attempts
games_won = 0
games_lost = 0
player_name = ""

root = tk.Tk()
root.title("Color Game")
root.configure(bg="#1a1a2e")

main_frame = tk.Frame(root, bg="#16213e")
main_frame.pack(padx=20, pady=20)

tk.Label(main_frame, text="Welcome to the Color Game!", font=("Helvetica", 16), fg="white", bg="#16213e").pack(pady=10)
tk.Label(main_frame, text="Please enter your name for the score board:", fg="white", bg="#16213e").pack()
name_entry = tk.Entry(main_frame)
name_entry.pack(pady=5)
name_entry.bind('<Return>', start_game)

tk.Button(main_frame, text="Start Game", command=start_game, bg="#0f3460", fg="white").pack(pady=10)

game_frame = tk.Frame(root, bg="#16213e")

tk.Label(game_frame, text="Guess the color from:", font=("Helvetica", 14), fg="white", bg="#16213e").pack(pady=5)
color_list_label = tk.Label(game_frame, text=", ".join(colors), fg="white", bg="#16213e")
color_list_label.pack(pady=5)

color_entry = tk.Entry(game_frame)
color_entry.pack(pady=5)
color_entry.bind('<Return>', play_game)

tk.Button(game_frame, text="Submit", command=play_game, bg="#0f3460", fg="white").pack(pady=5)
tk.Button(game_frame, text="See Scoreboard", command=show_scoreboard, bg="#0f3460", fg="white").pack(pady=5)
tk.Button(game_frame, text="Exit", command=exit_game, bg="#e94560", fg="white").pack(pady=5)

root.mainloop()
