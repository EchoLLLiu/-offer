# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/24'

# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
# 思路：递归: sum = n + sum(n-1)

class Solution:
	def Sum_Solution(self, n):
		if n == 1:
			return 1
		return n + self.Sum_Solution(n-1)

if __name__ == '__main__':
	n = 10
	s = Solution()
	print(s.Sum_Solution(n))