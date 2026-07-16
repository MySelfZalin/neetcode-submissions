from collections import defaultdict

class Solution:
    def __init__(self):
        self.row = [set() for _ in range(9)]
        self.column = [set() for _ in range(9)]
        self.square = defaultdict(set)
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        for y, line in enumerate(board):
            for x, cell in enumerate(line):
                if cell != ".":

                    answer = self.is_uniq_char(x,y,cell)
                    if answer:
                        return False



                    self.row[y].add(cell)
                    self.column[x].add(cell)

                    x_square = x // 3
                    y_square = y // 3
                    self.square[(x_square,y_square)].add(cell)
        return True            


    def is_uniq_char(self,x: int, y: int, val: str) -> bool:
        if val in self.row[y]:
            return True
        if val in self.column[x]:
            return True
        if val in self.square[(x // 3, y // 3)]:
            return True

        return False               

