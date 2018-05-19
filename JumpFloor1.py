# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/5/17'

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

class Solution:
    # def jumpFloor(self, number):
    #     '''递归:提交代码超时了'''
    #     if number in [0, 1, 2]:
    #     	return number
    #     return self.jumpFloor(number-1)+self.jumpFloor(number-2)

    def jumpFloor(self, number):
        '''迭代'''
        floor = []
        for i in range(number+1):
        	if i in [0,1,2]:
        		floor.append(i)
        		continue
        	floor.append(floor[i-1]+floor[i-2])
        return floor[-1]

if __name__ == '__main__':
	number = 5
	s = Solution()
	num = s.jumpFloor(number)
	print(num)