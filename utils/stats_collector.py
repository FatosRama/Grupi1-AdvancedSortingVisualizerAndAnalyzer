from dataclasses import dataclass
from typing import Dict

@dataclass
class SortStats:
    pass

class StatsCollector:
    def __init__(self):
        self.stats: Dict[str, SortStats] = {}