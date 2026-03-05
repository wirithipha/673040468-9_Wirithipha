import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

root = tk.Tk()
root.title("Student Registration")
root.geometry("420x520")

# ---------- SUBMIT FUNCTION ----------
def submit_form():

    name_val = name.get()
    email_val = email.get()
    phone_val = phone.get()
    dob_val = dob.get()
    gender_val = gender.get()
    program_val = program.get()
    story_val = story.get("1.0","end").strip()

    frame.destroy()

    confirm = tk.Frame(root, padx=20, pady=20)
    confirm.pack(fill="both", expand=True)

    confirm.columnconfigure(1, weight=1)

    tk.Label(confirm,
             text="Registration Confirmed!",
             font=("Arial",16,"bold")
             ).grid(row=0,column=0,columnspan=2,pady=10)

    tk.Label(confirm,text="Name:").grid(row=1,column=0,sticky="w")
    tk.Label(confirm,text=name_val).grid(row=1,column=1,sticky="w")

    tk.Label(confirm,text="Email:").grid(row=2,column=0,sticky="w")
    tk.Label(confirm,text=email_val).grid(row=2,column=1,sticky="w")

    tk.Label(confirm,text="Phone:").grid(row=3,column=0,sticky="w")
    tk.Label(confirm,text=phone_val).grid(row=3,column=1,sticky="w")

    tk.Label(confirm,text="Date of Birth:").grid(row=4,column=0,sticky="w")
    tk.Label(confirm,text=dob_val).grid(row=4,column=1,sticky="w")

    tk.Label(confirm,text="Gender:").grid(row=5,column=0,sticky="w")
    tk.Label(confirm,text=gender_val).grid(row=5,column=1,sticky="w")

    tk.Label(confirm,text="Program:").grid(row=6,column=0,sticky="w")
    tk.Label(confirm,text=program_val).grid(row=6,column=1,sticky="w")

    tk.Label(confirm,text="Your story:").grid(row=7,column=0,sticky="w")
    tk.Label(confirm,text=story_val).grid(row=7,column=1,sticky="w")

    tk.Button(confirm,
              text="New Registration",
              command=root.destroy
              ).grid(row=8,column=0,columnspan=2,pady=20)

# ---------- MAIN FRAME ----------
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

frame.columnconfigure(0, weight=1)

title = tk.Label(frame,
                 text="Student Registration Form",
                 font=("Arial",16,"bold"))
title.grid(row=0,column=0,pady=10)

# Full Name
tk.Label(frame,text="Full Name:").grid(row=1,column=0,sticky="w")
name = tk.Entry(frame)
name.grid(row=2,column=0,sticky="ew")

# Email
tk.Label(frame,text="Email:").grid(row=3,column=0,sticky="w",pady=(6,0))
email = tk.Entry(frame)
email.grid(row=4,column=0,sticky="ew")

# Phone
tk.Label(frame,text="Phone:").grid(row=5,column=0,sticky="w",pady=(6,0))
phone = tk.Entry(frame)
phone.grid(row=6,column=0,sticky="ew")

# Date of Birth
tk.Label(frame,text="Date of Birth:").grid(row=7,column=0,sticky="w",pady=(6,0))
dob = DateEntry(frame,width=18)
dob.grid(row=8,column=0,sticky="w")

# Gender
tk.Label(frame,text="Gender:").grid(row=9,column=0,sticky="w",pady=(6,0))

gender = tk.StringVar()
gender.set(None)

gender_frame = tk.Frame(frame)
gender_frame.grid(row=10,column=0,sticky="w")

tk.Radiobutton(gender_frame,text="Male",
               variable=gender,value="Male").grid(row=0,column=0,sticky="w")

tk.Radiobutton(gender_frame,text="Female",
               variable=gender,value="Female").grid(row=0,column=1,sticky="w")

tk.Radiobutton(gender_frame,text="Non-binary",
               variable=gender,value="Non-binary").grid(row=0,column=2,sticky="w")

tk.Radiobutton(gender_frame,text="Prefer not to say",
               variable=gender,value="Prefer not to say").grid(row=0,column=3,sticky="w")

# Program
tk.Label(frame,text="Program:").grid(row=11,column=0,sticky="w",pady=(6,0))
program = ttk.Combobox(
    frame,
    values=[
        "Computer Science",
        "Engineering",
        "Business",
        "Arts",
        "Sciences"
    ]
)
program.grid(row=12,column=0,sticky="ew")

# About
tk.Label(frame,text="Tell us a little bit about yourself:").grid(row=13,column=0,sticky="w",pady=(6,0))
story = tk.Text(frame,height=4)
story.grid(row=14,column=0,sticky="ew")

# Terms
accept = tk.BooleanVar()
tk.Checkbutton(frame,
               text="I accept the terms and conditions.",
               variable=accept
               ).grid(row=15,column=0,sticky="w",pady=10)

# Submit
submit = tk.Button(frame,
                   text="Submit Registration",
                   command=submit_form)
submit.grid(row=16,column=0,pady=10)

root.mainloop()