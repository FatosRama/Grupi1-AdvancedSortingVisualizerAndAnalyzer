from dataclasses import dataclass
from typing import Dict

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