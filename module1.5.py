
# Step 1: Read the input string
s = input()

# Step 2: Initialize a counter variable to zero
vowel_count = 0

# Step 3: Define what a vowel is
vowels = "aeiou"

# Step 4: Loop through each character in the string s
for char in s.lower(): # .lower() ensures we catch 'A' as well as 'a'
    if char in vowels:
        vowel_count += 1

# Step 5: Print the result in the required format
print(f"Number of vowels: {vowel_count}")