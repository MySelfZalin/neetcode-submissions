from collections import heapq

class MinStack:

    def __init__(self):
        self.curr_min = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.curr_min:
            self.curr_min.append(val)
            return

        last_min = self.curr_min[-1]
        if val < last_min:
            self.curr_min.append(val)
        else:
            self.curr_min.append(last_min) 

    def pop(self) -> None:
        self.curr_min.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.curr_min[-1]

        
