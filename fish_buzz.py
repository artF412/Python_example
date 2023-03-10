try:
    number = int(input('Enter Number : '))
    for i in range (number):
        if ((i+1) % 5) == 0:
            print('Buzz')
        else:
            print('Fit')
except ValueError:
    print('Error Sorry pls Enter Number!!')
        