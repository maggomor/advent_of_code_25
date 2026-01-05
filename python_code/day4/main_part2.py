from pydantic import BaseModel
import numpy as np
import itertools
from pathlib import Path
from typing import Tuple

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
    
    def pad_matrix(self, input_matrix: np.array) -> np.array:
        matrix_length, matrix_width = input_matrix.shape[0], input_matrix.shape[1]
        padded_matrix = np.zeros([matrix_length+2, matrix_width+2])
        for i in range(matrix_length):
            for j in range(matrix_width):
                padded_matrix[i+1, j+1] = input_matrix[i,j]
        return padded_matrix
    
    def get_internal_adjacent_sum(self, puzzle_matrix: np.matrix, horizontal_val: int, vertical_val: int) -> int:
        value = 0
        for comp_1, comp_2 in itertools.product([-1,0,1],[-1,0,1]):
            if not (comp_1 == 0 and comp_2 == 0):
                value += puzzle_matrix[horizontal_val + comp_1, vertical_val + comp_2]
        return value
    
    def get_interior_values(self, puzzle_matrix: np.array) -> int:
        counter = 0
        coordinates = []
        for horizontal_val in range(1, puzzle_matrix.shape[1]):
            for vertical_val in range(1, puzzle_matrix.shape[0]):
                if puzzle_matrix[horizontal_val, vertical_val] == 1:
                    if self.get_internal_adjacent_sum(puzzle_matrix, horizontal_val, vertical_val) < 4:
                        counter += 1
                        coordinates.append((horizontal_val, vertical_val))
        return counter, coordinates
    
    def process_puzzle(self) -> int:
        puzzle_matrix = self.create_puzzle_matrix()
        padded_matrix = self.pad_matrix(puzzle_matrix)
        count, coordinates = self.get_interior_values(padded_matrix) #+ self.get_exterior_values(puzzle_matrix) + self.get_corner_values(puzzle_matrix)
        while len(coordinates) > 0:
            for horizontal_val, vertical_val in coordinates:
                puzzle_matrix[horizontal_val-1, vertical_val-1] = 0
            padded_matrix = self.pad_matrix(puzzle_matrix)
            new_count, coordinates = self.get_interior_values(padded_matrix)
            count += new_count
        return count

if __name__ == "__main__":
    puzzle_input = "..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n@.@.@@@.@."
    with open(file_path, "r") as f:
        puzzle_input = f.read()
    checker = DayFourClass(puzzle_input = puzzle_input)
    outcome = checker.process_puzzle()
    print(f"Number of papers accessible by forklift is: {outcome}")