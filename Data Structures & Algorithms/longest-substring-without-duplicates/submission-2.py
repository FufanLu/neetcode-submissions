class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longst = 0
        left = 0

        counter = defaultdict(int)
        for right in range(len(s)):
            key = s[right]
            counter[key] += 1
            while counter[key] == 2:
                counter[s[left]] -= 1
                left += 1

            longst = max((right - left + 1), longst)

        return longst
                    
                    

        