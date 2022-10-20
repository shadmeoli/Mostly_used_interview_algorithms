# default and needed libraries and modules
import math
import json, csv
import os, sys


# most have a time complexity of O(n)
# learing algorithim
class Algorithims:


    # floyds tortoise and hare algorithim to find duplicates
    # O(n)
    def findDuplicate(self, nums):
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if hare == tortoise:
                break

        pt1 = nums[0]
        pt2 = tortoise

        while pt1 != pt2:
            pt1 = nums[pt1]
            pt2 = nums[pt2]

        return pt1


    # -- bubble sort algorithim --
    # O(n**2)
    def bubble(self, nums):
        print(nums)
        for i in range(0, len(nums)-1):
            for j in range(0, len(nums) -1 -i):
                nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

    # bubbles([6,4,5,2,3,1])

    
    # O(n)
    def search(self, matrix: [[1,2,3],[4,5,6],[7,8,9]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bott = 0, ROWS -1
        while top <= bott:
            row = (top + bott) //2
            if target > matrix[row][-1]:
                top = row +1
            elif target < matrix[row][0]:
                bott = row -1
            else:
                break
        
        if not(top <= bott):
            return False
        
        row = (top + bot) //2
        l, r = 0, COLS -1
        while l <= r:
            m = (l+r) //2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m -1
            else:
                return True

        return False

        # --stop --


    # singly linked list
    # O(n)
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next
    # cheaking the linked list
    class Linked_list:
        def __init__(self):
            self.head = None
        
        def insert_at_begining(self, data):
            node = Node(data, self.head)
            self.head = node
        
        def print(self):
            if self.head is None:
                print("empty")
                return
            
            itr = self.head
            llstr = ''

            while itr:
                llstr += str(itr.data) + '-->'
                itr = itr.next
            
            print(llstr)
        
        def insert_at_end(self, data):
            if self.head is None:
                self.head = Node(data, None)
                return
            
            itr = self.head
            while itr.next:
                itr = itr.next
            
            itr.next = Node(data, None)
        
        def insert_vals(self, data_list):
            self.head = None
            for data in data_list:
                self.insert_at_end(data)


    # array list and its operations implementaions getting LCM and GCD
    # O(n**2)
    class Mathematics:

        def lcm(self, nums):
            # sort the numbers
            # loop over the least number 
                # use the least numbers untill it is 1
                # use the next least number greater than 1
            # return 
            pass

        def gcd(self, nums):
            pass



    # binaray search and complexity analysis
    # linear serach
    # O(n)
    def locate_val(self, nums, requested):
         # pointer positon
        pointer = 0

        while pointer < len(nums):

            if nums[pointer] == requested:

                return pointer

            pointer += 1

            if pointer  == len(nums):

                return -1

            elif requested not in nums:

                return "Requested number is not present in the table {}".format(nums)


    # searching  a 2D matrix
    def search_and_sort_matrix(self, list):
        for i in range(0, len(list)-1):
            for j in range(0, len(list) -1 - i):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]



#  2D matrix to search
list = [
    [3,1,2,4],
    [7,5,8,6],
]

# algorithim runner
if __name__ == '__main__':
    algorithim = Algorithims()
    print(algorithim.findDuplicate([2,1,3,1,4]))
    print(algorithim.bubble([5,7,1,4,3,6]))
    # print(algorithim.locate_val([5,7,1,4,3,6,2], 2))
    # print(algorithim.search(list, 6))