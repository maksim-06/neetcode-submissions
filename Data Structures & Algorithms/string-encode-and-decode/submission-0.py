class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res += str(len(i)) + '#' + i
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            lenght = int(s[i:j])
            stroka = s[j + 1: j + 1 + lenght]
            res.append(stroka)

            i = j + 1 + lenght

        return res

