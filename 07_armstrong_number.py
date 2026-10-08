

number = int(input("Enter a number: "))

digits = str(number)
power = len(digits)

total = 0

for digit in digits:
    total = total + int(digit) ** power

if total == number:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
