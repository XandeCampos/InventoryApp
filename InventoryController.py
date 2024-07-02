from Item import Item

class Controller:
    def __init__(self):
        self._itemsList:list[Item] = []
    
    def __hasItem(self, item:Item):
        return item in self._itemsList
    
    def __hasOwner(self, owner:str):
        for i in self._itemsList:
            if i.getOwner() == owner: return True
        
        return False
                
    def addItem(self, item:Item):
        self._itemsList.append(item)
    
    def getItem(self, item:Item):
        if self.__hasItem(item):
            for i in self._itemsList:
                if i.getName() == item.getName():
                    return i
            
    def printInventory(self):
        for i in self._itemsList:
            print(i.toString())
    
    def printByOwner(self, owner:str):
        if not self.__hasOwner(owner):
            print("There are no items with that owner in the system")
        else:
            for i in self._itemsList:
                if i.getOwner() == owner:
                    print(i.toString())
    
    
            