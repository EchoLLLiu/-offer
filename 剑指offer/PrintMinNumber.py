# coding=utf-8

__author__ = 'LY'
__time__ = '2018/6/8'

# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
# 思路：将数字转换成字符串，并定义字符串比较函数，若str1+str2>str2+str1，则规定str1>str2.按此方法对字符串列表进行冒泡排序。

class Solution:
	def theMax(self, str1, str2):
		'''定义字符串比较函数'''
		return str1 if str1+str2 > str2+str1 else str2

	def PrintMinNumber(self, numbers):
		"""使用冒泡进行排序(把最大的放最后)"""
		string = [str(num) for num in numbers]
		res = []
		flag = True
		count = len(string) - 1
		while flag and  count > 0:
			flag = False
			for i in range(len(string)-1):
				if self.theMax(string[i], string[i+1]) == string[i]:
					temp = string[i]
					del string[i]
					string.insert(i+1, temp)
					flag = True
			count -= 1
		string = ''.join(string)
		return string

	# def cmp(self, a, b):
	# 	'''定义比较函数python2.x版本可用该方法'''
	# 	ab = int(a+b)
	# 	ba = int(b+a)
	# 	return 1 if ab > ba else -1

	# def PrintMinNumber(self, numbers):
	# 	string = [str(num) for num in numbers]
	# 	string.sort(self.cmp, reverse=True)
	# 	return ''.join(string)


if __name__ == '__main__':
	num = [7,13,4,246]
	s = Solution()
	print(s.PrintMinNumber(num))


