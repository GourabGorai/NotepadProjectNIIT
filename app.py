import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import ttkbootstrap as ttkb

def main_window(root: ttkb.Window):
    # window creation
    root.title("Death Note!")
    icon = tk.PhotoImage(file="app_images/skull.png")
    root.iconphoto(False, icon)
    root.state("zoomed")

    # title
    welcome = ttk.Label(master=root, text="Welcome to Death Note, What do you wanna Kill?", font=("Ink Free", 20), foreground="red")
    welcome.pack(side="top", anchor="center", padx=10, pady=10)

    #create new menu
    create_new = ttk.Label(master=root, text="Kill Someone", font=("Ink Free", 14), foreground="red")
    create_new.pack(side="top", anchor="nw", padx=10, pady=10)

    create_new_input_frame = ttk.Frame(master=root)
    create_new_button = ttk.Button(master=create_new_input_frame, text="Click to Create New Note", command=lambda: text_window(root))
    create_new_button.pack()
    create_new_input_frame.pack(side="top", anchor="nw", padx=5, pady=5)

    #see note menu
    see_note = ttk.Label(master=root, text="See who you have killed", font=("Ink Free", 14), foreground="red")
    see_note.pack(side="top", anchor="nw", padx=10, pady=10)

    see_note_input_frame = ttk.Frame(master=root)
    see_note_button = ttk.Button(master=see_note_input_frame, text="Click to Open Note", command=lambda: open_window(root))
    see_note_button.pack()
    see_note_input_frame.pack(side="top", anchor="nw", padx=5, pady=5)

    # about
    about = ttk.Label(master=root, text="Created by:\nPrasun Bagdi\nGourab Gorai\nPartha Sarathi Guin", font=("Ink Free", 14), foreground="red")
    about.pack(side="bottom", anchor="center", padx=10, pady=10)

    #run
    window.mainloop()

def open_window(root: ttkb.Window):

    file_path = filedialog.askopenfilename(filetypes=[("Text files", ".txt"), ("All files", ".*")])
    if file_path:
        with open(file_path, "r") as file:
            note_content = file.read()
        # Create a new Toplevel window
        new_window = tk.Toplevel(root)
        new_window.title("Death Note!")
        text_icon = tk.PhotoImage(file="app_images/skull.png")
        new_window.iconphoto(False, text_icon)
        new_window.state("zoomed")

        # Note content text
        see_note_text = ttk.Label(master=new_window, text="You have killed", font=("Ink Free", 14), foreground="red")
        see_note_text.pack(side="top", anchor="center", padx=10, pady=10)

        # Frame for text widget and scrollbars
        text_frame = ttk.Frame(master=new_window)
        text_frame.pack(side="top", anchor="center")

        # Vertical scrollbar
        v_scroll = ttk.Scrollbar(master=text_frame, orient=tk.VERTICAL)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Horizontal scrollbar
        h_scroll = ttk.Scrollbar(master=text_frame, orient=tk.HORIZONTAL)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        # Text widget with scrollbars
        note_text = tk.Text(master=text_frame, wrap="none", width=120, height=30, font=("Calibri", 14), yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
        note_text.pack(side="top", fill=tk.BOTH, expand=True)
        note_text.insert(tk.END, note_content)

        # Configure the scrollbars
        v_scroll.config(command=note_text.yview)
        h_scroll.config(command=note_text.xview)

        # save button
        save_button = ttk.Button(master=new_window, text="Save", command=lambda: save_note_to_file(note_text))
        save_button.pack(side="top", anchor="center")

def text_window(root: ttkb.Window):
    # Create a new Toplevel window
    new_window = tk.Toplevel(root)
    new_window.title("Death Note!")
    text_icon = tk.PhotoImage(file="app_images/skull.png")
    new_window.iconphoto(False, text_icon)
    new_window.state("zoomed")

    # Multi-line input for note content
    note_content_text = ttk.Label(master=new_window, text="You are going to kill", font=("Ink Free", 14), foreground="red")
    note_content_text.pack(side="top", anchor="center", padx=10, pady=10)

    # Frame for the text widget and scrollbars
    text_frame = ttk.Frame(master=new_window)
    text_frame.pack(side="top", anchor="center")

    # Vertical scrollbar
    v_scroll = ttk.Scrollbar(master=text_frame, orient=tk.VERTICAL)
    v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    # Horizontal scrollbar
    h_scroll = ttk.Scrollbar(master=text_frame, orient=tk.HORIZONTAL)
    h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    # Text widget with scrollbars
    note_content = tk.Text(master=text_frame, wrap="none", width=120, height=30, font=("Calibri", 14), yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
    note_content.pack(side="top", fill=tk.BOTH, expand=True)

    # Configure the scrollbars
    v_scroll.config(command=note_content.yview)
    h_scroll.config(command=note_content.xview)

    # save button
    save_button = ttk.Button(master=new_window, text="Save", command=lambda: save_note_to_file(note_content))
    save_button.pack(side="top", anchor="center")

def save_note_to_file(note_content: tk.Text):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", ".txt"), ("All files", ".*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(note_content.get("1.0", tk.END))

if __name__=="__main__":
    window = ttkb.Window(themename="cyborg")
    main_window(window)