class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        hash_dict = defaultdict(list)  # to add the key if it doesn't exist
        




        for word in strs:
            chars_map = [0] * 26 # A place holder for chars [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # this map is used for each word in the word, and then  that list is compared with other words in the list 
            for ltr in word:
                alphs_pos = ord(ltr) - ord('a') # setting the pos for each letter from 0-25 (idx of list); ex: char(a) - char(a) = 80 - 80 = 0 | char(b) - char(a) = 81 - 80 = 1 
                chars_map[alphs_pos] += 1 # only increasing the count of that letter by its index, not adding the letter itself
            hash_dict[tuple(chars_map)].append(word) # adding as tuple because a list(mutable) can't be a key in dictionary

        # print(hash_dict)
        ''' defaultdict(
            <
            class
            'list'
            >
            , {(1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['act', 'cat'], (
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0): ['pots', 'tops', 'stop'], 
            (1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['hat']})

        '''
        return (list(hash_dict.values()))