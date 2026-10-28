class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        ans = []
        path = []
        total = 0

        def backTracking(index):
            nonlocal total
            if total == target:
                ans.append(path[:])
                return

            if total > target or index == len(candidates):
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                total += candidates[i]
                path.append(candidates[i])

                backTracking(i+1)

                path.pop()
                total -= candidates[i]

        backTracking(0)

        return ans


