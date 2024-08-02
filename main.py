from store import Store

# Создание магазинов
store1 = Store("Магазин 1", "ул. Пушкина, д. 1")
store2 = Store("Магазин 2", "ул. Лермонтова, д. 2")
store3 = Store("Магазин 3", "ул. Чехова, д. 3")

# Добавление товаров в магазины
store1.add_item("яблоки", 140)
store1.add_item("бананы", 95)

store2.add_item("апельсины", 150)
store2.add_item("яблоки", 145)  # Добавляем яблоки в другой магазин

store3.add_item("виноград", 180)
store3.add_item("киви", 170)


# Запрос цены товара через консоль и вывод магазинов
def get_price_from_console():
    item_name = input("Введите название товара: ")
    price_info = Store.find_item(item_name)
    if price_info:
        for store_name, price in price_info:
            print(f"Цена на {item_name} в {store_name}: {price}")
    else:
        print(f"Товар '{item_name}' не найден в ассортименте.")


get_price_from_console()

# Тестирование методов для магазина 1
print("\nТестирование методов для магазина 1:")

# Добавление товара
store1.add_item("груши", 160)
print("\nПосле добавления груши:", store1)

# Обновление цены товара
store1.update_price("яблоки", 145)
print("\nПосле обновления цены на яблоки:", store1)

# Удаление товара
store1.remove_item("бананы")
print("\nПосле удаления бананов:", store1)

# Запрос цены имеющегося товара
price = store1.get_price("яблоки")
print("\nЦена на яблоки:", price)

# Запрос цены товара, которого нет в ассортименте
price = store1.get_price("бананы")
print("Цена на бананы:", price)
