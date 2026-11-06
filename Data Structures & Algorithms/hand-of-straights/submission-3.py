class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        counter = Counter(hand)


        for i in sorted(counter):
            need = counter[i]
            if need == 0:
                continue

            for j in range(i, i + groupSize):
                if counter[j] < need:
                    return False

                counter[j] -= need

            counter[i] -= need

        return True
        