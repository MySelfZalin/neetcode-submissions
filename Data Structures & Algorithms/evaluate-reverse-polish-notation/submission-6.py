class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char not in {'+', '-', '*', '/'}:
                stack.append(int(char))

            else:
                second_val = stack.pop()
                first_val = stack.pop()

                if char == "+":
                    stack.append(first_val + second_val)

                elif char == "-":
                    stack.append(first_val - second_val) 

                elif char == "*":
                    stack.append(first_val * second_val)  

                elif char == "/":
                        stack.append(int(first_val / second_val))


        return stack[0]                                  