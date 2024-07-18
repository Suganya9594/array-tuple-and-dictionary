nums = [2, 3, 5, 3, 7, 2, 5]
non_repeating = None

count_dict = {}

for num in nums:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

for num in nums:
    if count_dict[num] == 1:
        non_repeating = num
        break

if non_repeating is not None:
    print("First non-repeating element:", non_repeating)
else:
    print("No non-repeating element found in the list.")
