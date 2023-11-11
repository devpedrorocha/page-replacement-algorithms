import time

from algorithms.lru.least_recently_used import least_recently_used

pages_list = [0, 1, 2, 3, 4, 5, 0, 2, 3, 6, 7, 8]
pages_number = 5

def run_lru():
    print()
    print("LRU - Least Recently Used")
    start_time = time.perf_counter()
    page_faults = least_recently_used(pages_list, pages_number)
    print(f"Tempo de execução: {(time.perf_counter() - start_time):.14f} seconds")
    print(f"Total de faltas de página: {page_faults}")

def main():
    print('-- SIMULANDO ALGORITMOS DE SUBSTITUIÇÃO DE PÁGINAS --')
    run_lru()

if __name__ == "__main__":
    main()