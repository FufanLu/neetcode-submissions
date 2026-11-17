class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        char_map = defaultdict(int)

        left = 0
        longst = 0
        max_freq = 0

        for right in range(len(s)):
            char_map[s[right]] += 1
            max_freq = max(char_map[s[right]], max_freq)

            if (right - left + 1 - max_freq) > k:
                char_map[s[left]] -= 1
                left += 1

            longst = max(longst, (right - left + 1))

        return longst


        
        