

# a = {'id': 36262,'title': 'Платье', 'price': 2000, 'description': 'красивое платье', 'created_at': '23.08.22'}

import shelve
from datetime import datetime

from settings import FILENAME


""" 
db = {
    '45372': {
        'title': 'Apple Iphone 13',
        'price': 98000,
        'description': 'Very good phone',
        'created_at': '23.08.22 18:54'
    }
} 
"""

def create():
    id_ = datetime.now().strftime('%H%M%S')
    title = input('Введите название товара ')
    price = int(input('Введите цену товара '))
    description = input('Введите описание ')
    created_at = datetime.now().strftime('%d.%m.%y %H:%M')
    with shelve.open(FILENAME) as db:
        db[id_] = {
            'title': title,
            'price': price,
            'description': description,
            'created_at': created_at
        }


def get_all_data():
    with shelve.open(FILENAME) as db:
        for key, value in db.items():
            print('-----------------------------')
            print('id:', key, '|', 'title:', value['title'], '|', 'price:', value['price'])
            print('-----------------------------')


def get_data_by_id():
    id_ = input('Введите id товара ')
    with shelve.open(FILENAME) as db:
        try:
            prod = db[id_]
            print(
                f"""  
                Название: {prod['title']}
                Цена: {prod['price']}
                Описание: {prod['description']}
                Время создания: {prod['created_at']}
                """
            )
        except KeyError:
            print(f'{id_} не существует')



def update_data():
    id_ = input('Введите id товара: ')
    with shelve.open(FILENAME, writeback=True) as db:
        try:
            prod = db[id_]
            prod['title'] = input('Введите новое название ') or prod['title']
            prod['price'] = int(input('Введите новую цену ')) or prod['price']
            prod['description'] = input('Введите новое описание ') or prod['description']
        except KeyError:
            print(f'{id_} не существует')


def delete_data():
    id_ = input('Введите id товара ')
    with shelve.open(FILENAME) as db:
        try:
            db.pop(id_)
        except KeyError:
            print(f'{id_} не существует')


get_all_data()
