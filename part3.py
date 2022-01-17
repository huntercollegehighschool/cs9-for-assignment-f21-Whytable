"""
******
PART 3
******

Write a program that prompts the user to enter two integers, one representing the base of a rectangle, and one representing the height. The program will then print a rectangle made of asterisks (*) with those dimensions. 

(Hint: this may involve nested for loops(ie. a for loop inside a for loop), but it does not have to. Concatenating/adding strings ('*' + '*') or replicating strings ('*' * 3) may be helpful here.)

An example of what should appear on the console when the program runs:

Enter the base: 7
Enter the height: 3

*******
*******
*******

"""

#write your code here 

L = int(input("Enter the base of the rectangle: "))
H = int(input("Enter the height of the rectange: "))

if L > 0 and H > 0:
  for i in range(1, H + 1, 1):
    print('*' * L)

if L < 1 or H < 1:
  print("Run the program again with an integer!")
