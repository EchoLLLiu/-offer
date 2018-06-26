# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/24'

# 圆圈中最后剩下的数
# 思路：约瑟夫环问题

class Solution:
	def LastRemaining_Solution(self, n, m):
		if n < 1 or m < 1:
			return -1
		last = 0
		for i in range(2, n + 1):
			last = (last + m) % i
			print(last)
		return last

if __name__ == '__main__':
	n = 4
	m = 3
	s = Solution()
	print(s.LastRemaining_Solution(n,m))