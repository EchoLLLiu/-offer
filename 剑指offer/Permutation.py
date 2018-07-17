# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/7'

# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。（全排列）
# 例如：abc——>abc,acb,bac,bca,cab,cba
import pdb
class Solution:
	def Permutation(self, ss):
		if ss == [] or len(ss) == 1:
			return ss
		res = []
		for i in range(len(ss)):
			for j in self.Permutation(ss[:i]+ss[i+1:]):
				res.append(ss[i] + j)
		return sorted(list(set(res)))

if __name__ == '__main__':
	ss = ['a','a','b']
	s = Solution()
	print(s.Permutation(ss))
		