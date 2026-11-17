class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        counter_s1 = Counter(s1)
        counter = Counter(s2[:len(s1)])

        if counter == counter_s1:
            return True

        
        for i in range(len(s1), len(s2)):
            key = s2[i]
            counter[key] += 1
            counter[s2[i - len(s1)]] -= 1
            if counter[s2[i - len(s1)]] == 0:
                del counter[s2[i - len(s1)]]

            if counter == counter_s1:
                return True

            

        return False
        