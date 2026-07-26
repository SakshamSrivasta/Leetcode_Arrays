class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        numbers=sorted(nums)
        x=numbers[-1]*numbers[-2]*numbers[-3]
        y=numbers[0]*numbers[1]*numbers[-1]
        return max(x,y)