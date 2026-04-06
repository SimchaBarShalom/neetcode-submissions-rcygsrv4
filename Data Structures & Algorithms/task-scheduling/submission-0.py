class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=[0]*26
        heap=[]
        for i in range(len(tasks)):
            freq[ord(tasks[i])-ord('A')]+=1
        for i in range(len(freq)):
            if freq[i]>0:
                heap.append(-freq[i])      
        heapq.heapify(heap)
        queue=[]
        time=0
        while(len(heap)>0 or len(queue)>0):
            time+=1
            if len(heap)>0:
                count=heapq.heappop(heap)+1
                if count<0:
                    queue.append((count,time+n))       
            if len(queue)>0:
                countq,timeq=queue[0]
                if timeq==time:
                    queue.pop(0)
                    heapq.heappush(heap,countq)       
        return time
        
        