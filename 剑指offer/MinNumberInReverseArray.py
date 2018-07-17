# coding=utf-8

__author__ = 'LY'
__time__ = '2018/5/16'

# 找到非递减旋转数组的最小元素。例如输入[3,4,5,1,2]，找到1

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
        	return 0
        #array = sorted(rotateArray)
        #return array[0]
        low = 0
        high = len(rotateArray) - 1
        while low + 1 < high:
        	mid = (low+high)//2
        	# 当数组为:[1,0,1,1,1]时，只能使用暴力解法
        	if rotateArray[mid] == rotateArray[low] and rotateArray[mid] == rotateArray[high]:
        		return self.findmin(rotateArray)
        	# 当数组正常时，例如:[3,4,5,1,2]，使用二分查找法。
        	# 注意等号：[3,0,1,1,1]，[3,3,3,0,1]这两种情况
        	if rotateArray[mid] >= rotateArray[low] and rotateArray[mid] > rotateArray[high]:
        		low = mid
        		continue
        	if rotateArray[mid] < rotateArray[low] and rotateArray[mid] <= rotateArray[high]:
        		high = mid
        		continue
        if low + 1 >= high:
        	return rotateArray[low] if rotateArray[low] < rotateArray[high] else rotateArray[high]

    def findmin(self,rotateArray):
    	min = rotateArray[0]
    	for ele in rotateArray:
    		if ele < min:
    			min = ele
    	return min

if __name__ == '__main__':
	a = [1,0,1,1,1]
	s = Solution()
	print(s.minNumberInRotateArray(a))