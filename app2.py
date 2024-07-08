import tkinter as tk
from tkinter import filedialog, messagebox, font, ttk

class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quicknote")
        self.file_path = None

        # Default font
        self.current_font = ("Arial", 12)

        # Create Text Widget
        self.text_area = tk.Text(self.root, wrap='word', font=self.current_font)
        self.text_area.pack(expand=1, fill='both')

        # Create Menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # File Menu
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save As...", command=self.save_as)
        self.file_menu.add_command(label="Save", command=self.save, state='disabled')

        # Edit Menu
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
        font_popup = tk.Toplevel(self.root)
        font_popup.title("Change Font")

        tk.Label(font_popup, text="Font Family:").pack(pady=5)
        font_families = list(font.families())
        font_family_var = tk.StringVar(value=self.current_font[0])
        font_family_combobox = ttk.Combobox(font_popup, textvariable=font_family_var, values=font_families, state='readonly')
        font_family_combobox.pack(pady=5)

        tk.Label(font_popup, text="Font Size:").pack(pady=5)
        font_size_var = tk.IntVar(value=self.current_font[1])
        font_size_spinbox = tk.Spinbox(font_popup, from_=8, to=72, textvariable=font_size_var)
        font_size_spinbox.pack(pady=5)

        def apply_font():
            new_font_family = font_family_var.get()
            new_font_size = font_size_var.get()
            self.current_font = (new_font_family, new_font_size)
            self.text_area.config(font=self.current_font)
            font_popup.destroy()

        tk.Button(font_popup, text="Apply", command=apply_font).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
