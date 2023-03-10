while True:
    try:
        round = int(input('Enter Round : '))
        if round > 0:
            break
        else:
            raise ValueError
    except ValueError:
        print('Error Sorry Enter Round Number again pls!!')
        
while True: 
    try:
        point = int(input('Enter Point : '))
        if point > 0:
            break
        else:
            raise ValueError
    except ValueError:
        print('Error Sorry pls Enter Point Number again pls!!')

for i in range (round):
    if ((i+1) % point) == 0:
        print('Buzz')
    else:
        print('Fit')
        