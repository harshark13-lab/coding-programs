

numbers = [10, 20, 30, 40, 50, 60, 70]

target = int(input("Enter the number to search: "))

low = 0
high = len(numbers) - 1

found = False

while low <= high:
    middle = (low + high) // 2

    if numbers[middle] == target:
        print("Number found at index:", middle)
        found = True
        break

    elif numbers[middle] < target:
        low = middle + 1

    else:
        high = middle - 1

if not found:
    print("Number not found.")
