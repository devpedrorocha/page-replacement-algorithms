from algorithms.lru.unique_linked_lists import UniqueLinkedList


def least_recently_used(data: list, n_pages: int = 64):
    linked_list = UniqueLinkedList(n_pages)
    page_faults = 0
    for i in data:
        was_inserted = linked_list.insert(i)

        if was_inserted:
            page_faults += 1

    return page_faults

if __name__ == "__main__":
    print(least_recently_used([0, 1, 2, 3, 4, 5, 0, 2, 3, 6, 7, 8], 5))
    print(least_recently_used([1, 2, 3, 4, 4, 4, 5, 6, 3], 5))
