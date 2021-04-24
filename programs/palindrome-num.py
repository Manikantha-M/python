n=int(input('Enter:'))
temp=n
rev=0
while temp>0:
    dig=temp%10
    rev=rev*10+dig
    temp//=10
if rev==n:
    print('Palindrome')
else:
    print('No')