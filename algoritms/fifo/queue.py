

class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0)

    @property
    def get_items(self):
        return self.__items

    @property
    def size(self):
        return len(self.__items)

    @property
    def is_empty(self):
        return len(self.__items) == 0

    @property
    def is_full(self):
        return len(self.__items) == 1024
