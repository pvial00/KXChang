# Python3 program to calculate  
# discrete logarithm  
import math; 
  
# Iterative Function to calculate  
# (x ^ y)%p in O(log y)  
def powmod(x, y, p):  
  
    res = 1; # Initialize result  
  
    x = x % p; # Update x if it is more  
               # than or equal to p  
  
    while (y > 0):  
          
        # If y is odd, multiply x with result  
        if (y & 1):  
            res = (res * x) % p;  
  
        # y must be even now  
        y = y >> 1; # y = y/2  
        x = (x * x) % p;  
    return res;  
  
# Function to calculate k for given a, b, m  
def discreteLogarithm(a, b, m):  
    n = int(math.sqrt(m) + 1);  
  
    value = [0] * m;  
  
    # Store all values of a^(n*i) of LHS  
    for i in range(n, 0, -1):  
        value[ powmod (a, i * n, m) ] = i;  
  
    for j in range(n):  
          
        # Calculate (a ^ j) * b and check  
        # for collision  
        cur = (powmod (a, j, m) * b) % m;  
  
        # If collision occurs i.e., LHS = RHS  
        if (value[cur]):  
            ans = value[cur] * n - j;  
              
            # Check whether ans lies below m or not  
            if (ans < m):  
                return ans;  
      
    return -1;  
  
from Crypto.Util import number

def genBase(size):
    A = number.getPrime(size)
    B = number.getPrime(size)
    while B == A:
        B = number.getPrime(size)
    return A, B
    

def keygen(size):
    A, B = genBase(size)
    sk = number.getRandomRange(1, (B - 1))
    return sk, B, A
    
    
msg = 65
size = 8
sk, pk, n = keygen(size)
skB, pkB, nB = keygen(size)
print sk, pk, n
print skB, pkB, nB
p1 = pow(pk, sk, n)
p1B = pow(pk, skB, n)
print "p1", p1, p1B
p2 = pow(p1B, sk, n)
p2B = pow(p1, skB, n)
print "p2", p2, p2B
p3 = pow(pkB, sk, p2)
p3B = pow(pkB, skB, p2B)
print "p3", p3, p3B
p4 = pow(p3B, sk, p2)
p4B = pow(p3, skB, p2B)
print "p4", p4, p4B
#key = number.long_to_bytes(p4)
#print len(key)
Osk = discreteLogarithm(pk, p1, n)
print Osk
o1 = pow(p1B, Osk, n)
print o1
o2 = pow(p3B, Osk, o1)
print o2
Osk = discreteLogarithm(p2, p3, n)
print Osk
o1 = pow(p3B, Osk, n)
print o1
