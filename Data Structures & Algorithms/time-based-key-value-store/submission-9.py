class TimeMap:

    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]
        
    def get(self, key: str, timestamp: int) -> str:

        if key not in self.time_map:
            return ""

        stamps = self.time_map[key]

        left = 0
        right = len(stamps) - 1

        while left <= right:
            mid = (right - left) // 2 + left
            if stamps[mid][1] == timestamp:
                return stamps[mid][0]
            elif stamps[mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        return stamps[right][0] if right >= 0 else ''


        
