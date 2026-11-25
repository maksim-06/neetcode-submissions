class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stroka = ''
        max_len = 0
        for i in s:
            if i not in stroka:
                stroka += i
            else:
                max_len = max(max_len, len(stroka))
                ind = stroka.index(i)
                stroka = stroka[ind + 1:] + i
        max_len = max(max_len, len(stroka))
        return max_len
        
        