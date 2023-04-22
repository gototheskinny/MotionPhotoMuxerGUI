import os, subprocess, tkinter as tk
from tkinter import filedialog, messagebox

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="black")
        self.master = master
        self.in_path = self.out_path = None
        self.show_console = True  # Set the show_console attribute to True
        self.pack()
        self.create_widgets()
        self.master.protocol("WM_DELETE_WINDOW", self.master.destroy)

    def create_widgets(self):
        self.select_in_button = tk.Button(self, text="Select input directory", command=self.select_in_dir)
        self.select_in_button.pack(side="top")
        self.select_out_button = tk.Button(self, text="Select output directory", command=self.select_out_dir)
        self.select_out_button.pack(side="top")
        self.run_button = tk.Button(self, text="Run", command=self.run_script)
        self.run_button.pack(side="top")
        self.console_button = tk.Button(self, text="Hide console", command=self.toggle_console)  # Change the text to "Hide console"
        self.console_button.pack(side="top")
        self.console_text = tk.Text(self, height=20, width=100, bg="black", fg="white")
        self.console_text.pack()
        
    def select_in_dir(self):
        self.in_path = filedialog.askdirectory()

    def select_out_dir(self):
        self.out_path = filedialog.askdirectory()

    def run_script(self):
        if None in (self.in_path, self.out_path):
            tk.messagebox.showerror("Error", "Please select input and output directories.")
            return

        args = ['python', 'MotionPhotoMuxer.py', '--dir', self.in_path, '--output', self.out_path]
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        self.update_console(stdout.decode() + stderr.decode())

    def toggle_console(self):
        self.show_console = not self.show_console
        self.console_button.config(text=f"{'Hide' if self.show_console else 'Show'} console")

    def update_console(self, message):
        if self.show_console:
            self.console_text.insert(tk.END, message + "\n")

root = tk.Tk()
root.configure(bg="black")
app = App(master=root)
app.mainloop()
