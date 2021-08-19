# Python 3 program to
# find log(n) using Recursion
import math
def Log2n(n):

	return 1 + Log2n(n / 2) if (n > 1) else 0

# Driver code
n = int(input())
print("Using method 1")
print(Log2n(n))
print("Using method 2")

# Python3 program to find log(n) using Inbuilt
# Function of math library
print(int(math.log(n, 2)))


