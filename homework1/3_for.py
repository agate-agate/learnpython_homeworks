"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def get_average_for_list_of_scores(list_of_scores):

    length = len(list_of_scores)
    if not (length > 0):
        return 0

    total_score = sum(list_of_scores)

    return total_score / length

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    scores_structure = [
        {'school_class': '4a', 'scores': [3,4,4,5,2,]},
        {'school_class': '2b', 'scores': [3,5,7,]},
        {'school_class': '7b', 'scores': [4,5,]},
    ]
    school_scores = []
    for record in scores_structure:

        school_class_label  = record['school_class']
        school_class_scores = record['scores']
        school_scores += school_class_scores

        average_score = get_average_for_list_of_scores(school_class_scores)
        print(f'Средний бал по классу {school_class_label}: {average_score}')

    average_score = get_average_for_list_of_scores(school_scores)
    print(f'Средний бал по школе: {average_score}')

if __name__ == "__main__":
    main()
