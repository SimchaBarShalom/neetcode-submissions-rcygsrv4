class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.min_heap=[]
        for i in range(len(nums)):
            self.add(nums[i])

    def add(self, val: int) -> int:
        if len(self.min_heap)<self.k:
            heapq.heappush(self.min_heap, val)
        else:
            if val>self.min_heap[0]:
                heapq.heappushpop(self.min_heap, val)
        return self.min_heap[0]

        
