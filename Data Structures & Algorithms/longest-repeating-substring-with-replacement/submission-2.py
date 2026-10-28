class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        freq_num = 0

        ans = 0

        for right in range(len(s)):
            char = s[right]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

            freq_num = max(freq_num, count[char])

            while right - left + 1 - freq_num > k:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        
        return ans

            
