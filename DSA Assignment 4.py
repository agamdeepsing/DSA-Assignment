
# Ques 1
Since all three arrays are arranged strictly ascending, it is clear that if the current integer of one 
array exceeds that of another, the current integer of the other array cannot be in the intersection.

To identify the integers that are present in all three arrays, use three pointers in each of the three 
arrays. 

The three pointers each point to the start of one of the three arrays at first. Verify the three 
integers that each time the three pointers refer to. 

Move the pointer forward one position if a pointer points to an integer that is smaller than either of 
the other two numbers. The number is only in the intersection if the three integers to which the three 
pointers point are identical. 

then add integer to the result

t.c= O(nlogm)
s.c = O(1)


def arraysIntersection(arr1, arr2, arr3):
    def find(arr, val):
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] >= val:
                right = mid
            else:
                left = mid + 1
        return arr[left] == val

    res = []
    for num in arr1:
        if find(arr2, num) and find(arr3, num):
            res.append(num)
    return res


# Ques 2
Create the getElementsOnlyInFirstList function. The components that are present exclusively in the first 
parameter are returned by this method, which receives two lists of integers.

Recursively store each entry from the second parameter, nums2, in the hashset existsInNums2.

Check each element to see if it is present in the set existsInNums2 as you iterate over the elements in 
the first parameter, nums1. If so, move on to the next element; if not, put it in the onlyInNums1 
collection.

For the parameters (nums1, nums2), call the function getElementsOnlyInFirstList once, and for 
(nums2, nums1), call it a second time.

t.c = O(n+m)
s.c = O(max(n,m))

def getElementsOnlyInFirstList(nums1, nums2):
    onlyInNums1 = set(nums1) - set(nums2)
    return list(onlyInNums1)

def findDifference(nums1, nums2):
    return [getElementsOnlyInFirstList(nums1, nums2), getElementsOnlyInFirstList(nums2, nums1)]



# Ques 3
t.c = O(r*c)
s.c = O(r*c)


def transpose(self, A):
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in xrange(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans


# Ques 4
Time Complexity: O(nlogn)
Space Complexity: O(1)


def arrayPairSum(nums):
    nums.sort()
    total = 0
    for i in range(0, len(nums), 2):
        total += nums[i]
    return total


# Ques 5
t.c = O(logn)
s.c = O(1)


def arrangeCoins(self, n: int) -> int:
    left, right = 0, n
    while left <= right:
        k = (right + left) // 2
        curr = k * (k + 1) // 2
        if curr == n:
            return k
        if n < curr:
            right = k - 1
        else:
            left = k + 1
    return right



# Ques 6
t.c = O(nlogn)
s.c = O(n)

def sortedSquares(A):
    res = [num * num for num in A]
    res.sort()
    return res


# Ques 7
t.c = O(n)
s.c = O(1)

def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
    length = len(ops)
    if length == 0:
        return m*n
    result = [ops[0][0] , ops[0][1]]
    for i in range(1,length):
        result[0] = min(result[0] , ops[i][0])
        result[1] = min(result[1] , ops[i][1])
    return result[0]*result[1]   



# Ques 8
Create a result array with a size of 2 * n.

The nums array should be iterated over from index 0 to n-1:

In the result, place the elements xi+1, or nums[i], at index 2 * i, and yi+1, or nums[i + n], at index 2 * i + 1.

Give us the array of results.


t.c = O(n)
s.c = O(1)



class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [0] * (2 * n)
        for i in range(n):
            result[2 * i] = nums[i]
            result[2 * i + 1] = nums[n + i]
        return result

