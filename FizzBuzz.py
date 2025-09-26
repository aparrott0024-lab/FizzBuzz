# Alex Parrott
# 9-25-25
# Fizz Buzz Extra Credit Attempt

# This function counts to 100
def count_to_100():
    for i in range(1, 101):
        if (i % 3) == 0 and (i % 5) == 0:
            print ("FizzBuzz")
        elif (i % 5) == 0:
            print("Buzz")
        elif (i % 3) == 0:
            print("Fizz")
        else:
            print(i)

count_to_100()
