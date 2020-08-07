class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dups = set()
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                dups.add(nums[i])
        return list(dups)
            