import tkinter as tk

from calculator import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Musical Set Theory: Prime Form Calculator")
        self.geometry("900x450")

        self.label = tk.Label(self, text="Enter a list of any notes and/or pitch classes (separated by commas)", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.button = tk.Button(self, text="Calculate", command=self.handle_click)
        self.button.pack(pady=10)

        self.pform_label = tk.Label(self, text="", font=("Arial", 12))
        self.pform_label.pack(pady=5)

        self.icv_label = tk.Label(self, font=("Arial", 12))
        self.icv_label.pack(pady=5)

    def handle_click(self):
        pitches = self.entry.get()
        chord_data = full_calc(False, pitches)
        pform = chord_data[2]
        icv = chord_data[3]
        self.pform_label.config(text=f"Prime form: {pform}")
        self.icv_label.config(text=f"Interval class vector: {icv}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
