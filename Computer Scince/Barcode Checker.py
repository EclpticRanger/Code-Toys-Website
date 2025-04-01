code = input("Enter a 13-digit barcode: ")

if len(code) != 13 or not code.isdigit():
    print("Invalid input. Please enter exactly 13 digits.")
else:
    checksum_digit = int(code[-1])
    weighted_sum = 0
    for i in range(12):
        digit = int(code[i])
        if i % 2 == 0:
            weighted_sum += digit
        else:
            weighted_sum += digit * 3
    calculated_checksum = (10 - (weighted_sum % 10)) % 10
    if calculated_checksum == checksum_digit:
        print("Valid")
    else:
        print("Not Valid. Last digit should be:", calculated_checksum)
