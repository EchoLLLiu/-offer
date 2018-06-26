# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/20'

# 统计一个数字在排序数组中出现的次数。
# 思路：二分查找，找到最左边一个的位置和最右边一个的位置

class Solution:
	def GetNumberOfK(self, data, k):
		if data == []:
			return 0
		left = self.leftBinarySearch(data, k)
		right = self.rightBinarySearch(data, k)
		return right - left + 1 if right != -1 and left != -1 else 0 


	def leftBinarySearch(self, data, k):
		lens = len(data)
		left = 0
		right = lens - 1
		res = -1
		while left <= right:
			mid = (left + right) // 2
			if data[mid] == k:
				res = mid
				right = mid - 1
				continue
			if data[mid] < k:
				left = mid + 1
				continue
			if data[mid] > k:
				right = mid - 1
				continue
		return res

	def rightBinarySearch(self, data, k):
		lens = len(data)
		left = 0
		right = lens - 1
		res = -1
		while left <= right:
			mid = (left + right) // 2
			if data[mid] == k:
				res = mid
				left = mid + 1
				continue
			if data[mid] < k:
				left = mid + 1
				continue
			if data[mid] > k:
				right = mid - 1
				continue
		return res

if __name__ == '__main__':
	data = [1,2,3,3,3,4,5,6]
	s = Solution()
	print(s.leftBinarySearch(data, 3))
	print(s.rightBinarySearch(data,3))
	print(s.GetNumberOfK(data, 3))