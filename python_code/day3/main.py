from pydantic import BaseModel
import numpy as np
from pathlib import Path

file_path = Path(__file__).parent / "../no_push/inputs/day3.txt"
def argmax(iterable):
    return max(enumerate(iterable), key=lambda x: x[1])[0]

class DayThreeClass(BaseModel):
    joltage_ratings: str
    
    def get_list_of_joltages(self) -> list:
        joltage_ratings_list = self.joltage_ratings.split("\n")
        return joltage_ratings_list
    
    def list_battery_bank(self, battery_input: str) -> list:
        return [int(battery_input[num]) for num in range(len(battery_input))]
    
    def process_battery_bank(self, battery_input: str) -> int:
        result = self.list_battery_bank(battery_input)
        first_val = argmax(result[:-1])
        second_val = first_val + 1 + argmax(result[first_val+1:])
        return int(str(result[first_val]) + str(result[second_val]))
    
    def process_joltage_ratings(self) -> int:
        value = 0
        joltage_ratings_list = self.get_list_of_joltages()
        for joltage_rating in joltage_ratings_list:
            value += self.process_battery_bank(joltage_rating)
        return value

if __name__ == "__main__":
    with open(file_path, "r") as f:
        joltage_ratings = f.read()
    checker = DayThreeClass(joltage_ratings = joltage_ratings)
    outcome = checker.process_joltage_ratings()
    print(f"Sum of Joltages is: {outcome}")