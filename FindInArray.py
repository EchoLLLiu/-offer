#coding:utf-8
'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
'''
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表(非np中的数组，不能直接读取一列)
    def Find(self, target, array):
    	# startOfLine用来保存每一行列表的第一个数字
    	# 通过将target与其进行比较，找到target可能存在的那一行
#        startOfLine = [x[0] for x in array]
#        index = 0
#        lens = len(array)
#         if target < array[0][0]:
#        	return False
#        while index < lens and target > startOfLine[index]:
#        	index += 1
        # target比最后一行的第一个数字还要大时（target存在于最后一行或不存在array中）
        # 若target不等于某一行第一个数字，则其存在当前行的前一行（target存在于前几行，除了最后一行）
#        if index >= lens or target < startOfLine[index]:
#        	index = index-1
#       return target in array[index]   
		# 循环查找每一行，看target是否存在
        lens = len(array)
        count = 0
        for i in range(lens):
            if target in array[i]:
            	count += 1 
        if count >= 1:
        	return True
        else:
        	return False

if __name__ == '__main__':
	a = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
	s = Solution()
	print(s.Find(7,a))
