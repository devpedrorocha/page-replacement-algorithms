

class Queue:
    def __init__(self, max_size = 64):
        self.__items = []
        self.max_size = max_size

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0)

    def get_items(self):
        return self.__items

    def size(self):
        return len(self.__items)

    def is_empty(self):
        return len(self.__items) == 0

    def is_full(self):
        return len(self.__items) == self.max_size
