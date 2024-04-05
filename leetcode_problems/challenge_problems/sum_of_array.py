class Solution:
    def runningSum(self, nums: list) -> list:
        for items in nums:
            nums[items] = nums[items + 1  ]
        return nums
        


sol = Solution()
num = [1,1,1,1,1]
print(sol.runningSum(nums=num))
            