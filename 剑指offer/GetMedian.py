# coding=utf-8

__author__ = 'LY'
__time__ = '2018/7/15'

# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
# 如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
# 思路：边存边排序

class Solution:
	def __init__(self):
		self.data = []

	def Insert(self, num):
		self.data.append(num)
		self.data.sort()

	def GetMedian(self, x):
		lens = len(self.data)
		if lens % 2 == 0:
			low = lens // 2 - 1
			high = low + 1 
			median = (self.data[low] + self.data[high]) / 2.0
		else:
			mid = lens // 2 
			median = self.data[mid]
		return median

if __name__ == '__main__':
	li = [5,2,3,4,1,6,7,0,8]
	ss = Solution()
	for i in range(len(li)):
		ss.Insert(li[i])
		print(ss.data)
		print(ss.GetMedian(li))
