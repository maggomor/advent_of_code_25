from pydantic import BaseModel
import numpy as np
import itertools
from pathlib import Path

file_path = Path(__file__).parent / "../no_push/inputs/day4.txt"

class DayFourClass(BaseModel):
    puzzle_input: str
    
    def get_matrix_of_input(self) -> list:
        self.puzzle_input = self.puzzle_input.replace(".", "0").replace("@", "1")
        puzzle_input_list = self.puzzle_input.split("\n")
        return puzzle_input_list
    
    def make_input_matrix_numeric(self, puzzle_input_list: list) -> np.array:
        for index, elem in enumerate(puzzle_input_list):
            puzzle_input_list[index] = [int(elem[num]) for num in range(len(elem))]
        return np.array(puzzle_input_list)

    def create_puzzle_matrix(self) -> np.array:
        return self.make_input_matrix_numeric(self.get_matrix_of_input())
    
    def get_internal_adjacent_sum(self, puzzle_matrix: np.matrix, horizontal_val: int, vertical_val: int) -> int:
        value = 0
        for comp_1, comp_2 in itertools.product([-1,0,1],[-1,0,1]):
            if not (comp_1 == 0 and comp_2 == 0):
                value += puzzle_matrix[horizontal_val + comp_1 - 1, vertical_val + comp_2 - 1]
        return value
    
    def get_horizontal_adjacent_sum(self, puzzle_matrix: np.matrix, horizontal_val: int, step: int) -> int:
        value = 0
        if horizontal_val == 1:
            first_list = [0,1]
        elif horizontal_val == len(puzzle_matrix):
            first_list = [-1,0]
        else:
            raise ValueError("Wrong Size")
        for comp_1, comp_2 in itertools.product(first_list,[-1,0,1]):
            if not (comp_1 == 0 and comp_2 == 0):
                value += puzzle_matrix[horizontal_val + comp_1 -1, step + comp_2]
        return value

    def get_vertical_adjacent_sum(self, puzzle_matrix: np.matrix, vertical_val: int, step: int) -> int:
        value = 0
        if vertical_val == 1:
            second_list = [0,1]
        elif vertical_val == puzzle_matrix.shape[1]:
            second_list = [-1,0]
        else:
            raise ValueError("Wrong Size")
        for comp_1, comp_2 in itertools.product([-1,0,1], second_list):
            if not (comp_1 == 0 and comp_2 == 0):
                value += puzzle_matrix[step + comp_1 - 1, vertical_val + comp_2 - 1]
        return value
    
    def get_interior_values(self, puzzle_matrix: np.array) -> int:
        counter = 0
        for horizontal_val in range(1, puzzle_matrix.shape[1]-2):
            for vertical_val in range(1, puzzle_matrix.shape[0]-2):
                if puzzle_matrix[horizontal_val-1, vertical_val-1] == 1:
                    if self.get_internal_adjacent_sum(puzzle_matrix, horizontal_val, vertical_val) < 4:
                        counter += 1
        return counter
    
    def get_exterior_values(self, puzzle_matrix: np.array) -> int:
        counter = 0
        for horizontal_val in [1, len(puzzle_matrix)]:
            for steps in range(1, len(puzzle_matrix)-1):
                if puzzle_matrix[horizontal_val-1, steps] == 1:
                    if self.get_horizontal_adjacent_sum(puzzle_matrix, horizontal_val, steps) < 4:
                        counter += 1
        for vertical_val in [1, len(puzzle_matrix)]:
            for steps in range(1, puzzle_matrix.shape[1]-1):
                if puzzle_matrix[steps, vertical_val-1] == 1:
                    if self.get_vertical_adjacent_sum(puzzle_matrix, vertical_val, steps) < 4:
                        counter += 1
        return counter
    
    def get_corner_values(self, puzzle_matrix: np.array) -> int:
        counter = 0
        for val_1, val_2 in itertools.product([0, puzzle_matrix.shape[0]-1], [0, puzzle_matrix.shape[1]-1]):
            if puzzle_matrix[val_1, val_2] == 1:
                counter += 1
        return counter
    
    def process_puzzle(self) -> int:
        puzzle_matrix = self.create_puzzle_matrix()
        return self.get_interior_values(puzzle_matrix) + self.get_exterior_values(puzzle_matrix) + self.get_corner_values(puzzle_matrix)

if __name__ == "__main__":
    puzzle_input = "..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n@.@.@@@.@."
    with open(file_path, "r") as f:
        puzzle_input = f.read()
    checker = DayFourClass(puzzle_input = puzzle_input)
    outcome = checker.process_puzzle()
    print(f"Number of papers accessible by forklift is: {outcome}")