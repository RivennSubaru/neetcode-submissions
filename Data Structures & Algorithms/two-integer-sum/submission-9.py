class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in nums:
                j = nums.index(num2)
                if i != j:
                    res = [i, j] if j > i else [j, i]
                    return res