import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b),
        }
        stack = []
        for token in tokens:
                if token in ops:
                    a = stack.pop()
                    b = stack.pop()
                    ans = ops[token](b, a)
                    stack.append(ans)
                else:
                    stack.append(int(token))

        return stack[-1]


        