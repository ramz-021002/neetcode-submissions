class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        exp = ['+', '-', '*', '/']

        for t in tokens:
            if t in exp:
                val = 0
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                if t == '+':
                   val = val1 + val2
                elif t == '-':
                    val = val2 - val1
                elif t == '*':                        
                    val = val1 * val2
                elif t == '/':
                    val = int(val2 / val1)
                
                stack.append(val)
            else:
                stack.append(t)

        return int(stack.pop())
