
# Ques 1
t.c = R*c
s.c = O(n)
def constructArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        t = 0
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                ans[r][c] = original[t]
                t += 1
        return ans



# Ques 2
t.c = O(1)
s.c = O(1)
 
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)
    

the expression 2 * n + 0.25 represents the quadratic equation.The value of k, which stands for the number of whole rows, may be found by taking the square root and subtracting 0.5.
    




# Ques 3
firstly try to arrange/convert the element in the squares amd then apply the soting algo.

t.c = O(nlogn)
s.c = O(n)


def square(arr,n):
    for i in range(n):
        arr[i] = arr[i] *arr[i]
    arr.sort()

arr = [-4,-1,0,3,10]
n = len(arr)

for i in range(n):
    print(arr[i],end = " ")

square(arr,n)

for i in range(n):
    print(arr[i],end = ' ')

# Ques 4
Define a process The method getElementsOnlyInFirstList takes two lists of integers as input and outputs the items that are only present in the first list.

This approach makes advantage of the algorithm we previously discussed: Every element of the first list should be checked against the second list in a loop. In this case, we stop and set the boolean variable existInNums2 to true if the element is found in the second list.

If the variable existInNums2 is false after examining every element in the second list, only then do we save the value in the list onlyInNums1.

Give back onlyInNums 1.

For the parameters (nums1, nums2), call the function getElementsOnlyInFirstList once, then for (nums2, nums1), call it again.

t,c = O(n*m)
s.c = O(1)

def elements_in_lsit(nums1,nums2):
    num1 = set()
    for i in nums1:
        num2 = False
        for j in nums2:
            if j == i:
                num2 = True
                break
        if not num2:
            num1.add(i)
    return list(num1)
def find_difference(self,nums1,nums2):
    return[self.elements_in_list (nums1,nums2),self.elements_in_list(nums2,nums1) ]







# Ques 5
Determine the size of the [A[i] - d, A[i] + d] range for each A[i] in array B. Increase the response if the length is 0.

Lower_bound(begin(B), end(B), A[i] - d) can be used to determine the beginning of the range (A[i] - d).


Upper_bound(begin(B), finish(B), n + d) can be used to determine the element that follows the range's end point (the element after A[i] + d).

The length of the range is 0 if these two iterators are equal.



t.c = o(nlogn)
s.c = O(1)


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for a in arr1:
            valid = True
            for b in arr2:
                if abs(a - b) <= d:
                    valid = False
                    break
            if valid:
                count += 1
        return count



# Ques 6
traverse the entire array that has been given.
Increase the arr[i]%n'th element by n for each element in the array.
Retrace your steps over the array and output every index i for which arr[i]/n is larger than 1. This ensures that the index has been expanded to include the value n.

This method works because every element falls between 0 and n-1, and arr[i] would only exceed n if the value "i" had appeared more than once.



t.c = O(n)
s.c = O(1)

nums = [0, 4, 3, 2, 7, 8, 2, 3, 1]
arr = len(nums)
for i in range(arr):
  
    x = nums[i] % arr
    nums[x] = nums[x] + arr
  
for i in range(arr):
    if (nums[i] >= arr*2):
        print(i, " ")


# Ques 7
1. firstly you have to look for center element in the ars
2. if center > first This suggests that the inflection point will be to the right of mid, where we must search for it.
3.if center < first This suggests that the inflection point will be to the left of mid, where we must search for it.
3. nums[center]>nums[center+1]
center+1 is small
nums[center-1]>nums[center]
cenetrr is smaall

t.c = o(logn)
s.c = O(1)

def findmin(nums):
    if len(nums)==1:

        return nums[0]
    
    start = 0
    end = len(nums)-1

    if nums[end]>nums[0]:
        return nums[0]
    
    while end > start:
        center = start +(end - start ) // 2
        if nums[center] > nums[center+1]:
            return nums[center+1]
        

        
        elif nums[center-1]>nums[center]:
            return nums[center]
        
        
        elif nums[center]>nums[0]:
            start = center+1

        
        else:
            end = center -1




# Ques 8
approach hashmap
1. sort the ars
2. iterate through the ars
3. create the empty list in which the result gets stored. result = []
4. Reduce the frequency of the element that has a double value of the first element and add the first element to the result list.
5. trsversr the ars
6. print the elements in the result[]

t.c = O(nlogn)
s.c = O(n)

def original_ars(arr):
    frequency = {}
    for i in range(0,len(arr)):
        if arr[i] in frequency:
            frequency[arr[i]] +=1
        else:
            frequency[arr[i]] =1

    arr.sort()
    result = []

    for i in range (0,len(arr)):
        frequency1 = frequency[arr[i]]:
        if frequency1 >0 :
            result.append(arr[i])
            frequency[arr[i]] -= 1
            multilply = 2 *arr[i]

    return result

arr = [[1,3,4,2,6,8]]
result = original_ars(arr)

for i in range(0,len(result)):
    print(result[i],end = " ")


