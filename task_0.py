def validate_menu_item(item):
    if not isinstance(item, MenuItem):
        raise TypeError('Некорректный тип аргумента')


class MenuItem:
    def __init__(self, name, description, price):
        if not isinstance(name, str) or not isinstance(description, str) or not isinstance(price, int):
            raise TypeError('Некорректный тип аргументов')
        if not name or not description or price < 0:
            raise ValueError('Аргументы должны быть не пустыми и цена не меньше 0')
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f'{self.name}: {self.description} ({self.price} грн.)'


class Menu:
    def __init__(self):
        self.menu_items = []

    def add_item(self, menu_item):
        self.menu_items.append(menu_item)

    def remove_item(self, menu_item):
        self.menu_items.remove(menu_item)

    def modify_menu(self, menu_item, operation='add'):
        if not isinstance(menu_item, MenuItem):
            raise TypeError('menu_item должен быть экземпляром класса MenuItem')

        if operation not in ['add', 'remove']:
            raise ValueError("Операция может быть только 'add' или 'remove'")

        if operation == 'add':
            self.add_item(menu_item)
        elif operation == 'remove':
            self.remove_item(menu_item)

    def print_menu(self):
        print('Меню:')
        for item in self.menu_items:
            print(item)

    def get_menu_item(self, name):
        for item in self.menu_items:
            if item.name == name:
                return item
        return None


class Order:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_item(self, item):
        validate_menu_item(item)
        self.items.append(item)
        self.total_price += item.price

    def remove_item(self, item):
        validate_menu_item(item)
        if item in self.items:
            self.items.remove(item)
            self.total_price -= item.price

    def print_order(self):
        print('Замовлення:')
        for item in self.items:
            print(f'{item.name} - {item.price} грн.')
        print(f'Усього: {self.total_price} грн.')


def main():
    menu = Menu()  # Створення меню
    # Додавання блюд в меню:
    menu_items = [('Паста', "Спагетті с м'ясним соусом", 350), ('Салат', 'Салат з овочів з куркою', 250),
                  ('Суп', 'Борщ зі сметаною', 200), ('Десерт', 'Тирамісу', 150)]
    for name, description, price in menu_items:
        menu.modify_menu(MenuItem(name, description, price))

    order = Order()  # Створення замовлення
    # Виведення меню та отримання замовлення від користувача:
    while True:
        menu.print_menu()
        item_name = input('Що би Ви хотіли замовити? ')
        item = menu.get_menu_item(item_name)
        if item is None:
            print('Вибачте, цього блюда нема в меню.')
        else:
            order.add_item(item)
            print(f'{item.name} додано в замовлення.')
        more = input('Хочете замовити щось ще? (так/ні) ')
        if more.lower() != 'так':
            break
    order.print_order()  # Виведення замовлення


if __name__ == '__main__':
    main()
