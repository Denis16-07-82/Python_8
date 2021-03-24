#  Написать функцию email_parse(<email_address>), которая
#  при помощи регулярного выражения извлекает имя пользователя
#  и почтовый домен из email адреса и возвращает их в виде словаря.
#  Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь
#  учесть их в регулярном выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
import re

RE_NAME = re.compile(r'(\w+)@(\w+)\.\w+')


def email_parse(email_address):
    my_dict=dict()
    if RE_NAME.findall(email_address):
        new_tuple=RE_NAME.findall(email_address)[0]
        my_dict[new_tuple[0]]=new_tuple[1]
        print(my_dict)
    else:raise ValueError


if __name__ == '__main__':
    email_address = input('Введите ваш email адрес: ')
    try:
        email_parse(email_address)
    except ValueError :
        print(f'{ValueError}:wrong email:{email_address}')