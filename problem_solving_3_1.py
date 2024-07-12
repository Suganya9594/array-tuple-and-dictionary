sample_list = [10,501,22,37,999,87,351]


even_numbers = []
odd_numbers = []

# looping the list 
for numbers in sample_list:

    # dividing the numbers by two
    # if remainder is zero then it it is a even number
    if numbers % 2 == 0:
        even_numbers.append(numbers)


    else:
        odd_numbers.append(numbers)

# printing the results
print(even_numbers)
print(odd_numbers)
