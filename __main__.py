import random
import time

from algorithms.lru.least_recently_used import least_recently_used
from algorithms.fifo.fifo import fifo
from algorithms.second_chance.second_chance import second_chance
from algorithms.nru.not_recently_used import not_recently_used


import array


def run_lru(pages_list, pages_number):
    print()
    print("LRU - Least Recently Used")
    start_time = time.perf_counter()
    page_faults = least_recently_used(pages_list, pages_number)
    print(f"Tempo de execução: {(time.perf_counter() - start_time):.14f} seconds")
    print(f"Total de faltas de página: {page_faults}")


def run_fifo(pages_list, pages_number):
    print()
    print("FIFO - First In First Out")
    start_time = time.perf_counter()
    page_faults = fifo(pages_list, pages_number)
    print(f"Tempo de execução: {(time.perf_counter() - start_time):.14f} seconds")
    print(f"Total de faltas de página: {page_faults}")

def run_second_chance(pages_list, pages_number):
    print()
    print("Second Chance")
    start_time = time.perf_counter()
    page_faults = second_chance(pages_list, pages_number)
    print(f"Tempo de execução: {(time.perf_counter() - start_time):.14f} seconds")
    print(f"Total de faltas de página: {page_faults}")

def run_nru(pages_list, pages_number):
    print()
    print("Not Recently Used Algorithm")
    start_time = time.perf_counter()
    page_faults = not_recently_used(pages_list, pages_number)
    print(f"Tempo de execução: {(time.perf_counter() - start_time):.14f} seconds")
    print(f"Total de faltas de página: {page_faults}")

def main():
    print('-- SIMULANDO ALGORITMOS DE SUBSTITUIÇÃO DE PÁGINAS --')

    # Código para gerar um array com número aleatórios

    random_numbers = [random.randint(1, 256) for _ in range(200000)]

    numbers_array = array.array('I', random_numbers)

    with open('muitos_numeros_aleatorios.bin', 'wb') as file:
        numbers_array.tofile(file)
    
    numbers_from_file = []

    with open('muitos_numeros_aleatorios.bin', 'rb') as file:
        numbers_from_file = array.array('I')
        numbers_from_file.fromfile(file, 50000)

    run_fifo(numbers_from_file, 32)
    run_second_chance(numbers_from_file, 32)
    run_lru(numbers_from_file, 32)
    run_nru(numbers_from_file, 32)
    

if __name__ == "__main__":
    main()
