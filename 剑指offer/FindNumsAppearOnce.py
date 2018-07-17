# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/20'

# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

class Solution:
	# 返回[a,b] 其中ab是出现一次的两个数字
	# def FindNumsAppearOnce(self, array):
	# 	once = []
	# 	for num in array:
	# 		if array.count(num) == 1:
	# 			once.append(num)
	# 	return once

	# def FindNumsAppearOnce(self, array):
	# 	if array == []:
	# 		return []

	# 	res = 0
	# 	list1 = []
	# 	list2 = []
	# 	for num in array:
	# 		res = res^num
	# 	tmp = bin(res).replace('0b','')
	# 	if '1' in tmp:
	# 		idx = tmp[::-1].index('1')
	# 	for num in array:
	# 		if idx >= len(bin(num).replace('0b','')):
	# 			list1.append(num)
	# 		elif bin(num).replace('0b','')[::-1][idx] != '1':
	# 			list1.append(num)
	# 		else:
	# 			list2.append(num)
	# 	tmp1 = 0
	# 	tmp2 = 0
	# 	print(list1)
	# 	print(list2)
	# 	for i in list1:
	# 		tmp1 = tmp1^i
	# 	for j in list2:
	# 		tmp2 = tmp2^j
	# 	return [tmp1, tmp2]

	def FindNumsAppearOnce(self, array):
		tmp = set()
		for a in array:
			if a in tmp:
				tmp.remove(a)
			else:
				tmp.add(a)
		return list(tmp)

if __name__ == '__main__':
	arr = [2,3,2,1,3,6,6,7,5,8,8,7]
	s = Solution()
	print(s.FindNumsAppearOnce(arr))
	help(set)
