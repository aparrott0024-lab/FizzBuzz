# Alex Parrott
# 9-25-25
# Fizz Buzz Extra Credit Attempt

# This function counts to 100.
def count_to_100():
    for i in range(1, 101):
        # Checks if i is a multiple of 3 AND 5.
        if (i % 3) == 0 and (i % 5) == 0:
            # If so, it prints FizzBuzz in its place.
            print ("FizzBuzz")
        # Checks if i is a multiple of only 5.
        elif (i % 5) == 0:
            # If so, it prints Buzz in its place.
            print("Buzz")
        # Checks if i is a multiple of 3.
        elif (i % 3) == 0:
            # If so, it prints Fizz in its place.
            print("Fizz")
        else:
            # Prints the number if none of these match.
            print(i)

count_to_100()
