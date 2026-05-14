class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        '''
        Input: s = "Was it a car or a cat I saw?"

        Output: true

        '''

        '''

        Idea is to compare the first one with the last, second one with the second last ..

        only traversing through the half is enough, because the other half is already compared with by that time

        only caveat is the mid idx, though it is same for both even and odd, need to add idx + 1 for the even while looping

        [a,s,s,a]. -> 1 (idx)
        [a,s,a].   -> 1



        '''


        sentence = []
        for i in s:
            if i.isalpha() or i.isnumeric():
                sentence.append(i.upper())
        print(sentence)

        length = len(sentence)

        mid_idx = (length // 2)          # since it is int division, 3//2 == 1, 4 // 2 == 2, there will be '1' more of even

        

        if len(sentence) % 2 == 0:  # if the length is even
            for i in range(mid_idx):
                if sentence[i] != sentence[length -1 -i]:
                    return False
        
        if len(sentence) % 2 == 1:  # if the length is odd
            for i in range(mid_idx + 1):
                if sentence[i] != sentence[length -1 -i]:
                    return False
        
        return True
        
