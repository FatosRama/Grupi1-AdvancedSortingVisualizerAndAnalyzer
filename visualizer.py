import time

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

class FastVisualizer:
    """Fast Visualizer for comparisons (no display updates)"""