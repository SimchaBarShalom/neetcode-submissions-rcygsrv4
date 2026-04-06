class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap) 
        while len(max_heap) > 1:
            heaviest = -heapq.heappop(max_heap)
            second_heaviest = -heapq.heappop(max_heap)
            if heaviest != second_heaviest:
                remainder = heaviest - second_heaviest
                heapq.heappush(max_heap, -remainder) 
                
        if len(max_heap) == 0:
            return 0
        return -max_heap[0]
        