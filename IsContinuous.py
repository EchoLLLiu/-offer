# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/24'

# 扑克牌顺子
# 思路：（1）排序数组；（2）计算出0（大小王）的个数（小于等于4）；（3）计算除0以外其它牌之间的间隔，若小于等于0个数则为顺子

class Solution:
	def IsContinuous(self, numbers):
		if not numbers:
			return False
		zero_num = numbers.count(0)
		numbers.sort()
		MinIndx = zero_num
		gap = 0
		for i in range(MinIndx, len(numbers)-1):
			print(i, i+1)
			if numbers[i] == numbers[i+1]:
				return False
			gap += numbers[i+1] - numbers[i] - 1
		if gap <= zero_num:
			return True
		else:
			return False

if __name__ == '__main__':
	k = [1,3,0,0,5]
	s = Solution()
	print(s.IsContinuous(k))