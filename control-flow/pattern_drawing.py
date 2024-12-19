
# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in the current row
    for _ in range(size):
        print("*", end="")  # Print asterisks without a newline
    print()  # Move to the next line after completing a row
    row += 1
