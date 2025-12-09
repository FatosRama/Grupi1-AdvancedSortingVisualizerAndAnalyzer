import time
import matplotlib.pyplot as plt

class Visualizer:
    """Visualizer for step-by-step sorting"""

    def __init__(self, arr, fig, ax, canvas):
        self.arr = arr.copy()
        self.original = arr.copy()
        self.fig = fig
        self.ax = ax
        self.canvas = canvas
        self.comparisons = 0
        self.swaps = 0
        self.steps = 0
        self.start_time = time.time()

    def compare(self, i, j):
     """Compare two elements"""
        self.comparisons += 1
        self.steps += 1
        self.update_display([i, j], "Comparing")


    def swap(self, i, j):
     """Swap two elements"""
        self.swaps += 1
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.steps += 1
        self.update_display([i, j], "Swapping")

     def update_display(self, highlights, action):
        """Update visualization"""
        self.ax.clear()

        colors = []
        for idx in range(len(self.arr)):
            if idx in highlights:
                colors.append('red')
            else:
                colors.append('skyblue')

        self.ax.bar(range(len(self.arr)), self.arr, color=colors)
        self.ax.set_title(f"{action} - Step {self.steps}")
        self.ax.set_xlabel("Index")
        self.ax.set_ylabel("Value")

        if self.arr:
            self.ax.set_ylim(0, max(self.arr) * 1.1)

        self.canvas.draw()



class FastVisualizer:
    """Fast Visualizer for comparisons (no display updates)"""