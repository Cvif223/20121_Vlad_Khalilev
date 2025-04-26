from typing import Union
import sys

class ShopItem:

    def __init__(self, name: str, weight: Union[int, float], price: Union[int, float]):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name.lower(), self.price, self.weight))

    def __eq__(self, other):
        if self.name == other.name and self.weight == other.weight and self.price == other.price:
            return True
        return False


def create_shop_item(lst: list):
    shp_itm = dict()
    for i in lst:
        name, b = i.split(":")
        weight, price = b[1:].split(" ")

        shp_itm[ShopItem(name, float(weight), float(price))] = [ShopItem(name, float(weight), float(price)), len([x.split(":")[0] for x in lst if x.split(":")[0] == name])]
    return shp_itm

if __name__ == "__main__":

    lst_in = ['Системный блок: 1500 75890.56', 'Монитор Samsung: 2000 34000', 'Клавиатура: 200.44 545', 'Монитор Samsung: 2000 34000']

    shop_items = create_shop_item(lst_in)
    it1 = ShopItem('name', 10, 11)
    it2 = ShopItem('name', 10, 11)
    assert hash(it1) == hash(it2), "разные хеши у равных объектов"
    it2 = ShopItem('name', 10, 12)
    assert hash(it1) != hash(it2), "равные хеши у разных объектов"
    it2 = ShopItem('name', 11, 11)
    assert hash(it1) != hash(it2), "равные хеши у разных объектов"
    it2 = ShopItem('NAME', 10, 11)
    assert hash(it1) == hash(it2), "разные хеши у равных объектов"
    name = lst_in[0].split(':')
    #for sp in shop_items.values():
    #тут было сравнение на int    assert isinstance(sp[0], ShopItem) and type(sp[1]) == float, "в значениях словаря shop_items первый элемент должен быть объектом класса ShopItem, а второй - целым числом"
    v = list(shop_items.values())
    if v[0][0].name.strip() == "Системный блок":
        assert v[0][1] == 1 and v[1][1] == 2 and v[2][1] == 1 and len(v) == 3, "неверные значения в словаре shop_items"
    if v[0][0].name.strip() == "X-box":
        assert v[0][1] == 2 and v[1][1] == 1 and v[2][1] == 2 and len(v) == 3, "неверные значения в словаре shop_items"