class Solution(object):
    def countAsterisks(self, s):
        bar = False
        count = 0
        for x in s:
            if x=='|':
                bar = not bar
                
            if x=='*' and bar==False:
               count+=1
            
        return count