import tkinter as tk
from tkinter import messagebox
import random
import webbrowser

# List of random quotes
quotes = [
    "Believe you can and you're halfway there.",
    "Success is not the key to happiness. Happiness is the key to success.",
    "Your time is limited, so don't waste it living someone else's life.",
    "Don't let yesterday take up too much of today.",
    "It's not whether you get knocked down, it's whether you get up."
]

# Function to get a random quote
def get_random_quote():
    return random.choice(quotes)

# Function to update the quote label
def display_new_quote():
    quote = get_random_quote()
    quote_label.config(text=quote)

# Function to share the quote on Twitter
def share_on_twitter():
    quote = quote_label.cget("text")
    if quote:
        url = f"https://twitter.com/intent/tweet?text={quote}"
        webbrowser.open(url)
    else:
        messagebox.showwarning("No Quote", "Generate a quote first!")

# Set up the main window
root = tk.Tk()
root.title("Random Quote Generator")

# Set window size
root.geometry("400x300")

# Label to display the random quote
quote_label = tk.Label(root, text="", wraplength=300, font=("Helvetica", 14), justify="center")
quote_label.pack(pady=30)

# Button to get a new random quote
generate_button = tk.Button(root, text="New Quote", command=display_new_quote, bg="blue", fg="white", font=("Helvetica", 12))
generate_button.pack(pady=10)

# Button to share the quote on Twitter
share_button = tk.Button(root, text="Share on Twitter", command=share_on_twitter, bg="green", fg="white", font=("Helvetica", 12))
share_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
