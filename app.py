import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, font


class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quicknote")
        self.file_path = None
        self.current_font = ("Arial", 12)

        # Create Text Widget
        self.text_area = tk.Text(self.root, wrap='word', font=self.current_font)
        self.text_area.pack(expand=1, fill='both')

        # Create Menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # Menu Bar
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save As...", command=self.save_as)
        self.file_menu.add_command(label="Save", command=self.save, state='disabled')
        self.edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Change Font", command=self.change_font)

    def save_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.file_path = file_path
                self.file_menu.entryconfig("Save", state='normal')
                self.root.title(f"Quicknote - {self.file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def save(self):
        if self.file_path:
            try:
                with open(self.file_path, 'w') as file:
                    file.write(self.text_area.get(1.0, tk.END))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, file.read())
                self.file_path = file_path
                self.file_menu.entryconfig("Save", state='normal')
                self.root.title(f"Quicknote - {self.file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")

    def change_font(self):
        font_family = simpledialog.askstring("Font", "Enter font family:", initialvalue=self.current_font[0])
        font_size = simpledialog.askinteger("Font Size", "Enter font size:", initialvalue=self.current_font[1])
        if font_family and font_size:
            self.current_font = (font_family, font_size)
            self.text_area.config(font=self.current_font)


if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
