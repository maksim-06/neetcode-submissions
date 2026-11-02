class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for i in strs:
            spisok = [0] * 26

            for j in i:
                ind = ord(j) - ord('a')
                spisok[ind] += 1
            
            key = tuple(spisok)

            if key not in dictionary:
                dictionary[key] = []
            
            dictionary[key].append(i)
        
        return list(dictionary.values())

        # O(nlog(n))
        # dictionary = {}

        # for i in strs:
        #     key = ''.join(sorted(i))

        #     if key not in dictionary:
        #         dictionary[key] = []

        #     dictionary[key].append(i)
        
        # return list(dictionary.values())

        