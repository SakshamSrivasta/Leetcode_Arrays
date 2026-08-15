class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        floor=0
        time=0
        for r in requests:
            time+=abs(r-floor)
            floor=r
        return time