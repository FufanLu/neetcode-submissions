class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse = True)
        times = [(target - p) / v for p, v in cars]

        stack = []

        for time in times:
            if stack and stack[-1] >= time:
                continue

            stack.append(time)

        return len(stack)
        