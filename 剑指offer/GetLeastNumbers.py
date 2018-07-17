# coding=utf-8

__author__ = 'LY'
__time__ = '2018/6/17'

# 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4.
# 堆排序(小根堆)

class Solution:
	def GetLeastNumbers_Solution(self, tinput, k):
		if tinput == [] or len(tinput) < k or k == 0:
			return []
		'''堆排序，只排前k个最小'''
		self.Build_Min_Heap(tinput)
		i = len(tinput)-1
		count = 1
		while count <= k and i >= 0:
			tinput[0], tinput[i] = tinput[i], tinput[0]
			self.Min_Heapify(tinput, i, 0)
			count += 1
			i -= 1
		res = tinput[-k:]
		return res[::-1]

	def Min_Heapify(self, heap, heapSize, root):
		'''小根堆调整函数'''
		left = 2 * root + 1
		right = left + 1
		larger = root
		if left < heapSize and heap[larger] > heap[left]:
			larger = left
		if right < heapSize and heap[larger] > heap[right]:
			larger = right
		if larger != root:
			heap[larger], heap[root] = heap[root], heap[larger]
			self.Min_Heapify(heap, heapSize, larger)
		else: return

	def Build_Min_Heap(self, heap):
		'''构建初始小根堆'''
		heapSize = len(heap)
		for i in range((heapSize-2)//2, -1, -1):
			self.Min_Heapify(heap, heapSize, i)

if __name__ == '__main__':
	heap = [4,5,1,6,2,7,3,8]
	s = Solution()
	print(s.GetLeastNumbers_Solution(heap, 0))

