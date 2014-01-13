'''

PROJECT EULER

Problem 21 - amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n). If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers. For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''


def proper_divisor(a):
    '''Sums proper divisors'''
    output = 0 
    for x in range (1,a-1):
        result = a % x
        if result == 0: output += x
        else: 
            pass
    return output 


def is_amicable(num1):
    '''Returns True if two given
    integers are an amicable pair.'''
    sum1 = proper_divisor(num1)
    sum2 = proper_divisor(sum1)
    if num1 == sum2:
        return True


def sum_amicable(n):
    '''Sums amicable numbers within 
    a given upper bound of n.'''
    # sets sum to zero
    output = 0 
    # sets range of input values 
    for x in range(n):
        # sums proper divisors of input value 
        y = proper_divisor(x)
        # evaluates if derived pair is amicable
        if is_amicable (x) == True and x != y:
            if y < n: 
                # increments the output sum 
                output = output + x
    return output

# prints the sum of amicable numbers under 10,000
print sum_amicable(10000)

