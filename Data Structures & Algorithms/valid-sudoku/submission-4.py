class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        leng = len(board)
        
        rows = [set() for _ in range(leng)]
        cols = [set() for _ in range(leng)]
        boxes = [set() for _ in range(leng)]
# [set(), set(), set(), set(), set(), set(), set(), set(), set()]

        for row in range(leng):
            for col in range(leng):
                box_id = (row // 3) * 3 + (col // 3)
                # print(f'row = {row}, col = {col}, box_id={box_id}')

                value = board[row][col]

                if value == '.':
                    continue

                if (value in rows[row] )| (value in cols[col]) | (value in boxes[box_id]):
                    return False

                rows[row].add(value)
                cols[col].add(value)
                boxes[box_id].add(value)

        return True