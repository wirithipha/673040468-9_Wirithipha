# Name: Wirithipha Duangjan
# Student ID: 673040468-9

import tkinter as tk


class SimpleCalculator:

    def __init__(self, root):
        self.root = root
        self.root.title("AJN Calculator")
        self.root.geometry("370x340")  
        self.root.resizable(False, False)

        self.expression = ""
        self.create_widgets()

    def create_widgets(self):

        
        self.display = tk.Entry(
            self.root,
            font=("Arial", 20),  
            justify="right",
            bd=3,
            relief="ridge"
        )
        self.display.pack(fill="x", padx=8, pady=8)

        button_frame = tk.Frame(self.root)
        button_frame.pack(padx=8, pady=3)

        buttons = [
            ["C", "%", "/", "Del"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["", "0", ".", "="]
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):

                btn = tk.Button(
                    button_frame,
                    text=text,
                    width=6,         
                    height=2,
                    font=("Arial", 12),
                    bg="#EAD8C0",
                    activebackground="#D8C3A5",
                    bd=2,
                    relief="raised",
                    command=lambda t=text: self.on_button_click(t)
                )

                btn.grid(row=r, column=c, padx=4, pady=4)

    def on_button_click(self, text):

        if text == "C":
            self.expression = ""
            self.display.delete(0, tk.END)

        elif text == "Del":
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

        elif text == "=":
            try:
                result = eval(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""

        elif text == "":
            pass

        else:
            self.expression += text
            self.display.insert(tk.END, text)


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()
