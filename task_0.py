#Створення замовлення в кафе.
class MenuItem:
    def init(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
    def str(self):
        return f"{self.name}: {self.description} ({self.price} грн.)"


class Menu:
    def init(self):
        self.menu_items = []
    def add_item(self, menu_item):
        self.menu_items.append(menu_item)
    def remove_item(self, menu_item):
        self.menu_items.remove(menu_item)
    def print_menu(self):
        print("Меню:")
        for item in self.menu_items:
            print(item)
    def get_menu_item_by_name(self, name):
        for item in self.menu_items:
            if item.name == name:
                return item
        return None

class Order:
    def init(self):
        self.items = []
        self.total_price = 0
    def add_item(self, item):
        self.items.append(item)
        self.total_price += item.price
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.total_price -= item.price
    def print_order(self):
        print("Замовлення:")
        for item in self.items:
            print(f"{item.name} - {item.price} грн.")
        print(f"Усього: {self.total_price} грн.")

def main():
    menu = Menu()# Створення меню

    # Додавання блюд в меню:
    menu.add_item(MenuItem("Паста", "Спагетті с м'ясним соусом", 350))
    menu.add_item(MenuItem("Салат", "Салат з овочів з куркою", 250))
    menu.add_item(MenuItem("Суп", "Борщ зі сметаною", 200))
    menu.add_item(MenuItem("Десерт", "Тирамісу", 150))

    order = Order()# Створення замовлення

    # Виведення меню та отримання замовлення від користувача:
    while True:
        menu.print_menu()
        item_name = input("Що би Ви хотіли замовити? ")
        item = menu.get_menu_item_by_name(item_name)
        if item is None:
            print("Вибачте, цього блюда нема в меню.")
        else:
            order.add_item(item)
            print(f"{item.name} додано в замовленняя.")
            more = input("Хочете замовити щось ще?")
            if more.lower() != "так":
                break

    order.print_order()#Виведення замовлення

if name == 'main':
    main()
