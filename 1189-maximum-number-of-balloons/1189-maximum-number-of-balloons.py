class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dictt=defaultdict(int)
        balloon="balloon"
        for c in text:
            if c in balloon:
                dictt[c]+=1
        if any(c not in dictt for c in balloon):
            return 0
        else:
            return min(dictt['b'],dictt['a'],dictt['l']//2,dictt['o']//2,dictt['n'])


        