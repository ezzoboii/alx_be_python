if __name__ == "__main__":
    # Prompting user input for the number
    number = int(input("Enter a number to see its multiplication table: "))
    
    # Generating and printing the multiplication table
    for i in range(1, 11):  # Range from 1 to 10 (inclusive)
        result = number * i
        print(f"{number} * {i} = {result}")
