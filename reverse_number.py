'''

'''

def reverse_number(num):
    reverse = 0
    while (num>0):
        last_digit = num % 10
        reverse = reverse * 10 +last_digit
        num = num // 10
    return reverse

n = int(input('write your number: '))
print(reverse_number(n))

# alternaative

num = int(input('write your number: '))
number = str(num)
print('reverse is: ', number[::-1])

