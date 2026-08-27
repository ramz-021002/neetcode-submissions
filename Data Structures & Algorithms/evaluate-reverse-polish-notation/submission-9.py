class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        expMap = {'+': 0, '-': 1, '*': 2, '/': 3}


        for t in tokens:
            if t in expMap:
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                if t == '+':
                   stack.append(val1 + val2)
                elif t == '-':
                    stack.append(val2 - val1)
                elif t == '*':                        
                    stack.append(val1 * val2)
                elif t == '/':
                    stack.append(int(val2 / val1))

            else:
                stack.append(t)

        return int(stack.pop())
