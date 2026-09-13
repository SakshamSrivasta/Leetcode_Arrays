class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        n = len(grid)

        for i in range(n):
            if rowShift[i]:
                grid[i] = grid[i][rowShift[i]:] + grid[i][:rowShift[i]]
        
        for i in range(n):
            if colShift[i]:
                li = []
                j = x = 0
                
                while j < n:
                    if j < colShift[i]:
                        li.append(grid[j][i])
                    else:
                        grid[x][i] = grid[j][i]
                        x += 1

                    j += 1

                j = 0

                while x < n:
                    grid[x][i] = li[j]
                    j += 1
                    x += 1

        return grid