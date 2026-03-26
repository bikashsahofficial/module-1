# Step 1: Read the input N and convert it to an integer
n = int(input())

# Step 2: Use a dictionary comprehension to generate the squares
# range(1, n + 1) ensures we include N in our loop
squares_dict = {i: i * i for i in range(1, n + 1)}

# Step 3: Print the resulting dictionary
print(squares_dict)