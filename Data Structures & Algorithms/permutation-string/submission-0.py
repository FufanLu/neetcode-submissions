class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        count_s2 = Counter(s2[:len(s1)])

        if count_s1 == count_s2:
            return True

        for i in range(len(s1), len(s2)):
            if s2[i] in count_s2:
                count_s2[s2[i]] += 1
            else:
                count_s2[s2[i]] = 1

            old_char = s2[i - len(s1)]
            count_s2[old_char] -= 1
            if count_s2[old_char] == 0:
                del count_s2[old_char]

            if count_s2 == count_s1:
                return True

        return False

        
        
        