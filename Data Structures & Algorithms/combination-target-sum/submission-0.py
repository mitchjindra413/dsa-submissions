class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def rec(target, i, cur):
            if target == 0:
                res.append(cur.copy())
                return
            if target < 0 or i >= len(nums):
                return 
            
            n = nums[i]
            cur.append(n)
            rec(target - n, i, cur)
            cur.pop()

            rec(target, i + 1, cur)

        rec(target, 0, [])
        return res            


        
        
