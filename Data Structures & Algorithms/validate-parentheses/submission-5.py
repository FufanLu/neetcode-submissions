class Solution:
    def isValid(self, s: str) -> bool:

        parentheses = {
            "]" : '[',
            '}' : '{',
            ')' : '('
        }
        

        stack = []

        for char in s:
            if char not in parentheses:
                stack.append(char)

            elif not stack or stack[-1] != parentheses[char]:
                return False

            else:
                stack.pop()


        return not stack