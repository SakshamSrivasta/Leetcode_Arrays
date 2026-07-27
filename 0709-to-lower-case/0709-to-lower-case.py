class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

        # result=""
        # for ch in s:
        #     if 65 <= ord(ch) <= 90:
        #         result+=chr(ord(ch)+32)
        #     else:
        #         result+=ch
        # return result
