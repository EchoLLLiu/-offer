# coding=utf-8

__author__ = 'LY'
__time__ = '2018/7/15'

# 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
# 例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}

class Solution:
	def maxInWindows(self, num, size):
		if not num or not size or len(num) < size:
			return []
		# 滑动窗口起始点与终点
		start = 0
		end = size - 1

		res = []
		# Max_idx 当前滑动窗口内的最大值下标
		Max_idx = 0

		while end < len(num):
			if start == 0 or Max_idx < start:
				Max = max(num[start:end+1])
				res.append(Max)
				Max_idx = num.index(Max)
			elif num[Max_idx] > num[end]:
				res.append(Max)
			else:
				Max = num[end]
				res.append(Max)
				Max_idx = end
			start += 1
			end += 1
		return res


if __name__ == '__main__':
	lst = [2,3,4,2,6,2,5,1]
	s = Solution()
	print(s.maxInWindows(lst, 3))