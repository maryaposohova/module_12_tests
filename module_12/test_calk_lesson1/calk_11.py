# import logging

#
# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b
#
# def mul(a, b):
#     return a * b
#
# # def div(a, b):
# #     return a / b
#
# def div(a, b):
#     try:
#         logging.info(f'Succesful divide {a} / {b}')
#         return a / b
#     except ZeroDivisionError as err:
#         logging.error('Na nol ne deli!!!', exc_info=True)
#         return 0
#
# # новые ф-цц другого сотрудника, для них он создал новые тесты test_new_calc
# def sqrt(a):
#     return a**0.5
#
#
# def pow(a, b):
#     return a**b
#
#
# # def add(a, b):
# #     return a**2 + b**2
#
# if __name__ == '__main__':
#     # print(add(100, 2))
#     # print(sub(100, 2))
#     # print(mul(100, 2))
#     # print(div(100, 2))
#     # logging.debug('gf')
#     # logging.info('f')
#     # logging.warning('f')
#     # logging.error('f')
#     # logging.critical('a')
#     logging.basicConfig(level=logging.INFO, filemode= 'w', filename= 'py.log',
#                         format= '%(asctime)s | %(levelname)s | %(message)s')
#     print(div(3, 4))
#     print(div(3, 0))


#  правильное расположение
import logging, sys


def div(a, b):
    try:
        logging.info(f'Successful divide {a} / {b}')
        return a / b
    except ZeroDivisionError as err:
        logging.error('Na nol ne deli!!!', exc_info=True)
        return 0


if __name__ == '__main__':  # если нужно не перезаписывать, а дозаписывать, писать в filemode= не 'w', а 'a'
    logging.basicConfig(
        level=logging.INFO,
        filemode='w',
        filename='py.log',
        format='%(asctime)s | %(levelname)s | %(message)s'
    )

    print(div(3, 4))
    print(div(3, 0))

''' 
Если вы хотите видеть логи и в консоли, добавьте stream=sys.stdout в basicConfig.

Для более сложного логирования рассмотрите использование FileHandler и StreamHandler вместо basicConfig.
'''