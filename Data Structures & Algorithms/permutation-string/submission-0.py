class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False

        # Create two separate char lists to compare
        # they hold the keys and values (freq).. so they match.. they are same (order may vary)
        s1_map = [0] * 26 # [0, 0, 0, ..]
        s2_map = [0] * 26

        # Fill in the maps to the length of small one first

        # s1 - Subset / smaller, s2 - big

        for l in range(len(s1)):
            s1_map[ord(s1[l]) - ord('a')] += 1        # ord('a') = 97, then 97-97 => a is 0, b is 1 and so on..
            s2_map[ord(s2[l]) - ord('a')] += 1        # this makes the idx of the lists assoicate with the alphabets

        matches = 0             # counter to check for the matches, by both letter and freq..

        # get the matches; target is to get matches as 26, meaning same compelte set of alphas in both
        # though the smaller one has few nums, other chars are initiated using 0s.

        for i in range(26):
            if s1_map[i] == s2_map[i]:
                matches += 1
        
        # now create the window and keep checking

        l = 0
        for r in range(len(s1), len(s2)): # start from len(s1) as it is aleady done till there above
            if matches == 26: # if any point, they match, return True
                return True
            
            idx = ord(s2[r]) - ord('a')         # just get the idx for the maps
            s2_map[idx] += 1                    # add it to the map, the next char in the window
            if s1_map[idx] == s2_map[idx]:       # if they match at the same idx
                matches += 1                     # increment the matches

            elif s1_map[idx] + 1 == s2_map[idx]: # but, if there is aleady one more of such letter, decrement the match {a: 2 -> a:1}
                matches -= 1

            idx = ord(s2[l]) - ord('a')
            s2_map[idx] -= 1
            if s1_map[idx] == s2_map[idx]:
                matches += 1
            elif s1_map[idx] - 1 == s2_map[idx]:
                matches -= 1
            l += 1

        return matches == 26






        