#for string representations of string representations of up to base 62
defaultDigits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#converts the given base 10 fraction to a string fraction in specified base up to specified precision
#int numerator, int denominator, int base, int precision, list<str> digits -> str
def fractionBase(num, den, base, precision = 10, digits = defaultDigits):
    #checking if the provided set of digits is enough for the specified base
    if len(digits) < base:
        raise ValueError(str(len(digits)) + ' digits provided is not enough to represent the base of ' + str(base))

    if base % 1 != 0:
        raise ValueError('Base must be a natural number more than 1')

    #handling the whole part of the fraction
    whole = '0'
    if num >= den:
        #raise ValueError('Provided fraction is more than or equal to 1')
        whole = integerBase(num // den, base, digits)
        num = num % den

    #only keeping the digits we need
    digits = digits[0:base]

    #initializing our working list with the first decimal point
    dec = [digits[-1]]
    digitIndex = base - 1

    #keeping track of the precision level achieved so far
    index = 1

    #keeping track of whether we're still working the digit from the previous iteration
    newDigit = False

    #initializing the working fractions
    numerator = base - 1
    denominator = base
    while index <= precision:
        if newDigit:
            #if new digit we append the highest possible next digit and loop around to test
            digitIndex = base - 1
            dec.append(digits[-1])
            newDigit = False
            numerator *= base
            denominator *= base
            numerator += base - 1
        else:
            #we first check if the working digit is 0
            if dec[-1] == '0':
                #if it is then it means we work on the next digit
                newDigit = True
                index += 1
            #if not we cross multiply and compare instead of dividing and comparing
            else:
                left = den * numerator
                right = denominator * num
                if left < right:
                    #if the working solution is less, then it's right and we move onto the next digit
                    #this means the solution so far is just slightly below the target solution, and the next digit will bring this estimation even closer
                    newDigit = True
                    index += 1
                elif left > right:
                    #if it's not, we deincrement the working solution by one and loop around again
                    #this means the solution so far exceeds the target solution
                    digitIndex -= 1
                    dec[-1] = digits[digitIndex]
                    numerator -= 1
                else:
                    #if equal, we terminate immediately and return our solution
                    #this means we found an exact representation of our desired fraction in our base
                    break
    return whole + '.' + ''.join(dec)

#converts the given base 10 integer into a string integer in the specified base
#int number, int base, list<str> digits -> str
def integerBase(number, base, digits = defaultDigits):
    if number % 1 != 0:
        raise ValueError('Given number is not an integer')

    if number == 0:
        return '0'

    #only keeping the digits we need
    digits = digits[0:base]

    #finding the highest power
    power = 0
    while number > base ** power:
        power += 1
    
    #initialization of the output as a list of 0s
    output = [0] * (power + 1)

    #the actual conversion
    while number > 0:
        output[-power - 1] = number // (base ** power)
        number = number % (base ** power)
        power -= 1

    #if the first digit is 0, we don't need it
    if output[0] == 0:
        output = output[1:]
    
    return ''.join(map(lambda i: digits[i], output))
