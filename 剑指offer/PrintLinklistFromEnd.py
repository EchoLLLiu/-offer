# coding=utf-8

__author__ = 'LY'
__time__ = '2018/5/17'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None 

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        ''' 遍历链表，将节点值存放在列表中，倒序输出列表 '''
        p = listNode
        output = []
        if p==None:
            return output
        while p!=None:
            output.append(p.val)
            p = p.next
        return output[::-1]

    # def printListFromTailToHead(self, listNode):
    #     '''递归打印：如果链表太长，容易栈溢出'''
    #     p = listNode
    #     if p != None:
    #         if p.next != None:
    #             self.printListFromTailToHead(p.next)
    #         print(p.val)


    def createList(self,List):
        lens = len(List)
        for i in range(lens):
            node = ListNode(List[i])
            if i == 0:
                head = node
                p = head
                continue
            p.next = node
            p = p.next
        return head

if __name__ == '__main__':
    List = [1,2,3,4,5]
    s = Solution()
    head = s.createList(List)
    p = head
    while p != None:
        print(p.val)
        p = p.next
    print(s.printListFromTailToHead(head))

