
# QUes 1
class solution(object):
    def ispower3(self,n):
        if n == 1:
            return True
        elif n<3:
            return False
        if not n%3:
            return self.ispower3(n/3)
        return False
    

# Ques 2
class Solution:
    def lastRemaining(self, n: int) -> int:
        a1, an = 1, n
        i, step, cnt = 0, 1, n
        while cnt > 1:
            if i % 2:
                an -= step
                if cnt % 2:
                    a1 += step
            else:
                a1 += step
                if cnt % 2:
                    an -= step
            cnt >>= 1
            step <<= 1
            i += 1
        return a1


# QUes 3
def powerSet(str, index, current):
    if index == len(str):
        print(current)
        return
 
    powerSet(str, index + 1,
             current + str[index])
    powerSet(str, index + 1, current)


# Ques 4
def str(str):
    if str == '':
        return 0
    else:
        return 1+str(str[1:])
    


# ques 5
def countstrs(s):
    result = 0
    n = len(s)

    for i in range(n):
        for j in range(i,n):
            if s[i]==s[j]:
                result = result+1

    return result



# ques 6
def hanoi(rod,source=1,auxiliary=2,target = 3):
    if rod>0:
        hanoi(rod-1,source,auxiliary,target)

        hanoi(rod-1,auxiliary,target,source)

hanoi(3)



# ques 7
def print_permutations(str, ans):
    if len(str) == 0:
        print(ans, end=" ")
        return
    
    for i in range(len(str)):
        ch = str[i]
        remaining = str[:i] + str[i+1:]
        print_permutations(remaining, ans + ch)


# ques 8
def isconsonant(c):
    c = c.upper()
    return not (c == "A" or c== "E" or c == "I" or c=="O" or c =="U") and ord(c)>=65 and ord(c)<=90

def totalconsonant(str,n):
    if n==1:
        return isconsonant(str[0])
    return totalconsonant(str,n-1)+isconsonant(str(n-1))