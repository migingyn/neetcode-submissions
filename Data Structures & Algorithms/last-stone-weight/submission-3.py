import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        h = [-x for x in stones] # O(n) time/space

        heapq.heapify(h)

        while len(h) > 1:
            flarge = -heapq.heappop(h)
            slarge = -heapq.heappop(h)
            if flarge != slarge:
                heapq.heappush(h, -(flarge-slarge))

        return -heapq.heappop(h) if h else 0
        
