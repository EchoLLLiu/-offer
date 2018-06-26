# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/17'

# 连续子数组的最大和 
# 动态规划：若之前累加值<0,则累加值对当前值没用；若>0，则有用，相加起来

class Solution:
	def FindGreatestSumOfSubArray(self, array):
		max_sum = pre_sum = array[0]
		for i in range(1,len(array)):
			pre_sum = max(array[i], pre_sum+array[i])
			max_sum = max(max_sum, pre_sum)
		return max_sum

if __name__ == '__main__':
	ss = [6,-3,-2,7,-15,1,2,2]
	s = Solution()
	print(s.FindGreatestSumOfSubArray(ss))
