# Write a Python program to display the Fibonacci sequence for n terms
n = int(input())
f = 0
s = 1
t = 0
print(f)
print(s)
for i in range(n-2):
  t = f+s
  f = s
  s = t
  print(t)
