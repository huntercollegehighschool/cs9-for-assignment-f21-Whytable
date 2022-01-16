"""
******
PART 4
******

Write a program that prompts the user to enter a numbers. The program will then go through all the numbers from 1 to the input itself and:

- print "fizz" if the number is divisible by 3
- print "buzz" if the number is divisible by 5
- print "fizzbuzz" if the number is divisible by both 3 and 5
- print the number itself if it does not fall into any of the categories above
  
(Tip: order matters!)

What should appear on the console when this program runs:

Enter a number: 21
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17
fizz
19
buzz
fizz




if 
    print("fizz")
  
  elif i % 5:
    print("buzz")
  
  elif i % 3 and i % 5:
    print("fizzbuzz")
  
  else:
    print(i)



"""
# write your code here 

is_divisible3 = False
is_divisible5 = False
remainder3 = 0
remainder5 = 0
n = int(input("Enter a number: "))

for i in range(1, n+1, 1):
  remainder3 = i % 3
  is_divisible3 = remainder3 == 0

  remainder5 = i % 5
  is_divisible5 = remainder5 == 0

  if is_divisible5 == True and is_divisible3 == True:
    print("fizzbuzz")  
  elif is_divisible3 == True:
    print("fizz")
  elif is_divisible5 == True:
    print("buzz")
  else:
    print(i)






