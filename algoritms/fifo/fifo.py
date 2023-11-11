from typing import List
from algoritms.fifo.queue import Queue


def fifo(referenced_pages: List):

    faults = 0
    q = Queue()

    for page in referenced_pages:
        if page not in q.get_items():
            if (not q.is_full()) or q.is_empty():
                q.enqueue(page)
            else:
                q.dequeue()
                q.enqueue(page)

            faults += 1
    return faults
