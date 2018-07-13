# coding=utf-8

__author__ = 'LY'
__time__ = '2018/7/10'

# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
# 例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

class Solution:
    # s字符串
	def isNumeric(self, s):
		if not s:
			return False

		# if s.count('.') > 1:
		# 	return False

		if self.isSimNum(s) or self.isPointNum(s) or self.isENum(s):
			return True
		else:
			return False

	def isSimNum(self, s):
		'''判断是否是正负整数类型'''
		if not s:
			return False

		num = ['1','2','3','4','5','6','7','8','9','0']
		flag = ['+','-']

		if s[0] in flag and len(s) == 1:
			return False
		elif len(s) > 1:
			start = 1
		elif s[0] in num[:10]:
			start = 0

		for i in range(start,len(s)):
			if s[i] not in num:
				return False
		return True

	def isPointNum(self, s):
		'''判断是否是小数类型'''
		if not s:
			return False

		num = ['1','2','3','4','5','6','7','8','9','0']
		flag = ['+','-']

		if s.count('.') == 1:
			if s[0] != '.':
				if s[0] in flag:
					start = 1
				if s[0] in num[:10]:
					start = 0
				for i in range(start,len(s)):
					if s[i] not in (num+['.']):
						return False
				return True
			else:
				if s[1] in flag:
					return False
				else: return True
		return False


	def isENum(self, s):
		if not s:
			return False

		idx = 0
		if s.count('e') == 1:
			idx = s.index('e')
		elif s.count('E') == 1:
			idx = s.index('E')

		if (self.isSimNum(s[:idx]) or self.isPointNum(s[:idx])) and self.isSimNum(s[idx+1:]):
			return True
		else:
			return False



if __name__ == '__main__':
	s = Solution()
	print(s.isNumeric("+100"),s.isNumeric("5e2"),s.isNumeric("-123"),s.isNumeric("3.1416"),s.isNumeric("-1E-16"))
	print(s.isNumeric("12e"),s.isNumeric("1a3.14"),s.isNumeric("1.2.3"),s.isNumeric("+-5"),s.isNumeric("12e+4.3"))
	print(s.isNumeric("123.45"))




