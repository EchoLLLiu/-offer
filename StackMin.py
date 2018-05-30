# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/5/26'

# 定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数

class Solution:
	def __init__(self):
		self.items = []

	def push(self, node):
		self.items.append(node)
		return 

	def pop(self):
		if self.items == []:
			return
		popnode = self.items.pop()
		return popnode

	def top(self):
		if self.items == []:
			return
		return self.items[-1]

	def min(self):
		if self.items == []:
			return
		minNode = self.items[0]
		lens = len(self.items)
		for i in range(1,lens):
			if minNode > self.items[i]:
				minNode = self.items[i]
		return minNode

if __name__ == '__main__':
	s = Solution()
	List = [3,2,5,4,7,9,2,5,1]
	for ele in List:
		s.push(ele)
	print(s.items)
	print(s.min())