'''
reverse a string using stack.

'''



def reverse_stack(str):
    stack = []
    for char in str:
        stack.append(char)

    # pop all characters of string and add it to a variable
    reverse = ''
    while len(stack) > 0:
        last = stack.pop()
        reverse+=last
    return reverse
str = input('write your string: ')
print(reverse_stack(str))