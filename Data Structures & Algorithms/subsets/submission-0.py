import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        prev = self.subsets(nums[1:])
        n = nums[0]
        res = copy.deepcopy(prev)
        for p in prev:
            p.append(n)
        return res + prev