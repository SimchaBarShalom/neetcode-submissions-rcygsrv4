class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while (len(stones))>1:
            val1=-heapq.heappop(stones)
            val2=-heapq.heappop(stones)
            if val1!=val2:
                heapq.heappush(stones,-(val1-val2))
        return -stones[0] if stones else 0
        




        