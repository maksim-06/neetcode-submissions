class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        f = 0
        b = len(s) - 1
        stroka = 'abcdefghijklmnopqrstuvwxyz0123456789'
        while f < b:
            if s[f] not in stroka:
                f += 1
                continue

            if s[b] not in stroka:
                b -= 1
                continue

            if s[f] != s[b]:
                return False
            
            f += 1
            b -= 1

        return True
        