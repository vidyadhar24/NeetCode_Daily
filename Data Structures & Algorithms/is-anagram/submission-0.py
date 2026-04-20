class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_table = {}
        for ltr in s:
            if ltr not in hash_table:
                hash_table[ltr] = 1
            else:
                hash_table[ltr] += 1
        
        hash_table_2 = {}


        for ltr in t:
            if ltr not in hash_table_2:
                hash_table_2[ltr] = 1
            else:
                hash_table_2[ltr] += 1
                
        for ltr in hash_table:
            if ltr not in hash_table_2:
                return False
            elif hash_table[ltr] != hash_table_2[ltr]:
                return False
        return True

