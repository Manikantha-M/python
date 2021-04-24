import string
s=input('Enter:')
s=s.lower()
s=s.replace(' ','')
s=s.translate(str.maketrans('','',string.punctuation))
if s==s[::-1]:
    print('Palindrome')
else:
    print('No')