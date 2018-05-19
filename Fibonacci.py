# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/5/16'

# 现在要求输入一个整数n，请你输出斐波那契数列的第n项。n<=39

import time

class Solution:
    def Fibonacci(self, n):
    	'''递归法'''
        if n in [0,1]:
        	return n
        return self.Fibonacci(n-2)+self.Fibonacci(n-1)

class Solution:
	def Fibonacci(self, n):
		'''迭代法'''
		FibList = []
		# 将前n项保存在数组中
		for i in range(n+1):
			if i in [0,1]:
				FibList.append(i)
				continue
			FibList.append(FibList[-2]+FibList[-1])
		return FibList[-1]

if __name__ == '__main__':
	n = 39
	s = Solution()
	startTime = time.clock()
	res = s.Fibonacci(n)
	time = time.clock() - startTime
	print(res, time)