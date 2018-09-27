digit_index = '0123456789ABCDEF'


def convert_base(num_as_string, b1, b2):
    '''
    if string is empty return
    if bases are equal return string
    
    if b1 is not 10 convert input to base 10
    if b2 is not 10 convert result of previous operation to b2
    return result
    '''
    if not num_as_string:
        return ''
    result = ''
    neg = False
    if num_as_string[0] == '-':
        num_as_string = num_as_string[1:]
        neg = True
    if b1 == b2:
        return num_as_string
    # Check if string starts with 0, and then clear them off.
    if b1 != 10:
        result = convert_to_ten(num_as_string, b1)
        print result
    if b2 != 10:
        result = convert_from_ten(result, b2)
    if neg:
        return ''.join(['-', result])
    print result
    return result

def convert_to_ten(s, base):
    neg = False
    res = 0
    power = 1
    for c in reversed(s):
        res += (ord(c)-ord('0')) * power
        power *= base
    return str(res)

def convert_from_ten(s, base):
    n = int(s)
    print n
    res = []
    if not n:
        return s 
    while n:
        digit = n % base
        res.append(digit_index[digit])
        n //= base
    print res
    return ''.join(res)[::-1]

#print convert_base("1011", 4, 10)
#print convert_base("234", 5, 16)
print convert_base("615", 7, 13)
