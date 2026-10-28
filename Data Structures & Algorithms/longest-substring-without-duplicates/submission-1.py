class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}

        left = 0
        longst = 0

        for right in range(len(s)):
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)
            
            longst = max((right - left + 1), longst)
            char_map[s[right]] = right

        return longst



        