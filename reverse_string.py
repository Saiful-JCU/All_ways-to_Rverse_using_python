'''
Reverse a string.
input will be: Hello world
output should be: dlrow olleH
'''


def reverse_str(str):
    reverse = ''
    for char in str:
        reverse = char + reverse
    return reverse
str = input('write your senctece: ')
print(reverse_str(str))