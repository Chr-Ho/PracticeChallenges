# FizzBuzz Challenge
# Chr-Ho
# 12/29/24

# Display in the console 1-100 with each number on a seperate line.
# Each number that is a multiple of 3, replace the number with Fizz
# Each number that is a multiple of 5, replace the number with Buzz
# Each number that is a multiple of 3 and 5, replace the number with FizzBuzz


for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
