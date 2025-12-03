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
