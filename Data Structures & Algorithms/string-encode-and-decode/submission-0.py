class Solution:

    def encode(self, strs: List[str]) -> str:
        
        # result_str = ""
        # delimiter = "@"
        # temp_str = ""
        # counter = 0

        # for wrd in strs:
        #     for ltr in wrd:
        #         temp_str += ltr
        #         counter += 1
        # result_str += str(counter) + delimiter + temp_str
        # temp_str = ""
        # counter = 0

        result_str = ""
        for wrd in strs:
            result_str += str(len(wrd)) + '@' + wrd

        return result_str



    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '@':
                j += 1
            length = int(s[i:j])
            result.append(s[j+1 : j+1+length])
            i = j+1+length

        return result
