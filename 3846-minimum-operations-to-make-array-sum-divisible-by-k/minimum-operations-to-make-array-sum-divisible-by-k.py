class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        arrsum = 0
        min = 0
        for i in nums:
            arrsum +=i
        return arrsum % k





        