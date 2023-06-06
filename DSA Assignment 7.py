
# QUes 1
t.c = O(n)
s.c  = O(1)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        t1 = {}
        s1 = {}
        
        for i, j in zip(s, t):
            
            if (i not in t1) and (j not in s1):
                t1[i] = j
                s1[j] = i
            
            elif t1.get(i) != j or s1.get(j) != i:
                return False
            
        return True
    


# Ques 2
t.c = O(n)
s.c = O(1)

class Solution(object):
    def isStrobogrammatic(self, num):

        maps = {("6","9")}
        i = 0
        j = len(num)-1
        while i<=j:
            if (num[i],num[j]) not in maps:
                return False
            i+=1
            j-=1
        return True
    

# QUes 3
def addStrings(num1, num2):
    result = ""
    carry = 0
    i = len(num1) - 1
    j = len(num2) - 1
    
    while i >= 0 or j >= 0 or carry > 0:
        if i >= 0:
            carry += int(num1[i])
            i -= 1
        if j >= 0:
            carry += int(num2[j])
            j -= 1
        result = str(carry % 10) + result
        carry //= 10
    
    return result




# Ques 4
class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split(" ")[::-1])[::-1]




# ques 5
class Solution:

    def reverseStr(self, s, k):
        l = list(s)
        i = k - 1
        while i < len(l) + k:
            a = l[:i - k + 1]
            b = l[i - k + 1:i + 1]
            c = l[i + 1:]
            l = a + b[::-1] + c
            i += 2 * k
        return ''.join(l)


# ques 6
t.c = O(1)
s.c = O(1)


class Solution :
    def  rotateString(self, s,  goal) :
        return (len(s) == len(goal) and  goal in (s + s) )

# ques 7
import itertools

class Solution(object):
    def backspaceCompare(self, s, t):
        def F(s):
            result = 0
            for x in reversed(s):
                if x == '#':
                    result += 1
                elif result:
                    result -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(s), F(t)))



# ques 8
t.c = O(n)
s.c = O(1)


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)

        x, y = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, n):
            x, y = coordinates[i]

            if (y - y) * (x - x1) != (y - y1) * (x - x):
                return False

        return True