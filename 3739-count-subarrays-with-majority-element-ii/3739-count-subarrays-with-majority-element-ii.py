from sortedcontainers import SortedList
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:

        prefix = 0
        ans = 0

        seen = SortedList([0])

        for x in nums:

            if x == target:
                prefix += 1
            else:
                prefix -= 1

            ans += seen.bisect_left(prefix)

            seen.add(prefix)

        return ans