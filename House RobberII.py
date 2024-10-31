https://leetcode.com/problems/house-robber-ii/description/
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])

        def rob_linear(houses):
            rob1,rob2=0,0
            for money in houses:
                new_rob=max(money+rob1,rob2)
                rob1=rob2
                rob2=new_rob
            return rob2

        max_rob_case1=rob_linear(nums[:-1])
        max_rob_case2=rob_linear(nums[1:])

        return max(max_rob_case1,max_rob_case2)      
