def is_happy_number(n):

    # storing the results for optimisation
    seen_numbers = set()
    
    # conditions to eval that number is not equal to 1 and not in seen numbers
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = sum(int(digit)**2 for digit in str(n))
    
    return n == 1

# Function to display the result
def check_happy_number(n):
    
    if is_happy_number(n):
        print(f"{n} is a happy number!")
    else:
        print(f"{n} is not a happy number.")



num_list = [10,501,22,37,100,999,87,351]

for numbers in num_list:
    check_happy_number(numbers)