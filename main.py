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