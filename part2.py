"""
******
PART 2
******
Write a program that asks the user to enter a positive integer n. The program will then print the sum of the first n positive cubes.

For example, if the user types in 4, the program should print 100 (since 1^3 + 2^3 + 3^3 + 4^3 = 100).
"""

#write your code here
def cube(x):
  return x * x * x

ans = 0

n = int(input("Input an integer to find the sum of its positive cubes: "))

if n > 0:
  for i in range(1, n + 1, 1):
    num = cube(i)
    ans = ans + num
print(ans)

if n < 1:
  print("That is not a positive integer!")