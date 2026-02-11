# Name: Wirithipha Duangjan
# Student ID: 673040468-9

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("450x700")
root.configure(bg="#e6e6e6")
root.resizable(False, False)


main = tk.Frame(root, bg="white", padx=15, pady=15)
main.pack(pady=20)


title = tk.Label(main,
                 text="Adult and Child BMI Calculator",
                 bg="#b74a3a",
                 fg="white",
                 font=("Arial", 12, "bold"),
                 pady=8)
title.pack(fill="x", pady=(0,15))


age_frame = tk.Frame(main, bg="white")
age_frame.pack(fill="x", pady=5)

tk.Label(age_frame, text="Calculate BMI for",
         bg="white").pack(side="left")

age_combo = ttk.Combobox(age_frame,
                         values=["Adult Age 20+",
                                 "Child Age 2-19"],
                         state="readonly",
                         width=18)
age_combo.current(0)
age_combo.pack(side="right")


weight_frame = tk.Frame(main, bg="white")
weight_frame.pack(fill="x", pady=8)

tk.Label(weight_frame, text="Weight:",
         bg="white").pack(side="left")

weight_entry = tk.Entry(weight_frame, width=10)
weight_entry.pack(side="left", padx=5)

weight_unit = ttk.Combobox(weight_frame,
                           values=["pounds",
                                   "kilograms"],
                           state="readonly",
                           width=10)
weight_unit.current(0)
weight_unit.pack(side="right")


height_frame = tk.Frame(main, bg="white")
height_frame.pack(fill="x", pady=8)

tk.Label(height_frame, text="Height:",
         bg="white").pack(side="left")

height_entry = tk.Entry(height_frame, width=10)
height_entry.pack(side="left", padx=5)

height_unit = ttk.Combobox(height_frame,
                           values=["feet",
                                   "meters",
                                   "centimeters"],
                           state="readonly",
                           width=10)
height_unit.current(0)
height_unit.pack(side="right")


inch_frame = tk.Frame(main, bg="white")
inch_frame.pack(fill="x", pady=5)

inch_entry = tk.Entry(inch_frame, width=10)
inch_entry.pack(side="left", padx=(60,5))

tk.Label(inch_frame, text="inches",
         bg="white").pack(side="left")


button_frame = tk.Frame(main, bg="white")
button_frame.pack(fill="x", pady=15)

clear_btn = tk.Button(button_frame,
                      text="Clear",
                      width=10)
clear_btn.pack(side="left")

calc_btn = tk.Button(button_frame,
                     text="Calculate",
                     width=10)
calc_btn.pack(side="right")


answer_frame = tk.LabelFrame(
    main,
    text="Answer:",
    font=("Arial", 10, "bold"),
    bg="white",
    padx=15,
    pady=15,
    bd=1,
    relief="solid"
)
answer_frame.pack(fill="x", pady=15)



table_frame = tk.Frame(answer_frame, bg="white")
table_frame.pack(pady=10)

rows = [
    ("≤ 18.4", "Underweight", "#f7d774"),
    ("18.5 - 24.9", "Normal", "#9bd18c"),
    ("25.0 - 39.9", "Overweight", "#f5b041"),
    ("≥ 40.0", "Obese", "#f25c54")
]

# Header
tk.Label(table_frame, text="BMI",
         bg="#dddddd", width=15).grid(row=0, column=0)
tk.Label(table_frame, text="Status",
         bg="#dddddd", width=15).grid(row=0, column=1)

# Rows
for i, (bmi, status, color) in enumerate(rows, start=1):
    tk.Label(table_frame,
             text=bmi,
             bg=color,
             width=15).grid(row=i, column=0)
    tk.Label(table_frame,
             text=status,
             bg="#f2f2f2",
             width=15).grid(row=i, column=1)

root.mainloop()
