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
        
        
        for ltr in t:
                if ltr not in hash_table and len(hash_table) > 0:
                    return False
                else:
                    hash_table[ltr] -= 1
                    if hash_table[ltr] < 0:
                        return False
        return True
