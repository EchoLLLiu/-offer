# coding=utf-8

__author__ = 'LY'
__time__ = '2018/7/13'

# 将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 
# 数值为0或者字符串不是一个合法的数值则返回0。

class Solution:
	def isSimNum(self, s):
		'''判断是否是正负整数类型'''
		if not s:
			return False

		num = ['1','2','3','4','5','6','7','8','9','0']
		flag = ['+','-']
		start = 0
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

	def StrToInt(self, s):
		if not s or not self.isSimNum(s):
			return 0
		if self.isSimNum(s):
			return int(s)

if __name__ == '__main__':
	s1 = "+123"
	s2 = "-293"
	s3 = "0"
	s4 = "js234"
	s5 = "+"

	s = Solution()
	print(s.isSimNum(s1),s.isSimNum(s2),s.isSimNum(s3),s.isSimNum(s4),s.isSimNum(s5))
	print(s.StrToInt(s1),s.StrToInt(s2),s.StrToInt(s3),s.StrToInt(s4),s.StrToInt(s5))




