from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # Dictionary to store number -> index mapping

        for i, n in enumerate(nums):
            diff = target - n  # Calculate the difference needed
            if diff in prevMap:  # Check if the complement is already in the map
                return [prevMap[diff], i]  # Return indices of the two numbers
            prevMap[n] = i  # Store the current number and its index in the dictionary

        return []  # Return an empty list if no solution is found
