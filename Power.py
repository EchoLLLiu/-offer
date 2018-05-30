# coding = utf-8

__author__ = 'LY'
__time__ = '2018/5/28'

# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

class Solution:
	def Power_1(self, base, exponent):
		# 普通算法
		# 对0进行界定
		if base > -1e-7 and base < 1e-7:
			return 0
		if exponent == 1:
			return base
		if exponent == 0:
			return 1
		exp = abs(exponent)
		res = 1.0
		for i in range(exp):
			res *= base
		if exponent > 0:
			return res
		else:
			return 1/res

	def Power_2(self, base, exponent):
		# 高效算法
		if base > -1e-7 and base < 1e-7:
			return 0
		if exponent == 1:
			return base
		if exponent == 0:
			return 1
		exp = abs(exponent)
		ans = self.Power_2(base, exp >> 1)
		ans = ans * ans * 1.0
		if exp & 1 == 1 :
			# 如果幂为奇数
			ans = ans * base
		if exponent < 0:
			return 1/ans 
		return ans



if __name__ == '__main__':
	base = 2
	exponent = -1
	s = Solution()
	print(s.Power_1(base, exponent))
	print(s.Power_2(base, exponent))