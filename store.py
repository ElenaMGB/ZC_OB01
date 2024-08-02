class Store:
    all_stores = []  # Список всех магазинов для отслеживания

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}
        Store.all_stores.append(self)  # Добавляем магазин в общий список

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def __repr__(self):
        return f"Store(name='{self.name}', address='{self.address}', items={self.items})"

    @classmethod
    def find_item(cls, item_name):
        stores_with_item = []
        for store in cls.all_stores:
            if item_name in store.items:
                stores_with_item.append((store.name, store.items[item_name]))
        return stores_with_item
