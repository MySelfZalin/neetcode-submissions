from collections import defaultdict

class Solution:

    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        square = defaultdict(set)

        def is_uniq_char(x: int, y: int, val: str) -> bool:
            if val in row[y]:
                return True
            if val in column[x]:
                return True
            if val in square[(x // 3, y // 3)]:
                return True

            return False 
        
        for y, line in enumerate(board):
            for x, cell in enumerate(line):
                if cell != ".":

                    answer = is_uniq_char(x,y,cell)
                    if answer:
                        return False



                    row[y].add(cell)
                    column[x].add(cell)

                    x_square = x // 3
                    y_square = y // 3
                    square[(x_square,y_square)].add(cell)
        return True            


                  

