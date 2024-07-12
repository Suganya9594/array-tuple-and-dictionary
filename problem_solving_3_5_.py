total_number_of_mangoes = [3, 7, 2, 9, 1]
students = 3

total_number_of_mangoes.sort()  # Sort the list of total_number_of_mangoes in non-decreasing order
min_diff = float('inf')  # Initialize minimum difference to infinity

start = 0
end = students - 1

while end < len(total_number_of_mangoes):
    diff = total_number_of_mangoes[end] - total_number_of_mangoes[start]  # Calculate the difference
    if diff < min_diff:
        min_diff = diff
    start += 1
    end += 1

print("Minimum difference between bags given to students:", min_diff)
