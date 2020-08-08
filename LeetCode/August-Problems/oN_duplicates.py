class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dups = set(nums)
        for i in nums:
            if i in dups:
                dups.remove(i)
            else:
                dups.add(i)
        return list(dups)
            