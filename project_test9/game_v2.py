"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = 50 # первое предполагаемое число
    predict_number_min = 0 #минимальная граница поиска
    predict_number_max = 101 #максимальная граница поиска

    while True:
        count += 1
        if number < predict_number: # если загаданное число меньше предполагаемого
            predict_number_max = predict_number
            predict_number = (predict_number_max - predict_number_min) // 2 + predict_number_min # сокращаем границы поиска пополам
        if number > predict_number: # если загаданное число больше предполагаемого
            predict_number_min = predict_number
            predict_number = (predict_number_max - predict_number_min) // 2 + predict_number_min # сокращаем границы поиска пополам
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
