# coding=utf-8

__author__ = 'LY'
__time__ = '2018/6/13'

# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
# (1)先把满足要求的数对保存起来
# (2)计算每对数的差值，输出差值最大的。乘积最小，则两个数相差最大；乘积最大，则两个数相差最小。例如：[1,6]与[3,4]

class Solution:
    def FindNumbersWithSum(self, array, tsum):
    	if not array:
    		return []
    	res = []
    	for i in range(len(array)):
    		pair = []
    		if (tsum - array[i]) in array[i+1:]:
    			pair.append(array[i])
    			pair.append(tsum - array[i])
    		if pair != []:
    			res.append(pair)
    	if res != []:
    		sub = [abs(res[i][0] - res[i][1]) for i in range(len(res))]
    		maxsub = max(sub)
    		idx = sub.index(maxsub)
    		a = res[idx][0]
    		b = res[idx][1]
    		return [a, b] if a < b else [b, a]
    	return []


if __name__ == '__main__':
	arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
	s = Solution()
	print(s.FindNumbersWithSum(arr, 21))