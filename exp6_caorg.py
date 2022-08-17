str1 = input('Input first string: ')
str2 = input('Input second string: ')
print('')
print('The length of string 1 is ' + str(len(str1)))
print('The length of string 2 is ' + str(len(str2)))
print('')
if(len(str1) > len(str2)):
    print('String 1 has more characters than String 2.')
else:
    print('String 2 has more characters than String 1.')
