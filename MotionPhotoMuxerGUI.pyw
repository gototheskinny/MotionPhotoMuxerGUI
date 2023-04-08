import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.input_path = None
        self.output_path = None
        self.show_console = False
        self.pack()
        self.create_widgets()
        self.master.protocol("WM_DELETE_WINDOW", self.master.destroy)

    def create_widgets(self):
        self.select_input_button = tk.Button(self)
        self.select_input_button["text"] = "Select input directory"
        self.select_input_button["command"] = self.select_input_directory
        self.select_input_button.pack(side="top")

        self.select_output_button = tk.Button(self)
        self.select_output_button["text"] = "Select output directory"
        self.select_output_button["command"] = self.select_output_directory
        self.select_output_button.pack(side="top")

        self.run_button = tk.Button(self)
        self.run_button["text"] = "Run"
        self.run_button["command"] = self.run_script
        self.run_button.pack(side="top")

        self.console_button = tk.Button(self)
        self.console_button["text"] = "Show console"
        self.console_button["command"] = self.toggle_console
        self.console_button.pack(side="top")

        self.console_text = tk.Text(self, height=20, width=100)
        self.console_text.pack()

    def select_input_directory(self):
        self.input_path = filedialog.askdirectory()

    def select_output_directory(self):
        self.output_path = filedialog.askdirectory()

    def run_script(self):
        if self.input_path is None or self.output_path is None:
            tk.messagebox.showerror("Error", "Please select input and output directories.")
            return

        args = ['python', 'MotionPhotoMuxer.py', '--dir', self.input_path, '--output', self.output_path]
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        self.update_console(stdout.decode())
        self.update_console(stderr.decode())

    def toggle_console(self):
        self.show_console = not self.show_console
        if self.show_console:
            self.console_button.config(text="Hide console")
        else:
            self.console_button.config(text="Show console")

    def update_console(self, message):
        if self.show_console:
            self.console_text.insert(tk.END, message + "\n")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
