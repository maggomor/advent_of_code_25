from pydantic import BaseModel
import numpy as np
import itertools

from pathlib import Path

file_path = Path(__file__).parent / "../no_push/inputs/day2.txt"


class DayTwoClass(BaseModel):
    product_ids: str
    
    def get_ordered_list_of_ids(self) -> list:
        ids_list = self.product_ids.split(",")
        ordered_list = [x.split("-") for x in ids_list]
        return ordered_list
    
    def check_repeating_numbers(self, list_input: list) -> int:
        invalid_ids = []
        for number in range(int(list_input[0]), int(list_input[1])+1):
            number_str = str(number)
            if len(number_str) % 2 != 0:
                pass
            else:
                for increment in range(1,len(number_str)+1):
                    if number_str[0:increment] * int((len(number_str) / increment)) == number_str:
                        if int(len(number_str) / increment) == 2:
                            invalid_ids.append(int(number_str))
        return invalid_ids 
    
    def process_product_ids(self) -> int:
        all_invalid_ids = []
        ordered_lists = self.get_ordered_list_of_ids()
        for number_pair in ordered_lists:
            all_invalid_ids.append(self.check_repeating_numbers(number_pair))
        flattened_list = list(itertools.chain(*all_invalid_ids))
        sum_number = np.sum(np.array(flattened_list))
        return int(sum_number)


if __name__ == "__main__":
    with open(file_path, "r") as f:
        product_ids = f.read()
    #product_ids = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    checker = DayTwoClass(product_ids = product_ids)
    outcome = checker.process_product_ids()
    print(f"Sum of all invalid IDs is: {outcome}")