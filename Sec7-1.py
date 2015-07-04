def sumDigits(s):
    result = 0
    for e in s:
        try:
            result += int(e)
        except ValueError:
            print e, 'is not an integer.'
    return result

a = sumDigits('a2b45c')
print a