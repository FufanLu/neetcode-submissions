class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t) or not s:
            return ""


        need = Counter(t)
        missing = len(t)
        start = 0
        left = 0
        length = float('inf')

        for right, char in enumerate(s):
            if need[char] > 0:
                missing -= 1

            need[char] -= 1

            while missing == 0:
                if right - left + 1 < length:
                    start = left
                    length = right - left + 1
                
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        

        return '' if length == float('inf') else s[start : start + length]
        



        