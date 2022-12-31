# Count and Len Functions method 

str1 = "Python is awesome, isn't it?"

# Count the lenth

print('The total character is: ', len(str1))

# Count Method

substring = 'awesome'
print(substring, 'present ', str1.count(substring), 'times.')

substring2 = 'i'

print(str1.count(substring2,8,20))

#string.count(substring)----Return total count
#string.count(substring, start, and end)--- Return total count between start and end
