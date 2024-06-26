if __name__ == "__main__":
    # Prompting user input for the size of the pattern
    size = int(input("Enter the size of the pattern: "))
    
    # Using a while loop to iterate through each row
    row = 0
    while row < size:
        # Using a for loop to print asterisks in the current row
        for col in range(size):
            print("*", end="")
        # Moving to the next line after completing the row
        print()
        row += 1
