import numpy as np

def random_predict(number:int=1) -> int:
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return (count)

def score_game(random_predict) -> int:
    count_is = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_is.append(random_predict(number))
        
    score = int(np.mean(count_is))
    
    print(f'Your algo find the number for: {score} efforts')
    return(score)

score_game(random_predict)
 