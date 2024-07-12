def sum_first_and_last_digit(number):
    # Convert the number to a string to easily access the digits
    number_str = str(abs(number))
    
    # Find the first and last digits using string indexing
    first_digit = int(number_str[0])
    last_digit = int(number_str[-1])
    
    # Sum the first and last digit
    result = first_digit + last_digit
    
    return result

# Input from the user
user_input = int(input("Enter an integer: "))

# Calculate the sum of the first and last digit
sum_digits = sum_first_and_last_digit(user_input)

# Print the result
print(f"The sum of the first and last digit is: {sum_digits}")
