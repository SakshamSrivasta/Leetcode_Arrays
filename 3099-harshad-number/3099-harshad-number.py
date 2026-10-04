class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        if x<10:
            return x
        digit_sum=sum(int(digit) for digit in str(x))
        return digit_sum if x%digit_sum==0 else -1
        