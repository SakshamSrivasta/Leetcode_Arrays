class Solution:
    def maxIceCream(self, costs, coins):
        # dictt={}
        # for i in range(len(costs)):
        #     if costs[i] in dictt:
        #         dictt[costs[i]]+=1
        #     else:
        #         dictt[costs[i]]=1
        # count =0
        # for price in sorted(dictt):
        #     buy=min(dictt[price],coins//price)
        #     count+=buy
        #     coins-=buy*price
        # return count

        dictt={}
        for c in costs:
            dictt[c]=dictt.get(c,0)+1
        count=0
        for price in sorted(dictt):
            buy=min(dictt[price],coins//price)
            count+=buy
            coins-=price*buy
        return count