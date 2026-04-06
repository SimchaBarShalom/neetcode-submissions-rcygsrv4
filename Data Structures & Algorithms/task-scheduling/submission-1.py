class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=26*[0]
        for i in range(len(tasks)):
            freq[ord(tasks[i])-ord('A')]+=1
        max_freq=freq[0]
        count=0
        for i in range(len(freq)):
            if freq[i]>max_freq:
                max_freq=freq[i]
                count=1
            elif freq[i]==max_freq:
                count+=1
      
        return max((((max_freq-1)*(n+1))+count), len(tasks))
        

       