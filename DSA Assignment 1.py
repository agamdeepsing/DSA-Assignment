
# Ques 1

algo:
taking 1st value as current and then we apply current + x = target.
if x is present in the list the loop will stop and return the output 
in the form of indexes else it will again search for the x element by moving 
the current variable righwards

Time complexity = o(n^2)
space = o(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):
                if nums[j] == target-nums[i]:
                    return[i,j]
                

nums = [2,7,11,15]
target = 9
output = [0,1]




# Ques 2

approach :
1. we will take a variable count
2. then we will scan thewhole array
3. We shall insert that element in the place of count if the current element does not match val.

t.c = o(n)
s.c = o(1)

class RemoveElement:
    def removeElement(nums: List[int], val: int) -> int:
        # Counter for keeping track of elements other than val
        count = 0
        # Loop through all the elements of the array
        for i in range(len(nums)):
            if nums[i] != val:
                # If the element is not val
                nums[count] = nums[i]
                count += 1
        return count
    




# Ques 3


approach:
iterate over every element over array. and search for K
2. if the elemnt = k then print k
3.if elemrnt >k print the index of the k position. if there is no element >k then k inserted at last.

Time Complexity: O(N)
Auxiliary Space: O(1)

def find_index(arr, n, K):
	
	
	for i in range(n):
		
		# If K is found
		if arr[i] == K:
			return i
			
		
		elif arr[i] > K:
			return i
			
	return n

arr = [1, 3, 5, 6]
n = len(arr)
K = 2
print(find_index(arr, n, K))





# Ques 4

approach:
1. loop from the last index till the first index
2. If the number at current index is smaller than 3 then add one to the number and return the array


Time Complexity: O(n)
Space Complexity: O(1)

class Solution:
    def plusOne(self, digits):
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        newNumber = [0] * (n+1)
        newNumber[0] = 1
        return newNumber



# Ques5


t.c = O((m+n) log(m+n)) 
s.c = O(1)


def merge(self, nums1, m, nums2, n):
        i=0
        for x in range(len(nums1)):
            if i>=n:
                break
            if nums1[x]==0:
                nums1[x]=nums2[i]
                i+=1           
        nums1.sort()





# Ques 6

approach:
sort the array first ,nowcheck for adjacent values whether they are same or not.
     
Time Complexity:  O(N*logN)

Space Complexity: O(1)

def containsDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

nums = [1, 2, 3, 1]
res = containsDuplicate(nums)

# printing the result
if res:
    print("true")
else:
    print("false")





# QUes 7
 approach :
1. move left to right across the array
2. Continue to keep track of non-zero items.
3. Every non-zero element at arr[i] is moved to arr[count] and the count is increased.
4. All non-zero components have previously been moved to the front end upon traversal completion.


Time Complexity: O(n) 
Space: O(1)



def pushZerosToEnd(arr, n):
	count = 0 
	
	
	for i in range(n):
		if arr[i] != 0:
			
			
			arr[count] = arr[i]
			count+=1
	
	
	while count < n:
		arr[count] = 0
		count += 1
		

arr =  [0,1,0,3,12]
n = len(arr)
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)




# QUes 8

appraoch:
1.first seefor the duplicate number.
2. traverse the array take each number and place it in its respective index.
3. if the number is not -1 .hense we find our duplicate number and present it in the output.
4.we will traverse through the extra array, check for the index that has -1, this means it is missing.
Hence we will append this value to our output array.

t.c = o(n)
s.c = o(n)

class ErrorNumsFinder:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numbers = [-1 for i in range(len(nums)+1)]
        output = []
        for num in nums:
            if numbers[num] == -1:
                numbers[num] = num
            else:
                output.append(num)
        
        for i in range(1,len(numbers)):
            if numbers[i] == -1:
                output.append(i)
        return output