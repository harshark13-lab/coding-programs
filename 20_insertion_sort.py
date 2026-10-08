
numbers = [12, 11, 13, 5, 6]

print("Original list:", numbers)

for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j = j - 1

    numbers[j + 1] = key

print("Sorted list:", numbers)
