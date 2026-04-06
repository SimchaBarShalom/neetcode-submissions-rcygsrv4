class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        sumDivison = 1
        count = 0
        for i in range (len(nums)):
            if nums[i]==0:
                count+=1
            else:
                sumDivison*=nums[i]
        if count==1:
            for i in range (len(nums)):
                if nums[i]==0:
                    output[i]=sumDivison
                else:
                  output[i]=0
        elif count>1:
            return output
        else:
            for i in range (len(nums)):
                output[i]=int(sumDivison/nums[i])

        return output
    
  
            

            



