def get_cook_book_from_file():  #   data.txt

    with open('data.txt', 'rt', encoding='utf8') as f:
        cook_book = {}
        while True:
            name_dish = f.readline().strip()
            if not name_dish:
                break
            count_ingridient = f.readline().strip()
            dish = []

            for i in range(int(count_ingridient)):
                dish_list = (f.readline().strip().split('|'))
                dish.append({'ingridient_name': dish_list[0], 'quantity': int(dish_list[1]), 'measure': dish_list[2]})
            cook_book[name_dish] = dish
            f.readline()

    return cook_book



def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}

    for dish in dishes:

        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count

            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item

            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']

    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list():
    cook_book = get_cook_book_from_file()
    print('\n---МЕНЮ---')
    for dish in enumerate(cook_book, 1):
        print(dish)
    person_count = int(input('\n Введите количество человек: '))
    dishes = input('Введите блюда из меню в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print_shop_list(shop_list)

create_shop_list()
