def divisible_one(number):
    if number % 1 == 0:
        return "True"
    else:
        return "False"


def divisible_two(number):
    if number % 2 == 0:
        return "True"
    else:
        return "False"


def divisible_three(number):
    if number % 3 == 0:
        return "True"
    else:
        return "False"


def divisible_four(number):
    if number % 4 == 0:
        return "True"
    else:
        return "False"


def divisible_five(number):
    if number % 5 == 0:
        return "True"
    else:
        return "False"


def divisible_six(number):
    if number % 6 == 0:
        return "True"
    else:
        return "False"


def divisible_seven(number):
    if number % 7 == 0:
        return "True"
    else:
        return "False"


def divisible_eight(number):
    if number % 8 == 0:
        return "True"
    else:
        return "False"


def divisible_nine(number):
    if number % 9 == 0:
        return "True"
    else:
        return "False"


def divisible_ten(number):
    if number % 10 == 0:
        return "True"
    else:
        return "False"


smallnum = int(input("Enter the small number : "))
bignum = int(input("Enter the big number : "))

if smallnum == 1:
    print(divisible_one(bignum))
elif smallnum == 2:
    print(divisible_two(bignum))
elif smallnum == 3:
    print(divisible_three(bignum))
elif smallnum == 4:
    print(divisible_four(bignum))
elif smallnum == 5:
    print(divisible_five(bignum))
elif smallnum == 6:
    print(divisible_six(bignum))
elif smallnum == 7:
    print(divisible_seven(bignum))
elif smallnum == 8:
    print(divisible_eight(bignum))
elif smallnum == 9:
    print(divisible_nine(bignum))
elif smallnum == 10:
    print(divisible_ten(bignum))
else:
    print('This program is not programmed to divide by numbers greater than ten.')