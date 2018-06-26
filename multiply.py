# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/24'

# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

class Solution:
	def multiply(self, A):
		B = []
		if not A :
			return B
		if len(A) == 1:
			return A
		lens = len(A)
		B = [1 for i in range(lens)]
		for i in range(1,lens):
			B[i] = B[i-1] * A[i-1]
		temp = 1
		for k in range(lens-2, -1, -1):
			temp *= A[k+1]
			B[k] *= temp  
		return B

if __name__ == '__main__':
	A = [1,2,3,4,5]
	s = Solution()
	print(s.multiply(A))