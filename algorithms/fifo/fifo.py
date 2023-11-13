from typing import List
from algorithms.fifo.queue import Queue


def fifo(referenced_pages: List, number_of_pages: int = 64):

    faults = 0
    q = Queue(number_of_pages)

    for page in referenced_pages:
        if page not in q.get_items():
            if (not q.is_full()) or q.is_empty():
                q.enqueue(page)
            else:
                q.dequeue()
                q.enqueue(page)

            faults += 1
    return faults
