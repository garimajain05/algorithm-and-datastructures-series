class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}
        for j in range(len(nums)):
            value = nums[j]
            difference = target - value
            if(difference in HashMap):
              return [HashMap[difference], j]
            HashMap[value] = j
