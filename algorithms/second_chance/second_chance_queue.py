

class SecondChanceQueue:
    def __init__(self, max_size = 64):
        self.__items = []
        self.max_size = max_size

    def enqueue(self, item: dict):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0)

    def get_items(self):
        return self.__items

    def second_chance(self, page_referenced):
        while True:
            if self.is_first_page_referenced():
                self.send_to_end()
            else:
                self.dequeue
                self.enqueue({'page': page_referenced, 'referenced': True})
                return False

    def is_first_page_referenced(self):
        return self.__items[0]['referenced']

    def references_page(self, page_not_referenced):
        for object in self.__items:
            if page_not_referenced == object['page']:
                object['referenced'] = True


    def send_to_end(self):
        firstPage = self.__items[0]
        firstPage['referenced'] = False

        self.dequeue()
        self.enqueue(firstPage)

    def size(self) -> int:
        return len(self.__items)
  
    def is_empty(self) -> bool:
        return len(self.__items) == 0

    def is_full(self) -> bool:
        return self.size() == self.max_size
