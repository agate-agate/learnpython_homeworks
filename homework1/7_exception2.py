"""

Домашнее задание №1

Исключения: приведение типов

* Напишите функцию get_summ(num_one, num_two), которая принимает
  на вход два целых числа (int), складывает их и возвращает результат
  сложения
* Оба аргумента нужно приводить к целому числу при помощи int() и
  перехватывать исключение ValueError если приведение типов не сработало

"""

def get_summ(num_one, num_two):
    """
    Замените pass на ваш код
    """

    def to_int(num):
        try:
            num = int(num)
        except ValueError:
            num = 0;
        return num

    num_one = to_int(num_one);
    num_two = to_int(num_two);
    return num_one + num_two

if __name__ == "__main__":
    print(get_summ(2, 2))
    print(get_summ(3, "3"))
    print(get_summ("4", "4"))
    print(get_summ("five", 5))
    print(get_summ("six", "шесть"))
