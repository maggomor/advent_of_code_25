from pydantic import BaseModel
import numpy as np

class DayOneClass(BaseModel):
    location: int
    
    def spin(self, direction: str, steps: int):
        if direction.upper() == "R":
            multiplier = 1
        elif direction.upper() == "L":
            multiplier = -1
        else:
            raise ValueError("The Direction Command is invalid")
        result = self.location + multiplier * steps
        while result < 0:
            result += 100
        while result >= 100:
            result -= 100
        self.location = result
        return result 
    
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
        new_location = self.spin(direction, steps)
        return new_location
    
    def spin_through_list(self, input_list: list) -> list:
        return [self.get_new_location(item) for item in input_list]
    
    def count_zeros(self,input_list: list) -> int:
        return int(len(input_list) - np.count_nonzero(np.array(input_list)))
    
    def safecracking(self, input_list: list) -> int:
        return_list = self.spin_through_list(input_list)
        password = self.count_zeros(return_list)
        return password

if __name__ == "__main__":
    list_one = ["L50", "L12", "R48", "R17", "R97", "L12", "L15"]
    checker = DayOneClass(location = 50)
    outcome = checker.safecracking(list_one)
    print(f"Password is: {outcome}")