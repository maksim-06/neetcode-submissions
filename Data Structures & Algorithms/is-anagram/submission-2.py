class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        else:
            dictionary = {}
            for i in range(len(s)):
                if s[i] not in dictionary:
                    dictionary[s[i]] = 1
                else:
                    dictionary[s[i]] += 1

            f=0
            for i in range(len(t)):
                if t[i] in dictionary:
                    if t.count(t[i]) != dictionary[t[i]]:
                        f=1
                        return False
                else:
                    f=1
                    return False

            if f == 0:
                return True