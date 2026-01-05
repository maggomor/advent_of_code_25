from pydantic import BaseModel
import numpy as np
from typing import Tuple
import itertools
from pathlib import Path

file_path = Path(__file__).parent / "../no_push/inputs/day5.txt"

class DayFiveClass(BaseModel):
    puzzle_input: str
    
    def process_puzzle_input(self) -> Tuple[list, list]:
        return self.puzzle_input.split("\n\n")
    
    def get_list_of_ranges(self, input_list: list) -> list:
        return [range(int(x.split("-")[0]), int(x.split("-")[1])+1) for x in input_list.split("\n")]

    def check_all_ids(self) -> int:
        ranges_str, idx = self.process_puzzle_input()
        ranges = self.get_list_of_ranges(ranges_str)
        accept_id = []
        for elem in ranges:
            accept_id.append(list(elem))
            accept_id = [list(set(list(itertools.chain.from_iterable(accept_id))))]
        return len(list(set(list(itertools.chain(*accept_id)))))
    
    def check_id_overlap(self) -> int:
        ranges_str, idx = self.process_puzzle_input()
        ranges = self.get_list_of_ranges(ranges_str)
        intersections = [0]
        #for i in range(len(ranges)-1):
        #    set_elem = set(ranges[i])
        #    for comparison_range in ranges[i+1:]:
        #        intersections.append(len(set_elem.intersection(comparison_range)))
        min_elem = min([x[0] for x in ranges])
        max_elem = max([x[-1]+1 for x in ranges])
        counter = 0
        for i in range(min_elem, max_elem):
            flag = False
            for elem in ranges:
                if ((i in elem) and (not flag)):
                    counter += 1
                    flag = True
        counter = 0
        #for elem in ranges:
        #    counter += elem[-1] + 1 - elem[0]
        #counter -= sum(intersections)
        return counter
    
if __name__ == "__main__":
    puzzle_input = "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"
    with open(file_path, "r") as f:
        puzzle_input = f.read()
    #puzzle_input = "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"
    checker = DayFiveClass(puzzle_input = puzzle_input)
    outcome = checker.check_id_overlap()
    print(f"Number of acceptable ingredients is: {outcome}")