import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from visualizer import Visualizer
from visualizer import FastVisualizer
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import importlib
import os

class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Sorting Visualizer")
        self.root.geometry("1700x1000")

        self.array = []
        self.current_sorter = None
        self.all_stats = {}
        self.is_resuming = False
        self.stop_requested = False

        self.setup_ui()

    # PJESA E UI

    def setup_ui(self):
        self.control_frame = ttk.LabelFrame(self.root, text="Controls", padding=10)
        self.control_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        ttk.Label(self.control_frame, text="Array Size:").grid(row=0, column=0, sticky="w")
        self.size_var = tk.IntVar(value=30)
        size_slider = ttk.Scale(self.control_frame, from_=10, to=100,variable=self.size_var, orient="horizontal")
        size_slider.grid(row=0, column=1, padx=5)

        ttk.Label(self.control_frame, text="Array Type:").grid(row=1, column=0, sticky="w", pady=5)
        self.array_type = tk.StringVar(value="Random")
        array_types = ["Random", "Nearly Sorted", "Reverse", "Few Unique"]

        ttk.Combobox(self.control_frame, textvariable=self.array_type,values=array_types, state="readonly", width=15).grid(row=1, column=1, padx=5)

        ttk.Button(self.control_frame, text="Generate Array",
                   command=self.generate_array).grid(row=2, column=0, columnspan=2, pady=10)

        ttk.Label(self.control_frame, text="Custom Array:").grid(row=3, column=0, sticky="w", pady=5)
        self.custom_entry = ttk.Entry(self.control_frame, width=25)
        self.custom_entry.grid(row=3, column=1, padx=5)
        ttk.Button(self.control_frame, text="Use Custom",
               command=self.use_custom_array).grid(row=4, column=0, columnspan=2, pady=5)

        ttk.Label(self.control_frame, text="Algorithm:").grid(row=5, column=0, sticky="w", pady=10)
        self.algo_var = tk.StringVar()
        self.algo_combo = ttk.Combobox(self.control_frame, textvariable=self.algo_var,
                           state="readonly", width=20)
        self.algo_combo.grid(row=5, column=1, padx=5)
        self.load_algorithms()

        ttk.Label(self.control_frame, text="Speed (ms): ").grid(row=6, column=0, sticky="w", pady=5)
        self.speed_var = tk.IntVar(value=50)
        ttk.Scale(self.control_frame, from_=1, to=500, variable=self.speed_var, orient="horizontal").grid(row=6, column=1, padx=5)

        ttk.Button(self.control_frame, text="Visualize Sort", command=self.visualize_sort, style='Accent.TButton').grid(row=7, column=0, columnspan=2, pady=10)
        ttk.Button(self.control_frame, text="Fast Sort (No Visual)", command=self.fast_sort).grid(row=8, column=0, columnspan=2, pady=5)
        ttk.Button(self.control_frame, text="Compare All Algorithms", command=self.compare_all).grid(row=9, column=0, columnspan=2, pady=5)
        ttk.Button(self.control_frame, text="Reset", command=self.reset).grid(row=10, column=0, columnspan=2, pady=5)
        ttk.Button(self.control_frame, text="Pause", command=self.stop_sort).grid(row=11, column=0, columnspan=2, pady=5)

        vis_frame = ttk.LabelFrame(self.root, text="Visualization", padding=10)
        vis_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.fig, self.ax = plt.subplots(figsize=(12, 7))
        self.canvas = FigureCanvasTkAgg(self.fig, master=vis_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

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
            filename = algo.lower().replace(" ", "_")
            module = importlib.import_module(f"algorithms.{filename}")
            algorithm_func = getattr(module, filename)

            if self.is_resuming:
                vis = Visualizer(self.array, self.fig, self.ax, self.canvas)
                self.is_resuming = False
            else:
                vis = Visualizer(self.array, self.fig, self.ax, self.canvas)

            self.current_visualizer = vis

            self.stop_requested = False
            if hasattr(self, '_after_id'):
                try:
                    self.root.after_cancel(self._after_id)
                except Exception:
                    pass
                delattr(self, '_after_id')

            self._after_id = self.root.after(100, lambda: self.run_algorithm_steps(algorithm_func, vis, algo))

        except Exception as e:
            messagebox.showerror("Error", f"Failed to run {algo}:{str(e)}")
            self.toggle_buttons(True)

    def run_algorithm_steps(self, algorithm_func, visualizer, algo_name):
        try:
            if hasattr(self, 'stop_requested') and self.stop_requested:
                if hasattr(self, '_after_id'):
                    try:
                        self.root.after_cancel(self._after_id)
                    except Exception:
                        pass
                    delattr(self, '_after_id')
                return

            if not hasattr(self, 'algorithm_generator'):
                self.algorithm_generator = algorithm_func(visualizer)

            try:
                next(self.algorithm_generator)
                self._after_id = self.root.after(self.speed_var.get(),
                     lambda: self.run_algorithm_steps(algorithm_func, visualizer, algo_name))
            except StopIteration:
                self.algorithm_completed(visualizer, algo_name)
        except Exception as e:
            print(f"Error during visualization: {e}")
            self.algorithm_completed(visualizer, algo_name)

    def algorithm_completed(self, visualizer, algo_name):
        stats = visualizer.get_stats()
        stats['algorithm'] = algo_name
        self.all_stats[algo_name] = stats

        self.update_stats_display(stats)
        self.toggle_buttons(True)
        if hasattr(self, 'algorithm_generator'):
            try:
                del self.algorithm_generator
            except Exception:
                pass

        if hasattr(self, '_after_id'):
            try:
                self.root.after_cancel(self._after_id)
            except Exception:
                pass
            try:
                delattr(self, '_after_id')
            except Exception:
                pass

        self.stop_requested = False

    def fast_sort(self):
        if not self.array:
            messagebox.showwarning("Warning", "Generate an array first")
            return

        algo = self.algo_var.get()
        if not algo:
            messagebox.showwarning("Warning", "Select an algorithm")
            return

        try:
            filename = algo.lower().replace(" ", "_")
            module = importlib.import_module(f"algorithms.{filename}")
            algorithm_func = getattr(module, filename)

            vis = FastVisualizer(self.array.copy())

            for _ in algorithm_func(vis):
                pass

            stats = vis.get_stats()
            stats['algorithm'] = algo
            self.all_stats[algo] = stats

            self.update_visualization(vis.array, title=f"{algo} - Fast Sort Completed")
            self.update_stats_display(stats)
            self.update_report()


        except Exception as e:
            messagebox.showerror("Error", f"Failed to run {algo}:{str(e)}")

    def compare_all(self):
        if not self.array:
            messagebox.showwarning("Warning", "Generate an array first")
            return

        self.all_stats.clear()

        for algo in self.algo_combo['values']:
            try:
                filename = algo.lower().replace(" ", "_")
                module = importlib.import_module(f"algorithms.{filename}")
                algorithm_func = getattr(module, filename)

                vis = FastVisualizer(self.array.copy())

                for _ in algorithm_func(vis):
                    pass

                stats = vis.get_stats()
                stats['algorithm'] = algo
                self.all_stats[algo] = stats
            except Exception as e:
                print(f"Error running {algo}: {e}")

        self.update_report()

    def update_stats_display(self, stats):
        """Update current algorithm stats"""
        self.stats_text.delete(1.0, tk.END)

        report = f"Algorithm: {stats['algorithm']}\n"
        report += "=" * 30 + "\n"
        report += f"Time: {stats['time']:.6f} seconds\n"
        report += f"Comparisons: {stats['comparisons']:,}\n"
        report += f"Swaps: {stats['swaps']:,}\n"
        report += f"Array Size: {stats['array_size']}\n"
        report += f"Steps: {stats['steps']:,}\n"

        self.stats_text.insert(tk.END, report)

    def update_report(self):
        self.report_text.delete(1.0, tk.END)
        if not self.all_stats:
            self.report_text.insert(tk.END, "No statistics to display.\n")
            return

        report = "=" * 80 + "\n"
        report += "Sorting Algorithms Comparison Report\n"
        report += "=" * 80 + "\n\n"

        report += f"Array Size: {len(self.array)}\n"
        report += f"Array Type: {self.array_type.get()}\n\n"
        report += f"Array Sample: {self.array[:15]}...\n\n"

        report += f"{'Algorithm':<20}{'Time (s)':<12}{'Comparisons':<15}{'Swaps':<15}\n"
        report += "-" * 70 + "\n"

        
        sorted_stats = sorted(self.all_stats.items(), key=lambda kv: kv[1].get('time', float('inf')))
        for algo, stats in sorted_stats:
            report += f"{algo:<20}{stats.get('time', 0):<12.6f}"
            report += f"{stats.get('comparisons', 0):<15,} {stats.get('swaps', 0):<15,}\n"

        report += "\n" + "=" * 80 + "\n"
        report += "SUMMARY:\n"

        if len(sorted_stats) > 0:
            fastest = sorted_stats[0]
            slowest = sorted_stats[-1]

            report += f"Fastest: {fastest[0]} ({fastest[1].get('time', 0):.6f}s)\n"
            report += f"Slowest: {slowest[0]} ({slowest[1].get('time', 0):.6f}s)\n"

            if fastest[1].get('time', 0) > 0:
                ratio = slowest[1].get('time', 0) / fastest[1].get('time', 1)
                report += f"Speed Ratio (Slowest/Fastest): {ratio:.2f}x\n"

        self.report_text.insert(tk.END, report)

    def toggle_buttons(self, enabled):
        state = "normal" if enabled else "disabled"
        stop_state = "normal" if not enabled else "disabled"
        for w in self.control_frame.winfo_children():
            try:
                if getattr(w, 'cget', None) and w.cget('text') == 'Pause':
                    w.configure(state=stop_state)
                else:
                    w.configure(state=state)
            except Exception:
                pass

    def stop_sort(self):
        # Request stop and cancel any scheduled callbacks
        self.stop_requested = True

        if hasattr(self, '_after_id'):
            try:
                self.root.after_cancel(self._after_id)
            except Exception:
                pass
            try:
                delattr(self, '_after_id')
            except Exception:
                pass

        if hasattr(self, 'current_visualizer'):
            self.array = self.current_visualizer.arr.copy()  # Save current state
            self.update_visualization(self.array, title="Stopped")
            self.is_resuming = True  # Set resume flag

        if hasattr(self, 'algorithm_generator'):
            try:
                del self.algorithm_generator
            except Exception:
                pass

        self.toggle_buttons(True)

    def reset(self):
        self.array = []
        self.all_stats.clear()
        self.ax.clear()
        self.canvas.draw()
        self.stats_text.delete(1.0, tk.END)
        self.report_text.delete(1.0, tk.END)
        self.is_resuming = False

        if hasattr(self, 'algorithm_generator'):
            del self.algorithm_generator

        self.generate_array()


if __name__ == "__main__":
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()