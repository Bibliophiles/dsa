from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countFreq = defaultdict(int)
        for n in nums:
            countFreq[n] += 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for i, n in countFreq.items():
            freq[n].append(i)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
            if len(result) == k:
                return result
        