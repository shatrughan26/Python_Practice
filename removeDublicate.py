arr = [7, 9, 7, 5, 3, 9, 1, 3, 5]
unique_arr = []
for i in arr:
    if i not in unique_arr:
        unique_arr.append(i)
print(unique_arr)