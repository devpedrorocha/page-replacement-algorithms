from algorithms.nru.nru_queue import NruQueue


def not_recently_used(input_pages, max_size=64):

    print('entrou na função')

    periodicly_clear = 5
    faults = 0
    table = NruQueue(max_size)

    for page in input_pages:
        found = False
        for object in table.get_items():
            if object['page'] == page:
                found = True
                object["R"] = True

        if not found:
            table.notInTable(page)
            faults += 1

        periodicly_clear -= 1

        if periodicly_clear == 0:
            for pageObject in table.get_items():
                pageObject['R'] = False

            periodicly_clear = 5
    
    return faults

