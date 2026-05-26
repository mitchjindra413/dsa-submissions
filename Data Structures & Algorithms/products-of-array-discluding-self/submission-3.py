class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = []
        prod = 1
        for num in nums:
            prods.append(prod)  
            prod *= num

        backward_prods = []
        prod = 1
        for num in reversed(nums):
            backward_prods.append(prod)
            prod *= num

        res = []
        for i in range(len(nums)):
            res.append(prods[i] * backward_prods[len(backward_prods) - 1 - i])

        return res