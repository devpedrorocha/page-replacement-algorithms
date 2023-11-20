
import random

class NruQueue:
    def __init__(self, max_size):
        self.items = []
        self.classes = {} 
        self.max_size = max_size

        for i in range(0, 4):
            self.classes[f"class-{i}"] = []

    def include(self, page: str):
        self.items.append({'page': page,"R": True, "M": random.choice([False, True])}) 
    
    def get_items(self):
        return self.items
    
    def clearLowestClassses(self):
        for p in self.items:
            referenced = p['R']
            modified = p['M']
            if not referenced and not modified:
                self.classes["class-0"].append(p)
            elif not referenced and modified:
                self.classes["class-1"].append(p)
            elif referenced and not modified:
                self.classes["class-2"].append(p)
            else:
                self.classes["class-3"].append(p)

        
        if len(self.classes["class-0"]) > 0:
            page_to_be_removed = random.choice(self.classes["class-0"])
        elif len(self.classes["class-1"]) != 0:
            page_to_be_removed = random.choice(self.classes["class-1"])
        elif len(self.classes["class-2"]) != 0:
            page_to_be_removed = random.choice(self.classes["class-2"])
        elif len(self.classes["class-3"]) != 0:
            page_to_be_removed = random.choice(self.classes["class-3"])
        
        
        for item in self.items:
            if item['page'] == page_to_be_removed['page']:
                self.items.remove(item)

    
    def notInTable(self, page: str):
        
        if len(self.items) == 0 or len(self.items) < self.max_size:
            self.include(page)
   
        elif len(self.items) == self.max_size:
            self.clearLowestClassses()
            self.include(page)
            