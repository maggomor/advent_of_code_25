from pydantic import BaseModel
import numpy as np
from typing import Tuple

from pathlib import Path

file_path = Path(__file__).parent / "../no_push/inputs/day5.txt"

class DayFiveClass(BaseModel):
    puzzle_input: str
    
    def process_puzzle_input(self) -> Tuple[list, list]:
        return self.puzzle_input.split("\n\n")
    
    def get_list_of_ranges(self, input_list: list) -> list:
        return [range(int(x.split("-")[0]), int(x.split("-")[1])+1) for x in input_list.split("\n")]

    def check_all_ingredients(self) -> int:
        counter = 0
        ranges_str, idx = self.process_puzzle_input()
        ranges = self.get_list_of_ranges(ranges_str)
        for elem in idx.split("\n"):
            id_value = int(elem)
            flag = False
            for range_elem in ranges:
                if (id_value in range_elem and not flag):
                    counter +=1
                    flag = True
        return counter
    
if __name__ == "__main__":
    puzzle_input = "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"
    with open(file_path, "r") as f:
        puzzle_input = f.read()
    checker = DayFiveClass(puzzle_input = puzzle_input)
    outcome = checker.check_all_ingredients()
    print(f"Number of acceptable ingredients is: {outcome}")