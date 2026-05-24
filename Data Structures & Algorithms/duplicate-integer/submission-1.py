class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()

        for elm in nums:
            if elm in unique:
                return True
            unique.add(elm)
        
        return False
        