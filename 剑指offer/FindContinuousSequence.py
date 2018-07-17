# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/20'

# 和为S的连续正数序列

import math

class Solution:
	def FindContinuousSequence(self, tsum):
		endn = 2
		n = int(math.sqrt(2*tsum))
		res = []
		while n >= endn:
			List = []
			if ((n & 1) == 1 and tsum % n == 0) or (tsum % n) * 2 == n:
				j = 0
				k = (tsum // n) - (n - 1) // 2
				while j < n:
					List.append(k)
					k += 1
					j += 1
				res.append(List)
			n -= 1
		return res

if __name__ == '__main__':
	tsum = 100
	s = Solution()
	print(s.FindContinuousSequence(tsum))

