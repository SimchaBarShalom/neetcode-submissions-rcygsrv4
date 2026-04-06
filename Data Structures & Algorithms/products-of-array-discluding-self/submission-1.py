class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        sumRight= [1] * len(nums)
        sumLeft= [1] * len(nums)

        for i in range (1,len(nums)):
           sumLeft[i]=sumLeft[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            sumRight[i]=sumRight[i+1]*nums[i+1]
        for i in range (len(output)):
            output[i]=sumRight[i]*sumLeft[i]
        return output

      