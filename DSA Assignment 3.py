
# Ques 1
Sort the nums input array.

Create the variable diff, which will be used to hold the discrepancy between the goal and the triplet's total. Set up a variable called result to hold the total of the closest triplet discovered thus far.

From the first to the second-to-last entry, iterate through the input array nums.

Create two pointers with initial values on the left and right to look for the final two components whose sums are closest to the desired value.

Calculate the triplet nums[i] + nums[left] + nums[right] while left right.

Update result to the sum if there is a less absolute difference between the target and the sum than there is between the target and the current value of res.

Increase the left pointer if the sum is less than the desired value. Otherwise, move the right cursor downward.

Give the result value




t.c = O(N**2)
s.c = O(1)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float('inf')
        result = 0
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(target - total) < diff:
                    diff = abs(target - total)
                    result = total
                if total < target:
                    left += 1
                else:
                    right -= 1
        return result


#Ques2
t.c= O(n**4)
s.c = O(n**4)

use a hashmap and set a varaible answer that willl store all the possiblel quadruplets.

use a m var for storing the sum of all the pairs with the correspopnding indexes.

tore the sum of all pairs of elements (arr[i], arr[j]) with their indices (i, j) in the M.

if the value (K – sum) exists in the M, then store the current quadruplets in the HashMap ans.


class Pair:
    def __init__(self,x,y):
        self.index1 = x
        self.index2 = y

def foursum(nums,target):

    map = {}
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            sum =nums[i]+nums[j]

            if sum not in map:
                map[sum] = [Pair(i,j)]

            else:
                map[sum].append(Pair(i,j))


    answer = set()
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            ans =target-(nums[i]+nums[j])

            if ans in map:
                temp = map[ans]

                for pair in temp:
                    if pair.index1 != i and pair.index1 !=j and pair.index2 != i and pair.index2 != j:
                        l1 = nums[pair.index1],nums[pair.index2],nums[i], nums[j]

                        l1.sort()

                        answer.add(tuple(l1))

    
    result = list(answer)[::-1]
    return result

arr= [1,0,-1,0,-2,-2]
K = 0
result = foursum(arr,K)
for i in result:
    print(r)


# Ques 3
Time complexity : O(n)
Space complexity : O(1)

def nextPermutation(nums):
    i = len(nums)-2
    while i>=0 and nums[i+1]<=nums[i]:
        i-=1
    if i>=0:
        j = len(nums)-1
        while nums[j]<=nums[i]:
            j-=1
        swap(nums,i,j)
    reverse(nums,i+1)

def reverse(nums,start):
    i=start
    j = len(nums)-1
    while i<j:
        swap(nums,i,j)
        i+=1
        j-=1

def swap(nums,i,j):
    nums[i],nums[j] = nums[j],nums[i]


# Ques 4
using the binary search.

initailse the code with setting the value of start and end parameter as 0 and n-1. 

then we need to calcualte the mid value by (start +end)/2

if arr[mid] is found equal to the target value then mid is the answer.

if arr[mid] exceeds target, set high = mid – 1 Otherwise, set  low = mid + 1. 

t.c  = o(logn)
s.c = O(1)

def find(arr,n,target):
    start = 0
    end = n-1
    while start<=end:
        mid = (start+end)/2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            start = mid+1
        else:
            end = mid-1

        return end+1
    
arr = [1,3,5,6]
n = len(arr)
target = 5
print(find(arr,n,target))



# Ques 5
Start at the end of the vector, set the final element to 0 if it is 9 or quit the loop otherwise.

Insert 1 at the start if the loop set all numbers to 0 (or if all digits were 9).
If not, move the element up from where the loop stopped.

No carry, division, or modulo are required.


t.c= O(n)
s.c = O(1)


def add(nums):
    index = len(nums)-1
    while index >0 and nums[index]==9:
        nums[index]=0
        index-=1

    if index<0:
        nums.insert(0,1)

    else:
        nums[index]+=1

nums = [1,2,4]
add(nums)
for i in nums:
    print(i,end = " ")


# Ques 6
iterate over all of the numsnums items.

See if pop's key is in hash_tablehash_table.

Otherwise, create a key/value pair.

Hash_tablehash_table only has one element, thus use popitem to retrieve it.

t.c = o(n)
s.c = O(n)

def singleNumber(nums):
    hash_table = {}
    for i in nums:
        try:
            hash_table.pop(i)
        except:
            hash_table[i] = 1
    return hash_table.popitem()[0]





#Ques 7
t.c = O(n)
s.c = O(1)


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        i = 0
        
        while i < len(nums):
            start = nums[i]
            end = start
            
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                end = nums[i + 1]
                i += 1
            
            if start != end:
                ranges.append(str(start) + "->" + str(end))
            else:
                ranges.append(str(start))
            
            i += 1
        
        return ranges



#Ques 8
t.c = o(nlogn)
s.c = 0(1)


def Meetings(intervals):

    intervals.sort(key=lambda x: (x[0], x[1]))

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True
