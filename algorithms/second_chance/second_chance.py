from algorithms.second_chance.second_chance_queue import SecondChanceQueue

def second_chance(referenced_pages, max_size):

       faults = 0
       queue = SecondChanceQueue(max_size)

       for page in referenced_pages:
              found = False
              for object in queue.get_items():
                     if object['page'] == page:
                            queue.references_page(page)
                            found = True
              if not found:
                     if queue.is_empty() or (not queue.is_full()):
                            queue.enqueue({'page': page, 'referenced': True})
                            faults += 1
                     else:
                            queue.second_chance(page)
                            faults += 1

       return faults

