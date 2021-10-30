import numpy as np

number = np.random.randint(1, 101) #загадываем число
count = 0

while True:
    count += 1
    predict_number = int(input('Guess the number from 1 to 100: '))

    if predict_number > number:
        print('The number must be lower')
    
    elif predict_number < number:
        print('The number must be larger')

    else:
        print(f"You are right! The number is {number}, for {count} counts")
        break
