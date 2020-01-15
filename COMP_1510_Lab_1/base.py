number = (int(input("The Base number converter 1 to 9: ")))

if number < 10:
    max_base_number_10 = number ** 4 - 1
    print("The maximum value is: " + str(max_base_number_10))
else:
    print("Choose from the number 1 to 9")


def new_base_conversion(new_number):
    if new_number <= max_base_number_10:
        quotient = int(new_number / number)
        digit_0 = new_number - (quotient * number)
        quotient_1 = int(quotient / number)
        digit_1 = quotient - (quotient_1 * number)
        quotient_2 = int(quotient_1 / number)
        digit_2 = quotient_1 - (quotient_2 * number)
        quotient_3 = int(quotient_2 / number)
        digit_3 = quotient_2 - (quotient_3 * number)
        print(str(digit_3) + str(digit_2) + str(digit_1) + str(digit_0))

    else:
        print("The value must be less than or equal to the maximum")


new_base_conversion(int(input("Enter the value less than or equal to the maximum: ")))
