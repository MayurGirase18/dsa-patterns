"""
LeetCode 80: Remove Duplicates from Sorted Array - II

Pattern: Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)

"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums), nums
        
        unique_pos = 1
        
        for current in range(2, len(nums)):
            if nums[current] != nums[unique_pos-1]:
                unique_pos += 1
                nums[unique_pos] = nums[current]
        
        return unique_pos+1, nums       # return the no of uniuqe number
        
        
# Local testing
if __name__ == "__main__":
    solution = Solution()
        
    print(solution.removeDuplicates([1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5]))
    print(solution.removeDuplicates([1,1,1,2,2,3]))
    print(solution.removeDuplicates([-1, -1]))