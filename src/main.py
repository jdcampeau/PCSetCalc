import tkinter as tk

from calculator import *

class App(tk.Tk):
    def __init__(self):
        super().__init()
        self.title("Musical Set Theory: Prime Form Calculator")
        self.geometry("600x300")

        self.label = tk.label(root, text="Enter your name:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Calculate", command=handle_click)
        self.button.pack(pady=10)

    def handle_click(self):
        user_text = self.entry.get()
        self.label.config(text=f"Here's the text you entered: {user_text}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
