class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse = True)
        times = [(target - p) / s for p, s in cars]

        stack = []
        for t in times:
            if stack and stack[-1] >= t:
                continue
            
            stack.append(t)

        
        return len(stack)
