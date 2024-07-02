class Item:
    def __init__ (self, name:str, owner:str, quantity:int, localUsed:str):
        self._name = name
        self._owner = owner
        self._quantity = quantity
        self._localsSet = {localUsed}

    def getName(self):
        return self._name
    
    def getOwner(self):
        return self._owner
    
    def getQuantity(self):
        return self._quantity
    
    def getLocalsUsed(self):
        return list(self._localsSet)
    
    def hasLocal(self, local:str):
        return local in self._localsSet
            
    def addLocal(self, local:str):
        self.localsSet.add(local)
        
    def updateQuantity(self, adition:int):
        self.quantity += 1
        
    def toString(self):
        print("\nItem: {:<20} Owner: {:<20} Quantity: {:<10} Local Used: {:<20}".format(self.name, self.owner, self.quantity, str(self.localsSet)))
    