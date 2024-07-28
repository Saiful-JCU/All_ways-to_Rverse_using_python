'''
Reverse a string using a recursive function.
'''

str = input("write your string: ")
print(str[::-1])

# alternative

def Reverse_recursive(str_1):
    if len(str_1) == 0:
        return str_1
    else:
        return Reverse_recursive(str_1[1:]) + str_1[0] #

str_1 = input("write your string: ")
print('your reverse string is: ', Reverse_recursive(str_1))


