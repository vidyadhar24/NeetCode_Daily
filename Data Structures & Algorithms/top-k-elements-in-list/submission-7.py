class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Ex: [1,2,2,3,3]
        # nums = [1,2,2,3,3]
        
        frq_map = {}
        bucket_map = [[] for _ in range(len(nums) + 1)] # [[],[],[],[],[],[],[]]
        result = []

        # get freq first
        for n in nums:
            frq_map[n] = 1 + frq_map.get(n,0)  #get the curren count and increment
            # frq_map = [1:1, 2:2, 3:2]
        
        for key, val in frq_map.items():
            bucket_map[val].append(key)
            # bucket_map =  [[],[1],[2, 3],[],[],[]]
        
        for bucket_idx in range(len(bucket_map) -1, 0, -1):
            for n in bucket_map[bucket_idx]:
                result.append(n)
                if len(result) == k:
                    return result
        
    
