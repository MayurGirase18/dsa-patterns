"""
LeetCode 26: Remove Duplicates from Sorted Array

Pattern: Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)

"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        # # method 1:

        # unique_pos = 0
        # current = 1       # first number already unique so start from index 1.
        # unique_count = 1  # always a unique element present even if all numbers are same.

        # while current < len(nums):
        #     if nums[current] != nums[unique_pos]:
        #         unique_pos += 1
        #         nums[unique_pos] = nums[current]
        #         unique_count += 1

        #     current += 1

        # return unique_count, nums


        # method 2: Best
        
        unique_pos = 0

        for current in range(1, len(nums)):
            if nums[current] != nums[unique_pos]:
                unique_pos += 1
                nums[unique_pos] = nums[current]

        return unique_pos + 1       # return the no of uniuqe number


# Local testing
if __name__ == "__main__":
    solution = Solution()

    print(solution.removeDuplicates([1, 1, 1, 2, 2]))
    print(solution.removeDuplicates([2, 2, 3, 3, 3, 4, 4, 4, 4]))
    print(solution.removeDuplicates([-1, 0, 0, 1, 1, 1]))