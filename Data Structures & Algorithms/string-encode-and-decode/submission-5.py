class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f'{len(s)}#{s}'

        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []
        i = 0

        while i < len(s):
            total = 0
            j = i

            while j <= len(s) and s[j] != '#':
                total = (total * 10) + int(s[j])
                j += 1
            
            res.append(s[j + 1 : j+1+total])

            i = j + total + 1

        return res
            
