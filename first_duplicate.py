"""
Given an array a that contains only numbers in the range from 1 to a.length,
find the first duplicate number for which the second occurrence has the minimal
index. In other words, if there are more than 1 duplicated numbers, return the
number for which the second occurrence has a smaller index than the second
occurrence of the other number does. If there are no such elements, return -1.

=== Example ===

for:
    a = [2, 1, 3, 5, 3, 2]

the output should be:
    firstDuplicate(a) = 3
"""

def repeated(a):
    a_set = set()
    for i in a:
        if i in a_set:
            return i
        else:
            a_set.add(i)


def firstDuplicate(a):
    if len(a) == len(set(a)):
        return -1
    else:
        return repeated(a)


if __name__ == '__main__':
    # tests
     print([2, 1, 3, 5, 3, 2])
     print([2, 4, 3, 5, 1])
