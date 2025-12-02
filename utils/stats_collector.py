from dataclasses import dataclass
from typing import Dict
import time

@dataclass
class SortStats:
    name: str
    comparisons: int = 0
    swaps: int = 0
    array_accesses: int = 0
    start_time: float = 0.0
    end_time: float = 0.0
    finished: bool = False

class StatsCollector:
    def __init__(self):
        self.stats: Dict[str, SortStats] = {}


@property
def elapsed(self) -> float:
    return self.end_time - self.start_time if self.finished else time.time() - self.start_time

def finalize(self):
    self.end_time = time.time()
    self.finished = True

def register(self, algo_name: str):
    self.stats[algo_name] = SortStats(name=algo_name, start_time=time.time())

def increment(self, algo_name: str, comparisons=0, swaps=0, accesses=0):
    s = self.stats.get(algo_name)
    if s:
        s.comparisons += comparisons
        s.swaps += swaps
        s.array_accesses += accesses

def finish(self, algo_name: str):
    if algo_name in self.stats:
        self.stats[algo_name].finalize()

def get_ranking(self):
    finished = [s for s in self.stats.values() if s.finished]
    return sorted(finished, key=lambda x: x.elapsed)