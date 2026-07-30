class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        x=sorted(nums)
        for i in range(len(x)):
            x[i]-=1
        return x[-1]*x[-2]

        # nums.sort()
        # return (nums[-1] - 1) * (nums[-2] - 1)