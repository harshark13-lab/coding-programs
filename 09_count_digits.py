

number = int(input("Enter a number: "))

number = abs(number)

if number == 0:
    count = 1
else:
    count = 0

    while number > 0:
        number = number // 10
        count = count + 1

print("Number of digits:", count)
