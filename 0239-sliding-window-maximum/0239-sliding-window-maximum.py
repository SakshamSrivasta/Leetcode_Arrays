from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #BRUTE FORCE
        # n=len(nums)
        # ans=[]
        # if k>n:
        #     return [max(nums)]
        # for i in range(n-k+1):
        #     window_max=float("-inf")
        #     for j in range(i,i+k):
        #         if nums[j]>window_max:
        #             window_max=nums[j]
        #     ans.append(window_max)
        #  return ans

        #OPTIMAL- MONOTONIC DECREASING DEQUE
        ans=[]
        dq=deque()
        for i in range(len(nums)):
            while dq and dq[0]<=i-k:
                dq.popleft()
            while dq and nums[i]>nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i>=k-1:
                ans.append(nums[dq[0]])
        return ans
            








    














      