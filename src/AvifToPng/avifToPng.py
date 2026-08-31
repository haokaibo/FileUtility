# python src/main.py

import tkinter as tk
from tkinter import filedialog
import subprocess

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x200')
        
        # Input folder label and entry
        self.input_label = tk.Label(self, text='Input Folder:')
        self.input_label.pack()
        self.input_entry = tk.Entry(self)
        self.input_entry.pack()
        
        # Output folder label and entry
        self.output_label = tk.Label(self, text='Output Folder:')
        self.output_label.pack()
        self.output_entry = tk.Entry(self)
        self.output_entry.pack()
        
        # Button to select input folder
        self.select_input_button = tk.Button(self, text='Select Input Folder', command=self.select_input_folder)
        self.select_input_button.pack()
        
        # Button to convert AVIF files
        self.convert_button = tk.Button(self, text='Convert AVIF Files', command=self.convert_avif_files)
        self.convert_button.pack()

    def select_input_folder(self):
        folder_path = filedialog.askdirectory()
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, folder_path)

    def convert_avif_files(self):
        input_folder = self.input_entry.get()
        output_folder = self.output_entry.get()
        
        # Check if both folders are selected
        if input_folder and output_folder:
            subprocess.run(f"avif2png -i {input_folder} -o {output_folder}", shell=True)
        else:
            print("Please select both input and output folders")

if __name__ == "__main__":
    app = App()
    app.mainloop()