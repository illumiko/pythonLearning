import csv
class Item:
    # acts as global variable and if there is a same varibale at instance level then that
    # gets cstocked first
    payRate = 0.8
    stock = []
    def __init__(self,name:str,price:int,quantity=0):
       # sets rules for value
       assert price >= 0 ,"value should {price} >= 0"
       assert quantity >= 0 ,"value should {quantity} >= 0"
       self._name = name 
       self._price = price
       self._quantity = quantity
       Item.stock.append(self)
       # to set the __repr__ val 
       self.string = f"\nitem:'{self.__class__.__name__}'\nName:'{self.name}'\nPrice:'${self.price}'\nQuantity:'{self.quantity}'\n"
       # print(self.string)
    # sets a way of expressing instantied class values
    def __repr__(self) -> str:
        return self.string
    ##Geters
    @property
    def name(self):
        return self._name
    def price(self):
        return self._price
    def quantity(self):
        return self._quantity
    def calcTotalPrice(self):
        return self.price * self.quantity * self.payRate
    def netPrice(self):
        self.price*self.payRate
    #class methods
    @classmethod
    def instantiateFromCsv(cls):
        with open('stock.csv', 'r') as f:
            reader = csv.DictReader(f)
            for x in reader:
                Item(name=x['itemName'],price=int(x['price']),quantity=int(x['quantity']))
# inheritance
class Phone(Item):
    def __init__(self, name: str, price: int, quantity=0, referbished=0):
        super().__init__(name, price, quantity)
        self._referbished = referbished
        self.string += f"referbished:'{self.referbished}'\n"
    #getters
    @property
    def referbishedItems(self):
       return self._referbished       
samsuck = Phone('Jsh*t', 50, 10, 20)
lgCock = Phone('jGcuck*t', 20, 100, 10)
print(Item.stock)
