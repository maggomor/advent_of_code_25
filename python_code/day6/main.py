from pydantic import BaseModel
import numpy as np
from typing import Tuple

from pathlib import Path

file_path = Path(__file__).parent / "../no_push/inputs/day6.txt"


class DaySixClass(BaseModel):
    puzzle_input: str
    
    def process_puzzle_input(self) -> Tuple[list, list]:
        values = [[y for y in x.split(" ") if y != ""] for x in self.puzzle_input.split("\n")]
        return values[:-1], values[-1]
    
    def get_matrix(self, input_list: list, index_list:list) -> np.array:
        multipliers = [index for index, val in enumerate(index_list) if val == "*"]
        for index, item in enumerate(input_list):
            input_list[index] = [np.log(int(x)) if idx in multipliers else int(x) for idx, x in enumerate(item)]
        return np.array(input_list)
            
    def compute_sum(self) -> int:
        values, indexes = self.process_puzzle_input()
        puzzle_matrix = self.get_matrix(values, indexes)
        sums = puzzle_matrix.T @ np.ones(len(puzzle_matrix))
        multipliers = [index for index, val in enumerate(indexes) if val == "*"]
        for idx in multipliers:
            sums[idx] = np.exp(sums[idx])
        return int(sums.T @ np.ones(puzzle_matrix.shape[1]))
    
if __name__ == "__main__":
    with open(file_path, "r") as f:
        puzzle_input = f.read()
    checker = DaySixClass(puzzle_input = puzzle_input)
    outcome = checker.compute_sum()
    print(f"Sum of outcomes is: {outcome}")