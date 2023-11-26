def two_positive(a, b, c):

    # Count the number of positive integers
    count_positive = sum(x > 0 for x in (a, b, c))

    # Check if exactly two of the three integers are positive
    return count_positive == 2

# Get user Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Calculate the result by calling the function
result = two_positive(a, b, c)
print(f"The result is: {result}")