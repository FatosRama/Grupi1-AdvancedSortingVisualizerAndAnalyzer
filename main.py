import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from visualizer import Visualizer
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

        ttk.Label(control_frame, text="Algorithm:").grid(row=5, column=0, sticky="w", pady=10)
        self.algo_var = tk.StringVar()
        self.algo_combo = ttk.Combobox(control_frame, textvariable=self.algo_var,
                                       state="readonly", width=20)
        self.algo_combo.grid(row=5, column=1, padx=5)
        self.load_algorithms()

        stats_frame = ttk.LabelFrame(self.root, text="Current Algorithm Stats", padding=10)
        stats_frame.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

        self.stats_text = scrolledtext.ScrolledText(stats_frame, height=20, width=30)
        self.stats_text.pack(fill=tk.BOTH, expand=True)

        report_frame = ttk.LabelFrame(self.root, text="Comparison Report", padding=10)
        report_frame.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

        self.report_text = scrolledtext.ScrolledText(report_frame, height=12)
        self.report_text.pack(fill=tk.BOTH, expand=True)

        self.root.grid_rowconfigure(0, weight=3)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.columnconfigure(1, weight=3)
        self.root.columnconfigure(2, weight=1)

        style = ttk.Style()
        style.configure('Accent.TButton', foreground='white', background='#0078D7')

        self.generate_array()

        # PJESA E FUNKSIONEVE

    def load_algorithms(self):

        algorithms = [
            "Bubble Sort", "Bucket Sort", "Counting Sort", "Heap Sort",
            "Insertion Sort", "Merge Sort", "Quick Sort", "Radix Sort",
            "Selection Sort", "Tree Sort"
        ]
        self.algo_combo['values'] = algorithms
        self.algo_combo.current(0)
           
        
    def generate_array(self):
        size = self.size_var.get()
        array_type = self.array_type.get()

        if array_type == "Random":
            self.array = random.sample(range(1, size*3 + 1), size)
        elif array_type == "Nearly Sorted":
            self.array = list(range(1, size+1))

            for _ in range(size//10):
                i, j = random.sample(range(size), 2)
                self.array[i], self.array[j] = self.array[j], self.array[i]
        elif array_type == "Reverse":
            self.array = list(range(size, 0, -1))
        elif array_type == "Few Unique":
            unique_vals = random.sample(range(1, 100), 5)
            self.array = [random.choice(unique_vals) for _ in range(size)]

        self.update_visualization()
        


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


    def visualize_sort(self):
        if not self.array:
            messagebox.showwarning("Warning", "Generate an array first")
            return
                
        algo = self.algo_var.get()
        if not algo:
            messagebox.showwarning("Warning", "Select an algorithm")
            return
                
        self.toggle_buttons(False)

        try:
            filename = algo.lower().replace(" ","_")
            module = importlib.import_module(f"algorithms.{filename}")
            algorithm_func = getattr(module, filename)

            vis = Visualizer(self.array, self.fig, self.ax, self.canvas)
                    
            self.root.after(100, lambda: self.run_algorithm_steps(algorithm_func, vis, algo))
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run {algo}:{str(e)}")
            self.toggle_buttons(True)

