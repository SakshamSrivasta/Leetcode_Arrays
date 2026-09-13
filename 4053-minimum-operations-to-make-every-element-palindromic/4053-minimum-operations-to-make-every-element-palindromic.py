import bisect

# Global precomputation so it runs only ONCE across all test cases
EVENS = []
ODDS = []

def _precompute():
    palindromes = set()
    
    # Generate palindromes by mirroring prefixes up to 5 digits (covers up to 10^9)
    for i in range(1, 100000):
        s = str(i)
        
        # Odd length palindrome: e.g., '12' -> '121'
        p1 = int(s + s[:-1][::-1])
        palindromes.add(p1)
        
        # Even length palindrome: e.g., '12' -> '1221'
        p2 = int(s + s[::-1])
        palindromes.add(p2)
        
    # Include upper bound boundary safety
    palindromes.add(1000000001)

    # Sort into separate parity arrays
    for p in sorted(palindromes):
        if p > 0:
            if p % 2 == 0:
                EVENS.append(p)
            else:
                ODDS.append(p)

# Precompute globally on module import
_precompute()


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        total_ops = 0
        
        for x in nums:
            target_list = EVENS if x % 2 == 0 else ODDS
            
            # Binary search for closest palindrome
            idx = bisect.bisect_left(target_list, x)
            
            min_diff = float('inf')
            
            # Check candidate at idx
            if idx < len(target_list):
                min_diff = min(min_diff, abs(x - target_list[idx]))
                
            # Check candidate at idx - 1
            if idx > 0:
                min_diff = min(min_diff, abs(x - target_list[idx - 1]))
                
            total_ops += min_diff // 2
            
        return total_ops