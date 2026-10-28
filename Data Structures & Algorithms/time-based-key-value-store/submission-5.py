class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
            return ""
        times = self.store[key]
        left = 0
        right = len(times) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if times[mid][0] == timestamp:
                return times[mid][-1]
            elif times[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        return times[right][-1] if right >= 0 else ""
        
