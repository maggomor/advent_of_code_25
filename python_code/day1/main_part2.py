from pydantic import BaseModel
import numpy as np

from pathlib import Path

file_path = Path(__file__).parent / "../no_push/inputs/day1.txt"

class DayOneClass(BaseModel):
    location: int
    
    def spin(self, direction: str, steps: int):
        if direction.upper() == "R":
            multiplier = 1
        elif direction.upper() == "L":
            multiplier = -1
        else:
            raise ValueError("The Direction Command is invalid")
        print(f"Location is {self.location}, with direction {direction+str(steps)}")
        result = self.location + multiplier * steps
        counter = 0
        print(f"new location is {result}")
        flag = self.location == 0
        while result < 0:
            result += 100
            if ((not flag) and (result != 0)):
                counter += 1
                print(f"Adjusted to {result}, counter is {counter}")
        while result >= 100:
            result -= 100
            if ((result != 100) and (not flag) and (result != 0)):
                counter += 1
            print(f"Adjusted to {result}, counter is {counter}")
        self.location = result
        return result, counter
    
    def verify_input(self, input: str) -> bool:
        if input[0].upper() not in ["L", "R"]:
            raise ValueError("Wrong Direction")
        try:
            steps = int(input[1:])
        except:
            raise ValueError("Wrong Rotation: Input must be integer")
        return input[0].upper(), int(input[1:])
    
    def get_new_location(self, input: str) -> int:
        direction, steps = self.verify_input(input)
        new_location, counts = self.spin(direction, steps)
        return new_location, counts
    
    def spin_through_list(self, input_list: list) -> list:
        spin_list = [self.get_new_location(item) for item in input_list]
        location_list = [x[0] for x in spin_list]
        count_list = [x[1] for x in spin_list]
        return location_list, count_list
    
    def count_zeros(self,input_list: list) -> int:
        return int(len(input_list) - np.count_nonzero(np.array(input_list)))
    
    def safecracking(self, input_list: list) -> int:
        return_list, count_list = self.spin_through_list(input_list)
        password = self.count_zeros(return_list)
        counts = sum(count_list)
        return password, counts

if __name__ == "__main__":
    with open(file_path, "r") as f:
        puzzle_input = f.read()
    #puzzle_input = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"
    checker = DayOneClass(location = 50)
    outcome, counts = checker.safecracking(puzzle_input.split("\n"))
    print(f"Password is: {outcome}")
    print(f"Day 2 Password is {counts+outcome}")