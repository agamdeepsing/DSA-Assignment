
# QUes 1
class solution:
    def ispowerof2(self,n):
        if n<=0:
            return False
        while n>0:
            if n==1:
                return True
            elif n%2 == 0:
                n/=2
            else:
                return False
            


# Ques 2
def findsum(n):
    if n<=1:
        return n
    else:
        return n+findsum(n-1)


# QUes 3
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)




# Ques 4
def power(n,p):
    if p == 0:
        return 1
    return (n*power(n,p-1))


# ques 5
def findmax(a,n):
    if n==1:
        return a[0]
    return max(a[n-1],findmax(a,n-1))



# ques 6
def nth(a,d,n):
    return (a+(n-1)*d)


# ques 7
def tostring(list):
    return ''.join(list)

def permute(a,l,r):
    if l == r:
        print(tostring(a))
    else:
        for i in range(l,r):
            a[l],a[i] = a[i],a[l]
            permute(a,l+1,r)
            a[l],a[i] = a[i],a[l]


# ques 8
def product(arr, n):
  
    result = 1
    for i in range(0, n):
        result = result * arr[i]
    return result
