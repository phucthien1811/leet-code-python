from typing import List


class Solution:
    #brute force
    #Time complexity: O(n^2)
    #memory complexity: O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      #  for i in range(len(nums)):
        #    for j in range(i + 1, len(nums)):
          #      if nums[i] + nums[j] == target:
        #            return [i, j]
           #     

       # return []


       #Time complexity: O(n)
    #memory complexity: O(n)
        visit = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in visit:
                return [visit[diff], i]     
            visit[num] = i
        return []
print(Solution().twoSum([2, 7, 11, 15], 9))

