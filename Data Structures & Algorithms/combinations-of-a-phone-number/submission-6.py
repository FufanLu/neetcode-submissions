class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        word_dict = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        
        path = []
        ans = []

        def backTracking(index):
            if index == len(digits):
                ans.append(''.join(path[:]))
                return

            num = digits[index]
            for char in word_dict[num]:
                path.append(char)
                backTracking(index + 1)
                path.pop()

        backTracking(0)

        return ans



        