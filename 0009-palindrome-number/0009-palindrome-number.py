class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        original =x
        if x<0:
            return False
        while x>0:
            rev=(rev*10 )+ (x%10)
            x//=10
        return rev==original


        