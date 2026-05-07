class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_map = {}
        result = []

        freq_bucket = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hash_map[n] = 1 + hash_map.get(n, 0)


        for n, f in hash_map.items():
            freq_bucket[f].append(n)

        # print(freq_bucket)

        for n in range(len(freq_bucket) -1, 0, -1):
            for m in freq_bucket[n]:
                result.append(m)
                if len(result) == k:
                    return result
        