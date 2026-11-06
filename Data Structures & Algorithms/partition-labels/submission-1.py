class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        c = defaultdict(int)

        left = 0
        ans = []
        end = 0

        for i, v in enumerate(s):
            c[v] = i

        for right in range(len(s)):
            end = max(c[s[right]], end)
            if end == right:
                ans.append(right - left + 1)
                left = right + 1
            
        return ans


        