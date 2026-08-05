class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Revised on 5th Aug 2026

        hashDict = defaultdict(list)

        for wrd in strs:
            char_map = 26 * [0]

            for ltr in wrd:
                rel_idx = ord(ltr) - ord('a')
                char_map[rel_idx] += 1

            hashDict[tuple(char_map)].append(wrd)

        return list(hashDict.values())
        