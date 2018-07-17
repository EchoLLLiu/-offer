# coding=utf-8

__author__ = 'LY'
__time__ = '2018/7/16'

# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
# 但是不能进入行坐标和列坐标的数位之和大于k的格子。 
# 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

class Solution:
	def judge(self, threshold, i, j):
		if sum(map(int, str(i)+str(j))) <= threshold:
			return True
		else:
			return False

	def findgrid(self, threshold, rows, cols, matrix, i, j):
		count = 0
		if i<rows and i>=0 and j<cols and j>=0 and self.judge(threshold, i, j) and matrix[i][j]==0:
			matrix[i][j] = 1
			count = 1 + self.findgrid(threshold, rows, cols, matrix, i-1, j) \
					+ self.findgrid(threshold, rows, cols, matrix, i+1, j) \
					+ self.findgrid(threshold, rows, cols, matrix, i, j-1) \
					+ self.findgrid(threshold, rows, cols, matrix, i, j+1)
		return count

	def movingCount(self, threshold, rows, cols):
		matrix = [[0 for j in range(cols)] for i in range(rows)]
		count = self.findgrid(threshold, rows, cols, matrix, 0, 0)
		print(matrix)
		return count

if __name__ == '__main__':
	s = Solution()
	print(s.movingCount(15, 20, 20))
	