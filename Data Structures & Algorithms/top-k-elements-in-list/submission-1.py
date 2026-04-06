class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent={}
        for i in range(len(nums)):
            if nums[i] in frequent:
                 frequent[nums[i]]+=1
            else:
                frequent[nums[i]]=1
        arr=[[] for i in range (len(nums)+1)]
        for i in frequent:
            arr[frequent[i]].append(i)
        res=[]
        for i in range (len(nums),0,-1):
            if arr[i]:
                for j in arr[i]:
                    res.append(j)
                    if len(res)==k:
                        return res
        return res

        

        

        
        
        
        
   

            


        
    