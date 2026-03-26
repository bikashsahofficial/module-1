# Step 1: Get the input N and convert it to an integer
n = int(input())

# Step 2: Apply the formula sum = n * (n + 1) / 2
# We use integer division // to ensure the result is a whole number (55 instead of 55.0)
total_sum = n * (n + 1) // 2

# Step 3: Print the result using an f-string to match the required output format
print(f"The sum of the first {n} positive integers is {total_sum}")