class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low < high:
            curr_time = 0
            mid = (low + high) // 2
            for pile in piles:
                curr_time += math.ceil(pile / mid)

            if curr_time <= h:
                high = mid
            else:
                low = mid + 1
        return low