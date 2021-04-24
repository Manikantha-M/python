def bmicalc(w,h):
    bmi=w/(h**2)
    if bmi<18:
        print('underweight')
    elif bmi>=18 and bmi<=25:
        print('normal')
    else:
        print('overweight')

bmicalc(60,1.78)
bmicalc(40,1.8)
bmicalc(80,1.6)