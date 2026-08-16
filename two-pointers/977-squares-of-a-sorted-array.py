"""
LeetCode 977: Squares of a Sorted Array

Pattern: Two Pointers
Secondary Concepts: Sorted Array, Result Array

Time Complexity: O(n)
Space Complexity: O(n)

Note:
    - Separate negative and positive numbers.
    - Square both.
    - Reverse squared negatives.
    - Merge the two sorted arrays using two pointers.

"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # # method 1:
        # pos = []        # for positive elements
        # neg = []        # for negative elements
        # result = []

        # # split positives and negatives
        # for i in range(len(nums)):
        #     if nums[i] >= 0:
        #         pos.append(nums[i])
        #     else:
        #         neg.append(nums[i])

        # for i in range(len(pos)):
        #     pos[i] *= pos[i]

        # for i in range(len(neg)):
        #     neg[i] *= neg[i]

        # neg.reverse()


        # # merge both array
        # i = 0
        # j = 0

        # while i < len(pos) and j < len(neg):
        #     if pos[i] <= neg[j]:
        #         result.append(pos[i])
        #         i += 1

        #     else:
        #         result.append(neg[j])
        #         j += 1

        # while i < len(pos):
        #     result.append(pos[i])
        #     i+=1

        # while j < len(neg):
        #     result.append(neg[j])
        #     j+=1

        # return result


        # method 2: Best
        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for pos in range(len(nums) - 1, -1, -1):
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square >= right_square:
                result[pos] = left_square
                left += 1

            else:
                result[pos] = right_square
                right -= 1

        return result

# Local testing
if __name__ == "__main__":
    solution = Solution()

    print(solution.sortedSquares([1, 1, 2, 5, 8]))
    print(solution.sortedSquares([-2, -1, 0, 2, 5]))
    print(solution.sortedSquares([-5, -3, -2, -1]))
