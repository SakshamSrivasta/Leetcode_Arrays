class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        m=len(num)
        n=m-1
        trailing_zeroes=0
        while n>=0:
            if num[n]=="0":
                trailing_zeroes+=1
            else:
                break
            n-=1
        return num[:m-trailing_zeroes]
                



