class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap) 
        while len(maxHeap) > 1:
            heaviest1 = -heapq.heappop(maxHeap)
            heaviest2 = -heapq.heappop(maxHeap)
            if heaviest1 != heaviest2:
                val = heaviest1 - heaviest2
                heapq.heappush(maxHeap,-val) 

        if len(maxHeap) == 0:
            return 0
        return -maxHeap[0]
        