# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/5/26'

# 将1开始的自然数按照顺时针顺序填充到二维数组中，要求输入矩阵的 高度M 和 长度N， 输出填充后的矩阵

class Solution():
	def FillMatrix(self, m, n, count):
		# 创建 m*n的列表
		matrix = [[0]*n for i in range(m)]
		x = 0; y = 0; cnt =1
		while m>0 and n>0:
		 	if m == 1:
		 		for k in range(y, y+n):
		 			matrix[x][k] = cnt
		 			cnt += 1
		 		break
		 	if n == 1:
		 		for k in range(x, x+m):
		 			matrix[k][y] = cnt
		 			cnt += 1
		 		break
		 	matrix, cnt = self.FillEdge(x, y, m, n, cnt, matrix)
		 	x += 1
		 	y += 1
		 	m -= 2
		 	n -= 2
		return matrix

	def FillEdge(self, x, y, m, n, cnt, matrix):
		i = x; j = y
		while j < y+n-1:
			matrix[i][j] = cnt
			j += 1
			cnt += 1
		while i < x+m-1:
			matrix[i][j] = cnt
			i += 1
			cnt += 1
		while j > y:
			matrix[i][j] = cnt
			j -= 1
			cnt += 1
		while i > x:
			matrix[i][j] = cnt
			i -= 1
			cnt += 1
		return matrix, cnt

if __name__ == '__main__':
	s = Solution()
	m = 4
	n = 3
	print(s.FillMatrix(m,n,1))