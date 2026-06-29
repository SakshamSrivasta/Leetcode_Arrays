class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:

        #for pattern in patterns:

            # Check if pattern exists inside word
           # if pattern in word:
              #  count += 1

        #return count
        count = 0

        for pattern in patterns:

            found = False

            for i in range(len(word) - len(pattern) + 1):

                if word[i:i + len(pattern)] == pattern:
                    found = True
                    break

            if found:
                count += 1

        return count