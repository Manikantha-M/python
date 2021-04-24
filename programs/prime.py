n=int(input('Enter:'))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print('No')
            break
    else:
        print('Prime')
else:
    print('No')