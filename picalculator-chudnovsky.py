import decimal
# sets number of digits

def factorial(n):
    fact = decimal.Decimal('1')

    for i in range(1, n + 1):
        fact = fact * i
    return fact

def findPi(numOfDigits):
    decimal.getcontext().prec = numOfDigits
    k = 0
    result = decimal.Decimal('0')
    next = decimal.Decimal('426880') * decimal.Decimal('10005').sqrt()
    while True:
        a = factorial(6 * k)
        b = 545140134 * k + 13591409
        # top of the chudnovsky algorithm
        top = decimal.Decimal(str(a * b))
        c = factorial(3 * k)
        d = factorial(k) ** 3
        e = (-262537412640768000) ** k
        # bottom of the chudnovsky algorithm
        bottom = decimal.Decimal(str(c * d * e))
        result += top / bottom
        print(next / result)
        k += 1
digits = int(input('How much digits to compute (Greater than one): '))
findPi(digits)



