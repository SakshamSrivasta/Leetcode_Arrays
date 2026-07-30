class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        #USING 2 POINTER
        
        if ch not in word:
            return word
        idx=word.index(ch)
        if idx==-1:
            return word
        left,right=0,idx
        wor=list(word)
        while left<right:
            wor[left],wor[right]=wor[right],wor[left]
            left+=1
            right-=1
        return ''.join(wor)
        
        #USING JUST SLICING
        # if ch not in word:
        #     return word
        # idx=word.index(ch)
        # return word[:idx+1][::-1]+word[idx+1:]

        #USING TRY AND EXCEPT
        # try:
        #     idx=word.index(ch)
        #     return word[:idx+1][::-1]+word[idx+1:]
        # except ValueError:
        #     return word
        