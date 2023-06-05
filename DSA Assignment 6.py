
# Ques 1
The smallest and largest piece that we haven't yet put should be noted. insert the little element if we observe a "I," else, insert the huge element.

t.c = O(n)
s.c = O(1)

class Solution(object):
    def diStringMatch(self, num):
        start = 0
        end =  len(num)
        result = []
        for x in num:
            if x == 'I':
                result.append(start)
                start += 1
            else:
                result.append(end)
                end -= 1

        return result + [start]


# Ques 2
O(log(m * n)) time complexity.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Binary Search
        row = len(matrix)
        column = len(matrix[0])
        i = 0
        j =  (row * column) - 1

        while i <= j:
            mid = (i + j) >> 1
            mid_element = matrix[mid // column][mid % column] 
            if mid_element == target:
                return True
            elif mid_element < target:
                i = mid + 1
            else:
                j = mid - 1
        return False


# Ques 3
The apex must be when we can no longer go from left to right. Make sure the peak is neither the first 
nor the last component. After that, we descend. The array is legitimate if we make it to the end; else, 
it is invalid.


t.c = O(n)
s.c = O(1)

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        N = len(A)
        left = 0
        right = N - 1

        if N < 3 or A[left] >= A[left + 1]:
            return False

        while left < N - 1 and A[left] < A[left + 1]:
            left += 1

        while right > 0 and A[right - 1] > A[right]:
            right -= 1

        return left == right == N - 1



# ques 4
t.c = O(n*n)
s.c = O(1)

def max_length(nums):
    maximum = 0
    for start in range(0,len(nums)):
        zero = 0
        one = 0
        for end in range(start, len(nums)):
            if nums[end]==0:
                zero += 1
            
            elif zero == one:
                maximum = max(maximum,end-start+1)

            else:
                one += 1
    return maximum
            


# ques 5
t.c = O(nlogn)
s.c = O(1)


lass Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        n, res = len(nums1), 0
        for i in range(n):
            res += nums1[i] * nums2[n - i - 1]
        return res



# ques 6
t.c = O(nlogn)
s.c = O(1)

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        doubled = {}
        result = []
        changed.sort(reverse=True)
        for c in changed:
            if doubled.get(c * 2, 0) > 0:
                result.append(c)
                doubled[c * 2] -= 1
            else:
                doubled[c] = doubled.get(c, 0) + 1
        size = len(changed)
        if size % 2 == 1:
            size += 1
        return result if len(result) == size // 2 else []




# ques 7
t.c = O(n*n)
s.c= O(1)

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        resultult = [[0] * n for _ in range(n)]
        continue1 = 1
        for i in range((n + 1) // 2):
            
            for j in range(i, n - i):
                resultult[i][j] = continue1
                continue1 += 1
            
            for j in range(i + 1, n - i):
                resultult[j][n - i - 1] = continue1
                continue1 += 1
            
            for j in range(n - i - 2, i - 1, -1):
                resultult[n - i - 1][j] = continue1
                continue1 += 1
           
            for j in range(n - i - 2, i, -1):
                resultult[j][i] = continue1
                continue1 += 1

        return resultult





# Ques 8 
t.c = O(r1*c1*c2)
s.c = O(r1*c2)

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        r1, c1, c2 = len(mat1), len(mat1[0]), len(mat2[0])
        resultult = [[0] * c2 for _ in range(r1)]
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    resultult[i][j] += mat1[i][k] * mat2[k][j]
        return resultult