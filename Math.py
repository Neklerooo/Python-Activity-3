import math

# Get two integers, a and b, from the user
a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))

# Perform calculations
sum_result = a + b
difference_result = a - b
product_result = a * b
quotient_result = a / b
remainder_result = a % b
log_result = math.log10(a)
power_result = a**b

# Display the results
print("Sum of a and b:", sum_result)
print("Difference (a - b):", difference_result)
print("Product of a and b:", product_result)
print("Quotient (a / b):", quotient_result)
print("Remainder (a % b):", remainder_result)
print("Log base 10 of a:", log_result)
print("a raised to the power of b:", power_result)
