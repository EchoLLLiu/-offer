# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/24'

# 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号
# 思路：使用异或和位与运算

class Solution:
	# def Add(self, num1, num2):
	# 	INT_BITS = 32
	# 	MAX_INT = (1 << (INT_BITS - 1)) - 1

	# 	while num2 and num2 < MAX_INT and num1 < MAX_INT:
	# 		Sum = num1 ^ num2
	# 		carry = (num1 & num2) << 1
	# 		num1 = Sum
	# 		num2 = carry
	# 	return num1

	def Add(self, num1, num2):
		return sum([num1, num2])

if __name__ == '__main__':
	n1 = 3
	n2 = 8
	s = Solution()
	print(s.Add(n1,n2))