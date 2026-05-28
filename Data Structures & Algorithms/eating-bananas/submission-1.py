class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        best = r
        while l <= r:
            k = (l + r) // 2
            time = 0
            for num in piles:
                time += math.ceil(float(num) / k)
            if time > h:
                l = k + 1
            else:
                best = k
                r = k - 1
        
        return best
