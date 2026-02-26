class Ollivanders():

    def __init__(self,items):
        self.items = items

    def update_inventory(self):
        for item in self.items:
            item.update_quality()

    def get_inventory(self):
        return self.items


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"
    

#class Interfaz():
#   def update_quality(self):
#       pass


class NormalItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def setSell_in(self):
        self.sell_in -= 1

    def setQuality(self, valor):
        if self.quality + valor in range(0,51):
            self.quality += valor
        elif self.quality + valor > 50:
            self.quality = 50
        else:
            self.quality = 0


    def update_quality(self):
        if self.sell_in >= 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.setSell_in()
        
    
class ConjuredItem(NormalItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.sell_in >= 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)
        self.setSell_in()


class AgedBrie(NormalItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        self.setSell_in()

    
class Sulfuras(NormalItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        self.quality = 80
        self.setSell_in()



class Backstage(NormalItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.sell_in > 10:
            self.setQuality(1)
        
        elif self.sell_in > 5:
            self.setQuality(2)

        elif self.sell_in > 0:
            self.setQuality(3)

        else:
            self.quality = 0
        self.setSell_in


        





if __name__ == '__main__':

    #def test_Ollivanders_get_items():
    #    inventory = Ollivanders(['anillo', 'mazo', 'copa'])
    #    assert inventory.get_inventory() == ['anillo', 'mazo', 'copa']
    #    assert inventory.get_inventory() != ['anillo', 'maza', 'copa']        
    #    print("Ollivanders().get_items funciona")

    #test_Ollivanders_get_items()


    def test_NormalItem_update_quality():
        normal_item = NormalItem('Elixir of the Mongoose', 5, 7)
        assert normal_item.update_quality() == ['Elixir of the Mongoose', 4, 6]
        print('NormalItem().update_quality() funciona')

    test_NormalItem_update_quality()