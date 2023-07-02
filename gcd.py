#The greatest common divisor of two positive integers, A and B, is the largest number that can be evenly divided into both of them. Euclid’s algorithm can be used to find the greatest common divisor(GCD) of two positive integers. You can use this algorithm in the following manner. a. Compare the remainder of dividing the largest number by the smallest number. b. Replace the largest number with the smallest number and the smaller number with the remainder c. Repeat this process until the smaller number is zero The larger number at this point is the GCD of A and B. Write a program that lets the user to enter two integers and then prints each step in the process of using the Euclid’s algorithm to find their GCD
def gcd (x, y):  
  if (y == 0): 
    return x  
  else:  
    return gcd (y, x % y)  
  
a=int(input())
b=int(input())
print(gcd(a,b))
