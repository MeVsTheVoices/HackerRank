class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        freq = [[] for i in range(len(nums)) + 1]

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        for n, c in counts.items():
            freq[c].append(n)

        results = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                results.append(j)
                if len(results) == k:
                    return results
        return results
