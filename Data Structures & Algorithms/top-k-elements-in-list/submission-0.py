class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent={}
        for i in range(len(nums)):
            if nums[i] in frequent:
                 frequent[nums[i]]+=1
            else:
                frequent[nums[i]] =1
        s = sorted(frequent.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in s[:k]]

