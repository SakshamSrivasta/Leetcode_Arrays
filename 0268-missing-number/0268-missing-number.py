class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=sum(nums)
        sum_of_elements_present= (n*(n+1))//2
        return sum_of_elements_present-total