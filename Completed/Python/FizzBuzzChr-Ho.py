# FizzBuzz Challenge
# Chr-Ho
# 12/29/24

# Write a program that prints the numbers from 1 to 100.
# For multiples of 3, replace the number with Fizz
# For multiples of 5, replace the number with Buzz
# For multiples of both 3 and 5, replace the number with FizzBuzz


for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
