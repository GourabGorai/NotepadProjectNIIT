import tkinter as tk
from tkinter import filedialog, messagebox


class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quicknote")
        self.file_path = None

        # Create Text Widget
        self.text_area = tk.Text(self.root, wrap='word')
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
                self.root.title(f"Notepad - {self.file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
