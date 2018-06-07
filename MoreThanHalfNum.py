# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/6/7'

# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

class Solution:
	# def MoreThanHalfNum_Solution(self, numbers):
	# 	if numbers == []:
	# 		return 0
	# 	if len(numbers) == 1:
	# 		return numbers[0]
	# 	lens = len(numbers)
	# 	BreakFlag = lens / 2.0
	# 	currentCount = {}
	# 	for i in range(lens):
	# 		# 如果当前数字在之前出现过，个数加一
	# 		if numbers[i] in currentCount.keys():
	# 			if currentCount[numbers[i]] + 1 > BreakFlag:
	# 				return numbers[i] 
	# 			currentCount[numbers[i]] += 1
	# 		else: currentCount[numbers[i]] = 1
	# 	return 0

    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers: return 0
        res = 0
        times = 0
        for i, num in enumerate(numbers):
            if times == 0:
                res = num
                times = 1
            elif num == res:
                times += 1
            else:
                times -= 1
        return res if numbers.count(res) > len(numbers) / 2 else 0


if __name__ == '__main__':
	num = [1,2,3,2,2,2,5,4,2]
	s = Solution()
	print(s.MoreThanHalfNum_Solution(num))


