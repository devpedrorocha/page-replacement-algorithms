

# I need to make a class for implement the second chance algorithm


class SecondChance:
    def __init__(self):
        self.__items = []
        self.second_chance = {}

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

    def send_to_end(self):
        firstPage = self.__items[0]
        firstPage['referenced'] = False

        self.dequeue()
        self.__items.enqueue(firstPage)

    @property
    def size(self) -> int:
        return len(self.____items)

    @property
    def is_empty(self) -> bool:
        return self.currentSize == 0

    @property
    def is_full(self) -> bool:
        return self.currentSize == 1024
