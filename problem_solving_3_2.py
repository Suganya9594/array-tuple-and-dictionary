num_list = [10,501,22,37,100,999,87,351]

# Create an empty list to store the prime numbers
prime_numbers = []

for number in num_list:
    # Define a not_a_prime_number variable
    not_a_prime_number = False

    
    if number > 1:
        # Check for factors of the numbers
        for i in range(2, number):
            if (number % i) == 0:
                # If factor is found, set not_a_prime_number to True
                not_a_prime_number = True
                # Break out of loop
                break

        # Check if not_a_prime_number is False 
        if not not_a_prime_number:
            prime_numbers.append(number)  

# Print the list of prime numbers
print("Prime numbers :", prime_numbers)
