"""
LeetCode 167: Two Sum II - Input Array Is Sorted

Main Pattern: Two Pointers

Time: O(n)
Space: O(1)

Note:
    1. if sum is bigger than target, j-=1. 
    2. if sum is smaller than target, i+=1.

"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        i = 0                       #left
        j = len(numbers) - 1        #right

        while i < j:
            current_sum = numbers[i] + numbers[j]

            if current_sum == target:
                return [i+1, j+1]

            elif current_sum < target:
                i += 1

            elif current_sum > target:
                j -= 1

        else:
            return "Sum is not possible.."


# Local testing
if __name__ == "__main__":
    solution = Solution()

    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([2, 3, 4], 8))
    print(solution.twoSum([-1, 0], -1))
    