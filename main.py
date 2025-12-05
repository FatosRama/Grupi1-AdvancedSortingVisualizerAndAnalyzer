import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import importlib
import os

class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Sorting Visualizer")
        self.root.geometry("1400x900")

        self.array = []
        self.current_sorter = None
        self.all_stats = {}

        self.setup_ui()

    # PJESA E UI

    def setup_ui(self):
        control_frame = ttk.LabelFrame(self.root, text="Controls", padding=10)
        control_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        ttk.Label(control_frame, text="Array Size:").grid(row=0, column=0, sticky="w")
        self.size_var = tk.IntVar(value=30)
        size_slider = ttk.Scale(control_frame, from_=10, to=100,variable=self.size_var, orient="horizontal")
        size_slider.grid(row=0, column=1, padx=5)

        ttk.Label(control_frame, text="Array Type:").grid(row=1, column=0, sticky="w", pady=5)
        self.array_type = tk.StringVar(value="Random")
        array_types = ["Random", "Nearly Sorted", "Reverse", "Few Unique"]

        ttk.Combobox(control_frame, textvariable=self.array_type,values=array_types, state="readonly", width=15).grid(row=1, column=1, padx=5)

        ttk.Button(control_frame, text="Generate Array",
                   command=self.generate_array).grid(row=2, column=0, columnspan=2, pady=10)

        ttk.Label(control_frame, text="Custom Array:").grid(row=3, column=0, sticky="w", pady=5)
        self.custom_entry = ttk.Entry(control_frame, width=25)
        self.custom_entry.grid(row=3, column=1, padx=5)
        ttk.Button(control_frame, text="Use Custom",
                   command=self.use_custom_array).grid(row=4, column=0, columnspan=2, pady=5)

        # PJESA E FUNKSIONEVE

        def load_algorithms(self):
            return
        
        def generate_array(self):
            return
        
        




        def use_custom_array(self):
            try:
                text = self.custom_entry.get()
                self.array = [int(x.strip()) for x in text.split(",")]
                if len(self.array) > 100:
                    self.array = self.array[:100]
                    messagebox.showinfo("Note", "Limited to first 100 elements")
                self.update_visualization()
            except ValueError:
                messagebox.showerror("Error", "Enter comma-separated integers")

        def update_visualization(self, arr=None, highlights=None, title=None):
            if arr is None:
                arr = self.array

            self.ax.clear()

            colors = ['skyblue'] * len(arr)
            if highlights:
                for idx in highlights:
                    if 0 <= idx < len(colors):
                        colors[idx] = 'red'

            bars = self.ax.bar(range(len(arr)), arr, color=colors)
            self.ax.set_title(title or "Array Visualization")
            self.ax.set_xlabel("Index")
            self.ax.set_ylabel("Value")

            if arr:
                self.ax.set_ylim(0, max(arr) * 1.1)

            self.canvas.draw()
