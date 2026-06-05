import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            tmp = []
            for subset in res:
                tmp += [subset + [num]]
            res += tmp

        return res 
        