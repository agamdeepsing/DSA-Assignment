
# Ques 1
t.c = O(logn)
s.c = O(1)


class solution:
    def sqrt(self,n):
        if x == 0:
            return 0
        start = 1
        end = n
        while start<end:
            mid = start+(end-start)//2
            if mid == n//mid:
                return mid
            elif mid>n//mid:
                end = mid-1
            else:
                start=mid+1
        return end
    

# Ques 2
def peak(arr,start,end,n):

    mid = start+(end-start)/2
    mid = int(mid)

    if mid == 0 or arr[mid-1] <=arr[mid] and mid == n -1 or arr[mid+1]<=arr[mid]:
        return mid
    elif mid>0 and arr[mid-1]> arr[mid]:
        return peak(arr,start,mid-1,n)
    else:
        return peak(arr,mid+1,end,n)
    

def find(arr,n):
    return peak(arr,0,n-1,n)



# ques 3
def findmissing(arr,n):
    temp = [0]*(n+1)
    for i in range(0,n):
        temp[arr[i]-1]=1
    for i in range(0,n+1):
        if temp[i] == 0:
            ans = i+1
    print(ans)



# QUes 4
t.c = O(nlogn)
s.c= O(n)


class solution:
    def duplicate(self,num):
        num.sort()
        for i in range(1,len(num)):
            if num[i]==num[i-1]:
                return num[i]



# Ques 5
def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    i, j, k = 0, 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            nums1[k] = nums1[i]
            i += 1
            j += 1
            k += 1
    return nums1[:k]


# Ques 6
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        start = 0
        end = len(nums) - 1

        if nums[end] > nums[0]:
            return nums[0]

        while end >= start:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                start = mid + 1
            else:
                end = mid - 1


# Ques 7
def search(nums, target, findStartIndex):
    ans = -1
    start = 0
    end = len(nums) - 1
    while start <= end:
 
        mid = start + (end - start) // 2
 
        if target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1
        else:
            ans = mid
            if findStartIndex:
                end = mid - 1
            else:
                start = mid + 1
 
    return ans
 

# Ques 8
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Map = {}
        result = []
        for num in nums1:Map[num] = Map.get(num,0)+1
        
        for num in nums2:
            if num in Map and Map[num] != 0:
                result.append(num) 
                Map[num] -= 1

        return result 
