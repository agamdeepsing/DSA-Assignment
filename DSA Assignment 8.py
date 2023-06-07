
# QUes 1
class Solution:
    def minimumDeleteSum(self, s1, s2):
        n = len(s1)
        m = len(s2)
        s1 = " " + s1
        s2 = " " + s2
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, m + 1):
            dp[0][i] = dp[0][i - 1] + ord(s2[i])
        
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i])
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i]), dp[i][j - 1] + ord(s2[j]))
        
        return dp[n][m]

# Ques 2

t.c = O(n)
s.c = O(1)


class Solution:
    def checkValidString(self, s):
        start = end = 0
        for c in s:
            start += 1 if c == '(' else -1
            end += 1 if c != ')' else -1
            if end < 0:
                break
            start = max(start, 0)

        return start == 0



# QUes 3
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def result(i, j):
            if i == 0:
                return j
            if j == 0:
                return i
            if word1[i-1] == word2[j-1]:
                return result(i-1, j-1)
            return 1 + min(result(i, j-1), result(i-1, j), result(i-1, j-1))

        return result(len(word1), len(word2))



# Ques 4
def tree2str(self, root: Optional[TreeNode]) -> str:
        
                    
        if(root == None):
            return ""
        
        output: str = str(root.val)
        
        if (root.left != None or root.right != None):
            output += "(" + self.tree2str(root.left) + ")"
            
        if (root.right != None):
            output += "(" + self.tree2str(root.right) + ")"          
        
        return output;   


# ques 5
from typing import List

class Solution:
    def compress(self, array: List[str]) -> int:
        count = 1
        index = 0
        for i in range(1, len(array)):
            if array[i] == array[i-1]:
                count += 1
            else:
                array[index] = array[i-1]
                index += 1
                if count > 1:
                    for digit in str(count):
                        array[index] = digit
                        index += 1
                count = 1

        array[index] = array[-1]
        index += 1
        if count > 1:
            for digit in str(count):
                array[index] = digit
                index += 1

        return index



# ques 6
class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        c = collections.Counter(p)
        cur = collections.Counter(s[:len(p)])
        for i in range(len(s)-len(p)+1):
            if cur==c:
                res.append(i)
            if i == len(s)-len(p):
                break
            cur[s[i]]-=1
            if cur[s[i]]==0:
                del cur[s[i]]
            cur[s[i+len(p)]]+=1
        return res


# ques 7
def decodeString(self, s: str) -> str:
    while '[' in s:

		s = re.sub(r'(\d+?)\[(\w+?)\]', lambda m: int(m.group(1))*m.group(2), s)
    return s


# ques 8
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            char_counts = set()
            for ch in s:
                if ch in char_counts:
                    return True
                char_counts.add(ch)
            return False

        differing_indices = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                differing_indices.append(i)

        if len(differing_indices) != 2:
            return False

        i, j = differing_indices
        return s[i] == goal[j] and s[j] == goal[i]


