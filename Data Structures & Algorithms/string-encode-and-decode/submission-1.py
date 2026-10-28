class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f'{len(s)}#{s}'

        return res
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i

            while j < len(s) and s[j] != '#':
                j += 1

            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            ans.append(word)
            i = j + 1 + length

        return ans

