# Didn't solve this. Too time consuming. The key to solving this is 
# 1. A way to save the formulars and trigger recalculation when a new set command changed any of the value that affects the formula.
# 2. Delete a formula when a new set command overwirtes it.

class Excel:

    def __init__(self, height: int, width: str):
        self.height = height # Input hiehgt - 1.
        self.width = ord(width) - ord('A') + 1 # ord(input_char) - ord('A')
        self.sheet = [[0] * self.width for _ in range(self.height)]
        # Need a structure to save the formula, also need a logic to delete the formula if the target cell is re-set.
        self.formula = {}

    def _cell_in_range(self, row, column, my_range):
        # Create range.
        cell_list = []
        seperator = my_range.find(':')
        upper_left = my_range[0:seperator]
        upper_left_col = ord(upper_left[0]) - ord('A')
        upper_left_row = int(upper_left[1:]) - 1
        lower_right = my_range[seperator+1:]
        lower_right_col = ord(lower_right[0]) - ord('A')
        lower_right_row = int(lower_right[1:]) - 1
        for this_row in range(upper_left_row, lower_right_row +1):
            for this_col in range(upper_left_col, lower_right_col+1):
                cell_list.append([this_row, this_col])

        to_check_row = row - 1
        to_check_col = ord(column) - ord('A')

        return ([to_check_row, to_check_col] in cell_list)

    def _is_recalculate(self, row:int, column: str):
        for key, values in self.formula.items():
            # Check key.
            if row == key[0] and column == key[1]:
                yield key[0], key[1], values
            # Check value.
            for value in values:
                # Single cell.
                if len(value) <=3:
                    if value == column + str(row):
                        yield key[0], key[1], values
                else:
                    # A range, check if cell in the range.
                    if self._cell_in_range(row, column, value):
                        yield key[0], key[1], values


    def set(self, row: int, column: str, val: int) -> None:
        self.sheet[row-1][ord(column) - ord('A')] = val
        # Delete saved formula if current set overwrites it.
        for key, _ in self.formula.items():
            if key[0] == column and key[1] == row:
                del self.formula[key]
        # Check if current set affect any of the saved formula.
        for re_row, re_column, values in self._is_recalculate(row, column):
            self.sum(re_row, re_column, values)

    def get(self, row: int, column: str) -> int:
        return self.sheet[row-1][ord(column) - ord('A')]
        
    def sum(self, row: int, column: str, numbers: list[str]) -> int:
        self.formula[(row, column)] = numbers

        sum = 0
        to_set_row = row - 1
        to_set_col = ord(column) - ord('A')

        for num in numbers:
            # Single cell.
            if len(num) <= 3:
                col = ord(num[0]) - ord('A')
                row = int(num[1:]) - 1
                sum += self.sheet[row][col]
            else:
                # A range of cells.
                seperator = num.find(':')
                upper_left = num[0:seperator]
                upper_left_col = ord(upper_left[0]) - ord('A')
                upper_left_row = int(upper_left[1:]) - 1
                lower_right = num[seperator+1:]
                lower_right_col = ord(lower_right[0]) - ord('A')
                lower_right_row = int(lower_right[1:]) - 1

                for row in range(upper_left_row, lower_right_row +1):
                    for col in range(upper_left_col, lower_right_col+1):
                        sum += self.sheet[row][col]

        self.sheet[to_set_row][to_set_col] = sum 
        return sum


        


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)