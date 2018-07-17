# coding=utf-8

__author__ = 'LY'
__time__ = '2018/7/16'

# 有 n 个学生站成一排，每个学生有一个能力值，牛牛想从这 n 个学生中按照顺序选取 k 名学生，要求相邻两个学生的位置编号的差不超过 d，
# 使得这 k 个学生的能力值的乘积最大，你能返回最大的乘积吗？
## 思路： 动态规划

class Solution():
	def findMultiMax(self, n, ability, k, d):
		if not ability:
			return 0
		# 只挑一个学生
		if k == 1:
			return max(ability)
		# 只有一个学生时
		if n == 1 and k > 1:
			return 0

		Max_multi = 1
		start = 0
		end = start + (k-1) * d 
		more_end = end + 1

		while more_end < len(ability):
			abi_sort = sorted(ability[start, more_end])
			Max_multi = max(Max_multi, self.multi(k, abi_sort)) 
			start += 1
			end += 1
			more_end += 1

		if more_end >= len(ability):
			abi_sort = sorted(ability[start, more_end], reverse = True)
			Max_multi = max(Max_multi, self.multi(k, abi_sort))


	def multi_k(self, k, abi_sort):
		for i in range(k):
			multi *= abi_sort[i]
		return multi




