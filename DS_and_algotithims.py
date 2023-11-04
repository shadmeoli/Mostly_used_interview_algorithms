# most have a time complexity of O(n)
class Algorithims:
    """
        This is the parent entry class housing most of the algorithms

        I have implemented:
            - Floyd's tortoise and hare
            - Locating duplicates
            - Bubble search
            - Binary search
            - Singly linked list
            - searching a 2d Matrix
            - Implicit revers
            - Frequency counter
            - LCM
    """

    # Floyd's tortoise and hare algorithim to find duplicates
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

    def dups(self, nums):
        """
                **Locating dupliactes in a N length array**

                Find duplicates in an array of numbers

                - duplicates can be more than 1
                - if there are more than one duplicates:
                return the max val with duplicates:
                else if there is a less val with a high frequency of repetitions:
                return that one

                case 1:
                input  : [2, 5, 3, 4, 7, 2]
                output : 2

                case 2:
                input  : [2, 4, 3, 5, 4, 2]
                output : 4

                case 3:
                input  : [2, 3, 7, 4, 7, 4, 1, 4]
                output : 4
        """
        visited = []
        dup_val = []

        for num in nums:
            if num in visited:
                dup_val.append(num)
            else:
                visited.append(num)

        vals = {val: dup_val.count(val)+1 for val in dup_val}
        results = [key for key, val in vals.items() if max(
            vals.values()) == val]

        if len(results) > 1:
            return max(results)
        else:
            return results[0]

    # -- bubble sort algorithim --
    # O(n**2)

    def bubble(self, nums):
        print(nums)
        for i in range(0, len(nums)-1):
            for j in range(0, len(nums) - 1 - i):
                nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

    # bubbles([6,4,5,2,3,1])
    # O(n)
    def search(self, target: int, matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bott = 0, ROWS - 1
        while top <= bott:
            row = (top + bott) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bott = row - 1
            else:
                break

        if not (top <= bott):
            return False

        row = (top + bott) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l+r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
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
            node = self.Node(data, self.head)
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
                self.head = self.Node(data, None)
                return

            itr = self.head
            while itr.next:
                itr = itr.next

            itr.next = self.Node(data, None)

        def insert_vals(self, data_list):
            self.head = None
            for data in data_list:
                self.insert_at_end(data)

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
            if pointer == len(nums):
                return -1

            elif requested not in nums:
                return "Requested number is not present in the table {}".format(nums)

    def search_and_sort_matrix(self, list):
        """
                searching  a 2D matrix
                [ [vals]]
                """
        for i in range(0, len(list)-1):
            for j in range(0, len(list) - 1 - i):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]

    def splitter(self, word: str):
        """
                Complete the solution so that it splits the string
                into pairs of two characters.
                If the string contains an odd number of characters
                then it should replace the missing second character
                of the final pair with an underscore ('_').
                """
        if len(word) % 2 == 1:
            word += "_"
        values = []
        for i in range(0, len(word), 2):
            values.append(word[i:i+2])
        resonse = {
            "number _of_pairs": len(values),
            "pairs": values
        }
        return resonse

    # matix search

    def locate(self, x, y, X_axis=[100, 200, 100], y_axis=[50, 100, 100]):
        locations = {X_axis.index(val[0]): val for val in zip(X_axis, y_axis)}
        print(locations)
        locations = [val for val in zip(X_axis, y_axis)]
        for location in locations:
            if (
                (location[0] > x or location[0] == x)
                and
                    (location[-1] > y or location[-1] == y)):
                return f"icon_{locations.index(location)}"
            else:
                continue

    def implicitReverse(self, nums):
        """
        Given an array on length (n)
        recerate a new array having values form the outisde of the array
        coming in

        input : [1,2,3,4,5,6,7,8,9]
        output : [1,9,2,8,3,7,4,6,5]

        INFO : The function give out a generator
        that you can loop over to get the values
        or use a list comprehention to write the values to a list
        """
        for i in range(0, len(nums)//2):
            yield nums[i]
            yield nums[-1-i]

    # frequency for val X in a len(N) 2D-array

    def main(self, nums) -> int:

        x = [nums.count(num) for num in nums]

        if max(x) == min(x):
            return 0
        else:
            freq = {}
            for num in nums:
                if nums.count(num) > 1:
                    freq[num] = nums.count(num)

            return max(freq)

    # this is a move compact version of the above function
    def tower_builder2(self, n):
        """[ QUESTION ]
                Build a pyramid-shaped tower, as an array/list of strings,
                given a positive integer number of floors.

        A tower block is represented with "*" character.

        result:
              *  
             *** 
            *****
                """
        return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

    # LCM
    def lcm(self, nums) -> list[int]:
        iters: list[int] = []
        if iters:
            while max(iters) > 1:
                for i in range(0, len(nums)):
                    iters.append(nums[i]//max(iters))
        else:
            for i in range(0, len(nums)):
                iters.append(nums[i]//2)
        return iters


if __name__ == "__main__":
    alg = Algorithims()
    # floysd_algo = alg.findDuplicate([2,5,3,4,7,2])
    # duplicates = alg.dups([2,5,3,4,7,2])
    # bbl = alg.bubble([2,1,3,5,2,7,3,6,9,8])
    # pair_splitter = alg.splitter("Example")
    # tower = alg.tower_builder2(n=10)
