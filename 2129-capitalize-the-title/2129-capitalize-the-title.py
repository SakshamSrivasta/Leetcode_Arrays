class Solution:
    def capitalizeTitle(self, title: str) -> str:
        # words=title.split()
        # for i in range(len(words)):
        #     word_len=len(words[i])
        #     if word_len<=2:
        #         words[i].lower()
        #     else:
        #         words[i]=words[i][0].capitalize()+words[i][1::].lower()
        # return ''.join(words)
        words = title.split()
        for i in range(len(words)):
            word_len = len(words[i])
            
            if word_len <= 2:
                words[i] = words[i].lower()
            else:
                words[i] = words[i].capitalize()
        
        return " ".join(words)