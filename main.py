import tkinter as tk

window = tk.Tk()


def handle_click(event):
    global love
    love += 1
    love_label['text'] = f"Love Recieved: {love}"
    love_label.pack()


def it_has_been_written(*args):
    button['text'] = f"Click me {user_entry.get() or ''}"
    button.pack()

love = 0
greeting = tk.Label(text="Hello, Owner!", padx=6, pady=6)
greeting.pack(padx=6, pady=6)
name_label = tk.Label(text="What is your Name?")
name_label.pack(padx=6, pady=6)
user = tk.StringVar()
user.trace("w", lambda name, index, mode, sv=user: it_has_been_written(user))
user_entry = tk.Entry(textvariable=user)

user_entry.pack(padx=6, pady=6)

name_label = tk.Label(text="Pet Button")
name_label.pack(padx=6, pady=6)
button = tk.Button(
    text=f"Click me! {user_entry.get() or ''}",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

button.bind("<Button-1>", handle_click)
button.pack(padx=6, pady=6)

love_label = tk.Label(text=f"Love Recieved {love}")
name_label.pack(padx=6, pady=6)
window.mainloop()