class Solution:
    def maxIceCream(self, costs, coins):

        freq={}

        for c in costs:
            freq[c]=freq.get(c,0)+1

        count=0

        for price in sorted(freq):

            buy=min(
                freq[price],
                coins//price
            )

            count+=buy
            coins-=buy*price

        return count