"""问题：给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
分析：第一个位置最大值是自己，第二个是自己或者与第一个位置的和，第三个是自己或者与前两个最大值的和，依次类推。"""
class Solution():
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)
