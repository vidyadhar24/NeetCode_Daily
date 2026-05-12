class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]   # set(), set(), set(), set(), set(), set(), set(), set(), set()]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]


        # let's map all the rows from 0 - 8 and cols also 0 - 8

        for row in range(9):
            for col in range(9):    # to traverse through coordinates like (0, 0) for fist cell, (8, 8) for last cell

                box_id = (row // 3) * 3 + (col // 3)  # maps every cell to one of 9 boxes (numbered 0–8 left-to-right, top-to-bottom)

                # e.g. cell (4, 7) → box_id = (4÷3)x3 + (7÷3) = 1x3 + 2 = 5.   total boxes being 9 ( 0  - 8 as 012 in the first line, 345, 678 in 2nd and 3rd lines)

                value = board[row][col]   # get the actual value from the cell

                if value == ".":
                    continue         # skip the empty cells

                if value in rows[row] or value in cols[col] or value in boxes[box_id]:
                    return False

                rows[row].add(value)  # add to the rows set
                cols[col].add(value)
                boxes[box_id].add(value)
        
        
        return True         # if no duplicates exist


    # the idea is to have three lists and to check for duplicates in the same
    # this is achieved using 'Hash sets'
    # one set for each row, one for each col and one for each box (3, 3)
    # using coordinates is the trick here. ***> IMP
    # just loop through each cell from left to right, using co-ordinates and then assign the value to
    # the respective row, col and box and check for the duplicates at the same time ( before assigning acually)
