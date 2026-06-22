# The best solution
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicate = set(nums)
        return len(no_duplicate) != len(nums)