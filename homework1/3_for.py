"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

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
    school = {
        'total_scores':   0,
        'total_students': 0,
        'average_scores': 0,
    }
    for record in scores_structure:
        school_class = {
            'total_scores':   0,
            'total_students': 0,
            'average_scores': 0,
        }
        for score in record['scores']:
            school['total_scores']   += score
            school['total_students'] += 1
            school_class['total_scores']   += score
            school_class['total_students'] += 1
            school_class['average_scores'] = \
                school_class['total_scores'] / school_class['total_students']
        print(
            'Средний бал по классу ' + record['school_class'] + ' ' + \
                str(school_class['average_scores'])
        )
    if school['total_students'] > 0:
        school['average_scores'] = \
            school['total_scores'] / school['total_students']
    print(
        'Средний бал по школе ' + str(school['average_scores'])
    )

if __name__ == "__main__":
    main()
