# coding=utf-8

__author__ = 'LY'
__time__ = '2018/6/17'

# 汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
# 对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。

class Solution:
	def LeftRotateString(self, s, n):
		if not s :
			return ''
		ss = list(s)
		leftStr = ss[:n]
		count = 0
		while count < n: 
			del ss[0]
			count += 1
		res = ss + leftStr
		return ''.join(res)

	# 旋转
	def LeftRotateString2(self, s, n):
		if not s :
			return ''
		res1 = list(reversed(s[:n]))
		res2 = list(reversed(s[n:]))
		res = res1 + res2
		res = list(reversed(res))
		return ''.join(res)

	def RightRotateString(self, s, n):
		if not s :
			return ''
		res = list(reversed(s))
		res1 = list(reversed(res[:n]))
		res2 = list(reversed(res[n:]))
		res = res1 + res2
		return ''.join(res)

if __name__ == '__main__':
	ss = 'abcXYZdef'
	s = Solution()
	print(ss)
	print(s.LeftRotateString(ss, 3))
	print(s.LeftRotateString2(ss, 3))
	print(s.RightRotateString(ss, 3))