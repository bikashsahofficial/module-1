#Take input from the user
text=input()

#Sort the characters of the string
#sorted() returns a list of characters in ascending Unicode order
sorted_chars = sorted(text)

#Join the list of characters back into a single string
result = "".join (sorted_chars)

#Print the final result
print(result)