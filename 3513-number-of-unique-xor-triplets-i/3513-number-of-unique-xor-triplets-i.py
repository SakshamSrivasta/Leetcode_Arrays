class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        if n == 2:
            return 2

        highest = 1 << (n.bit_length() - 1)
        return highest << 1