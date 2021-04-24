s=input('Enter:')
temp=''
for i in s:
    temp=i+temp
if temp==s:
    print('Palindrome')
else:
    print('No')