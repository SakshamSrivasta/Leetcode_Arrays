class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        n=len(num)
        m=n-1
        len_trailing_zeroes=0
        while (m>=0):
            if num[m]=="0":
                len_trailing_zeroes+=1
            else:
                break
            m-=1
        return num[:n-len_trailing_zeroes]



