
# Ques 1
Time Complexity: O(NlogN)
Space Complexity: O(1)

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        output=0
        for i in range(0,len(nums),2):
            output+=min(nums[i],nums[i+1])
        return(output)


# Ques 2
approach:
1. first sort the candies, then try to count the total unique candies by comparing elements in the array that you have sorted. This removes the need to do repeated traversals.

appraoch2:
use a hashset
Remember that duplicate items are not allowed in sets, thus attempting to add an item that already exists in a set will have no effect.

time complexity:O(N)
space complexity:O(N)


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        unique_candies = len(set(candyType))
        return min(unique_candies, len(candyType) // 2)



# Ques 3
approach: 1.We don't need to care about the order of the numbers or their index in N as our target harmony array deals with the absolute value of its components and since it's a subsequence of our numbers array (N).

2.The implication is that we should begin by creating a frequency map from N if the only thing that matters is the numbers that appear in N, not their order or index.

3.Then, by adding the frequency of each number (key) with the frequency of key+1, we can iterate through the entries in our frequency map (freq) and keep track of the largest value discovered.

4.The best outcome (ans) should then be returned.


t.c = O(N)
s.c = O(N)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}
        ans = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for key, val in freq.items():
            if (key + 1) in freq:
                ans = max(ans, val + freq[key + 1])
        return ans



# Ques 4
Time:O(n)
Space:O(1)

class Solution:
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    for i, flower in enumerate(flowerbed):
      if flower == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
        flowerbed[i] = 1
        n -= 1
      if n <= 0:
        return True

    return False



# Ques 5
To determine the largest product, we don't necessarily need to sort the provided numsnumsnums array. Instead, by iterating over the numsnumsnums array just once, we can only locate the two lowest values—min1min1min1 and min2min2min2—and the three biggest values—max1,max2,max3max1,max2,max3—in the array.

To obtain the needed maximum product, we must find the greater value out of min1min2max1min1 times min2 times max1min1min2max1 and max1max2max3max1 times max2 times max3max1max2max3.



Time complexity : O(n)
Space complexity : O(1)


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        #float('-inf') to represent negative infinity.
        min1 = float('inf')
        min2 = float('inf')
        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')
        
        for n in nums:
            if n <= min1:
                min2 = min1
                min1 = n
            elif n <= min2:
                min2 = n
            
            if n >= max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2:
                max3 = max2
                max2 = n
            elif n >= max3:
                max3 = n
        
        return max(min1 * min2 * max1, max1 * max2 * max3)



# Ques 6

t.c = O(logn)
s.c = O(logn)


class Solution:
    def search(self, nums, target):
        return self.binary_search(nums, target, 0, len(nums) - 1)

    def binary_search(self, nums, target, start, end):
        if start > end:
            return -1

        mid = (end - start) // 2 + start
        mid_num = nums[mid]

        if mid_num == target:
            return mid

        if target < mid_num:
            return self.binary_search(nums, target, start, mid - 1)

        return self.binary_search(nums, target, mid + 1, end)




# Ques 7
To check whether an array A is monotone increasing, we'll check A[i] <= A[i+1] for all i. The check for monotone decreasing is similar.

t.c = O(N)
s.c = O(1)


class Solution(object):
    def isMonotonic(self, A):
        return (all(A[i] <= A[i+1] for i in xrange(len(A) - 1)) or
                all(A[i] >= A[i+1] for i in xrange(len(A) - 1)))


# Ques 8
If min(A) + K < max(A) - K, then return max(A) - min(A) - 2 * K
If min(A) + K >= max(A) - K, then return 0

t.c =O(n)
s.c = O(1)

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(A) - min(A) - 2 * K)
