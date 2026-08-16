"""
LeetCode 977: Squares of a Sorted Array

Pattern: Two Pointers
Secondary Concepts: Sorted Array, Result Array

Time Complexity: O(n)
Space Complexity: O(n)

"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        pos = []
        neg = []
        result = []

        for i in range(len(nums)):
            if nums[i] >= 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])

        for i in range(len(pos)):
            pos[i] *= pos[i]

        for i in range(len(neg)):
            neg[i] *= neg[i]

        neg.reverse()

        if not neg:
            result = pos
            return result

        elif not pos:
            result = neg
            return result

        else:
            i = 0
            j = 0

            while i < len(pos) and j < len(neg):
                if pos[i] <= neg[j]:
                    result.append(pos[i])
                    i += 1

                else:
                    result.append(neg[j])
                    j += 1

            while i < len(pos):
                result.append(pos[i])
                i+=1

            while j < len(neg):
                result.append(neg[j])
                j+=1

            return result

# Local testing
if __name__ == "__main__":
    solution = Solution()

    print(solution.sortedSquares([1, 1, 2, 5, 8]))
    print(solution.sortedSquares([-2, -1, 0, 2, 5]))
    print(solution.sortedSquares([-5, -3, -2, -1]))
