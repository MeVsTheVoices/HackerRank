from collections import deque
import math


class Solution(object):
    def shortestSubarray(self, nums, k):
            """
            Given an array of integers nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

            :param nums: List[int] - The array of integers
            :param k: int - The target sum
            :return: int - The length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
            """
            size = len(nums)
            dq = deque()
            shortest = math.inf
            current_sum = 0
            min_sum = 0
            
            # Keep adding until we find a subarray with sum >= k
            for i in range(size):
                current_sum += nums[i]
                
                # If current_sum - min_sum >= k, then we have found a subarray with sum >= k
                if current_sum - min_sum >= k:
                    shortest = min(shortest, i + 1)
                
                # Remove all elements from the left that are greater than or equal to current_sum
                while dq and current_sum - dq[0][1] >= k:
                    shortest = min(shortest, i - dq[0][0])
                    dq.popleft()
                
                # Remove all elements from the right that are greater than or equal to current_sum
                while dq and current_sum <= dq[-1][1]:
                    dq.pop()
                
                # Add current_sum to the right
                dq.append((i, current_sum))
                
                min_sum = min(min_sum, current_sum)
            
            return shortest if shortest != math.inf else -1
        