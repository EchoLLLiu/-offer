# -*- coding:utf-8 -*-

__author__ = 'LY'
__time__ = '2018/5/19'

# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。(不能使用首尾指针同时移动的方法，这种方法会导致相对位置改变,即快排思想) 

class Solution:
    def reOrderArray(self, array):
        '''增加空间实现奇数偶数调换位置（需要额外空间）'''
        EvenArray = []
        i = 0
        while i < len(array):
        	if array[i]%2 == 0:   # 如果是偶数，添加到EvenArray中
        		EvenArray.append(array[i])
        		del array[i]
        	else:
        		i += 1
        array += EvenArray
        return array

    # def reOrderArray(self, array):
    # 	'''同时使用两个指针从头开始遍历，在原数组上进行，不开辟额外空间'''
    # 	if len(array) == 0:
    # 		return array
    # 	even = 0
    # 	while even < len(array):
    # 		while even < len(array):
    # 	 		# 从左到右遍历，找到第一个偶数
    # 			if array[even]%2 == 1:
    # 				even += 1
    # 			else: break
    # 		# 找到第一个偶数后，从该偶数后遍历，找到第一个奇数
    # 		odd = even + 1
    # 		while odd < len(array):
    # 			if array[odd]%2 == 0 :
    # 				odd += 1
    # 			else: break
    # 		# 当even后面不再有奇数时，退出大循环
    # 		if odd >= len(array): 
    # 			break
    # 		# 将偶数与奇数之间的数字后移，并把odd的值放到even中
    # 		tmp = array[odd]
    # 		array[even+1:odd+1] = array[even:odd]
    # 		array[even] = tmp
    # 	return array


if __name__ == '__main__':
	array = [1,3,4,7,2,8,5]
	s = Solution()
	print(s.reOrderArray(array))

