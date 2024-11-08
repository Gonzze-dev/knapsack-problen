class Item(object):
    def __init__(self, id, weight, profit):
        self.id = id
        self.weight = weight
        self.profit = profit
        self.profitPerWeight = profit / weight
        
    def __str__(self):
        return f"ID: {self.id}, weight: {self.weight}, profit: {self.profit}, profitXWeigth: {self.profitPerWeight} "
    
    def __lt__(self, other):
        if isinstance(other, Item):
            return self.profitPerWeight > other.profitPerWeight
        
        return NotImplemented
    
