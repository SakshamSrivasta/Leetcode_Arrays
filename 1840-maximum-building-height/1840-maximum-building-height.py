class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        if restrictions and restrictions[-1][0] != n:
            restrictions.append([n, n-1])
        restrictions.sort()
        m = len(restrictions)
        # Forward pass
        for i in range(1, m):
            d = restrictions[i][0] - restrictions[i-1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + d)
        # Backward pass
        for i in range(m-2, -1, -1):
            d = restrictions[i+1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + d)
        # Find max peak
        ans = 0
        for i in range(1, m):
            left, h1 = restrictions[i-1]
            right, h2 = restrictions[i]
            d = right - left
            peak = (h1 + h2 + d) // 2
            ans = max(ans, peak)
        return ans







        