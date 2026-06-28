class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #slicing
        #n=len(nums)
        #nums[:]=nums[n-k:]+nums[:n-k]
        #return nums

        #function using 
        #n=len(nums)
        #rotations=k%n # since agar array ki length 6 (n)hai, toh 6th rotation (k=6) par same array hi banjayegi rotate hokar, iska mtlb agar 6 leghtn ke array ko 10 baar rotate karana hai toh 7th 8th 9th 10th rotation consider krnege, baaki 1-6th roation kyu karani, iske liye hum 10%6 krdenge jisse humei 4 hi rotation karani pde aur required array miljaye
        #for _ in range(0,rotations):
        #    e=nums.pop()
        #    nums.insert(0,e)
        #return nums
        n=len(nums)
        k=k%n
        def reverse(nums,left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        reverse(nums,n-k,n-1)
        reverse(nums,0,n-k-1)
        reverse(nums,0,n-1)
        
