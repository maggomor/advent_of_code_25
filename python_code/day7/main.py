from pydantic import BaseModel
import numpy as np
from typing import Tuple, List
from collections import Counter
from pathlib import Path

file_path = Path(__file__).parent / "../no_push/inputs/day7.txt"


class DaySevenClass(BaseModel):
    puzzle_input: str
    
    def process_puzzle_input(self) -> List:
        return self.puzzle_input.split("\n")
    
    def emit_beam(self) -> List:
        puzzle_list = self.process_puzzle_input()
        origin = puzzle_list[0].find("S")
        puzzle_list = [list(x) for x in puzzle_list]
        puzzle_list[1] = [x if idx != origin else "|" for idx, x in enumerate(puzzle_list[1])]
        return puzzle_list        
    
    def split_beam(self, input_list: list, ray_indices :list) -> np.array:
        return [x if idx not in ray_indices else "|" for idx, x in enumerate(input_list)]
            
    def hit_splitter(self, previous_row: list, current_row: list) -> List:
        counter = 0
        for idx, elem in enumerate(previous_row):
            if elem == "|":
                if current_row[idx] == ".":
                    current_row[idx] = "|"
                elif current_row[idx] == "^":
                    if idx > 0:
                        current_row[idx-1] = "|"
                        counter += 1
                    if idx < (len(current_row) - 1):
                        current_row[idx+1] = "|"
                        counter += 1
                    if idx < (len(current_row) - 1):
                        counter -= 1
        return current_row, counter
    
    def traverse_manifold(self):
        puzzle_list = self.emit_beam()
        count_var = 0
        for idx, row in enumerate(puzzle_list):
            if idx == 0:
                pass
            elif idx == len(puzzle_list)-1:
                counter = Counter(row)
                return counter["|"], count_var
            else:
                next_row = puzzle_list[idx+1]
                puzzle_list[idx+1], new_counter = self.hit_splitter(previous_row = row, current_row = next_row)
                count_var += new_counter 

if __name__ == "__main__":
    with open(file_path, "r") as f:
        puzzle_input = f.read()
    checker = DaySevenClass(puzzle_input = puzzle_input)
    outcome, count = checker.traverse_manifold()
    print(f"Number of exiting rays is: {outcome}, Number of splits is {count}")