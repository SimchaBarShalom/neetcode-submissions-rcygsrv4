class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        sum_right= [1] * len(nums)
        sum_left= [1] * len(nums)

        for i in range (1,len(nums)):
           sum_left[i]=sum_left[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            sum_right[i]=sum_right[i+1]*nums[i+1]
        for i in range (len(output)):
            output[i]=sum_right[i]*sum_left[i]
        return output

      