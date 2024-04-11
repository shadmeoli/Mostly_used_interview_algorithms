"""
[THIS IS A QUESTION i GOT FROM CODES WARS] - THIS IS JUST MY SOLUTION YOU DOSEN'T MEAN
IS THE RIGHT WAY OF DOING IT


An integer partition of n is a weakly decreasing list of positive integers which sum to n.

For example, there are 7 integer partitions of 5:

[5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1].
Write a function which returns the number of integer partitions of n.
The function should be able to find the number of integer partitions of
n for n at least as large as 100.
"""


def partition_count(n):
    partition_count = [0] * (n + 1)
    partition_count[0] = 1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partition_count[j] += partition_count[j - i]

    return partition_count[n]


if __name__ == "__main__":
    print(partition_count(5))
