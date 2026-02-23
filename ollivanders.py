class Ollivanders():

    def __init__(self,items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()

    def get_items(self):
        return self.items


class Item():
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        item = f"{self.name} {self.sell_in} {self.quality}"
        return item

    
class Interfaz():

    def update_quality():
        pass





if __name__ == '__main__':

    def test_Ollivanders_get_items():
        inventario = Ollivanders(['anillos', 'mazo', 'espada']) 
        items = inventario.get_items() 
        assert items == ['anillos', 'mazo', 'espada']

    def test_Item_print():
        item = Item("anillo", 30, 50)
        assert repr(item) == "anillo 30 50"