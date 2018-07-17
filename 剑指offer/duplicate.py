# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/24'

# 数组中重复的数字

class Solution:
	# 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
	# 函数返回True/False
	# def duplicate(self, numbers, duplication):
	# 	flag = False
	# 	if not numbers:
	# 		return flag
	# 	for i in range(len(numbers)):
	# 		if numbers[i] in numbers[i+1:]:
	# 			duplication[0] = numbers[i]
	# 			flag = True
	# 			break
	# 	return flag

	def duplicate(self, numbers, duplication):
		flag = False
		if not numbers:
			return flag

		temp = set()
		for k in numbers:
			if k in temp:
				duplication[0] = k
				flag = True
				break
			else:
				temp.add(k)
		return flag

if __name__ == '__main__':
	k = [2,3,1,0,2,5,3]
	duplication = [0]
	s = Solution()
	print(s.duplicate(k, duplication))

