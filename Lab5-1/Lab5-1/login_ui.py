# Name: Wirithipha Duangjan
# Student ID: 673040468-9

import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Login")
root.geometry("400x550")
root.configure(bg="#d9e3ec")


card = Frame(root, bg="white", padx=30, pady=30, bd=2, relief="groove")
card.pack(pady=30)


Label(card, text="LOGIN",
      font=("Arial", 14, "bold"),
      bg="white", fg="#444").pack(anchor="w", padx=35, pady=(30,20))

Label(card, text="Email", bg="white", anchor="w").pack(fill="x")
email_entry = Entry(card, width=30)
email_entry.pack(pady=5)



Label(card, text="Password", bg="white", anchor="w").pack(fill="x")
pass_entry = Entry(card, width=30, show="*")
pass_entry.pack(pady=5)


remember = Checkbutton(card,
                       text="Remember me?",
                       bg="white",
                       fg="#e75480",
                       activebackground="white")
remember.pack(anchor="w", pady=5)


login_btn = Button(card,
                   text="LOGIN",
                   bg="#e75480",
                   fg="white",
                   width=25,
                   pady=5,
                   relief="flat")
login_btn.pack(pady=10)


forgot = Label(card,
               text="Forgot Password?",
               bg="white",
               fg="gray")
forgot.pack(anchor="e")


or_frame = Frame(card, bg="white")
or_frame.pack(pady=15, fill="x")

line1 = Frame(or_frame, bg="lightgray", height=1)
line1.pack(side="left", expand=True, fill="x", padx=5)

Label(or_frame, text="OR", bg="white", fg="gray").pack(side="left")

line2 = Frame(or_frame, bg="lightgray", height=1)
line2.pack(side="left", expand=True, fill="x", padx=5)


social_frame = Frame(card, bg="white")
social_frame.pack(pady=10)

google_btn = Button(social_frame, text="G",
                    fg="red",
                    width=3,
                    relief="groove")
google_btn.pack(side="left", padx=5)

facebook_btn = Button(social_frame, text="f",
                      fg="#3b5998",
                      width=3,
                      relief="groove")
facebook_btn.pack(side="left", padx=5)

linkedin_btn = Button(social_frame, text="in",
                      fg="#0077b5",
                      width=3,
                      relief="groove")
linkedin_btn.pack(side="left", padx=5)


signup = Label(card,
               text="Need an account? SIGN UP",
               bg="white",
               fg="gray")
signup.pack(pady=15)

root.mainloop()
