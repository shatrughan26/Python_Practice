arr = [7, 9, 7, 5, 3, 9, 1, 3, 5]

min_val = arr[0]
max_val = arr[0]

for i in arr:
    if i < min_val:
        min_val = i
    if i > max_val:
        max_val = i

print("Minimum value:", min_val)
print("Maximum value:", max_val)