# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/5/17'

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

class Solution:
    def jumpFloorII(self, number):
        '''迭代法，保存n次结果'''
        floor = []
        for i in range(number+1):
        	if i in [0,1,2]:
        		floor.append(i)
        		continue
        	step = 0
        	for k in range(i):
        		step += floor[k]
        	floor.append(step+1)
        return floor[-1]

    # def jumpFloorII(self, number):
    #     '''递归法：当number很大时，递归很深，会超时'''
    #     if number in [0,1,2]:
    #     	return number
    #     res = 0
    #     for k in range(number):
    #     	res += self.jumpFloorII(k)
    #     return res+1



if __name__ == '__main__':
	number = 3
	s = Solution()
	num = s.jumpFloorII(number)
	print(num)