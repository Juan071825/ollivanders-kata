class Ollivanders():

    def __init__(self,items):
        self.items = items

    def update_inventory_quality(self):
        for item in self.items:
            item.update_quality()

    def get_items(self):
        return self.items


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    
class NormalItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
        

    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in >= 0:
            self.quality -= 1
        else:
            self.quality -= 2
        return [self.name, self.sell_in, self.quality]

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Interfaz():

    def update_quality(self):
        pass



if __name__ == '__main__':

    def test_Ollivanders_get_items():
        inventory = Ollivanders(['anillo', 'mazo', 'copa'])
        assert inventory.get_items() == ['anillo', 'mazo', 'copa']
        assert inventory.get_items() != ['anillo', 'maza', 'copa']        
        print("Ollivanders().get_items funciona")

    test_Ollivanders_get_items()


    def test_NormalItem_update_quality():
        normal_item = NormalItem('Elixir of the Mongoose', 5, 7)
        assert normal_item.update_quality() == ['Elixir of the Mongoose', 4, 6]
        print('NormalItem().update_quality() funciona')

    test_NormalItem_update_quality()