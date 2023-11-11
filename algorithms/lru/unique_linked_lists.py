class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class UniqueLinkedList:
    def __init__(self, max_count):
        self.head = None
        self.tail = None
        self.count = 0
        self.max_count = max_count

    def insert(self, data):
        new_node = Node(data)

        # Se a lista estiver vazia, insira o novo nó como a cabeça e a cauda
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.count += 1
            return 1

        # Procure pelo nó com os mesmos dados
        current = self.head
        while current and current.data != data:
            current = current.next

        # Se o nó com os mesmos dados for encontrado, mova-o para o início
        if current:
            if current == self.head:
                # Caso especial: o nó a ser movido já está no início
                return 0

            if current == self.tail:
                # Atualize a cauda para o nó anterior
                self.tail = current.prev
                self.tail.next = None
            else:
                # Remova o nó de sua posição atual
                current.prev.next = current.next
                current.next.prev = current.prev

            # Mova o nó para o início
            current.next = self.head
            self.head.prev = current
            current.prev = None
            self.head = current
            return 0
        else:
            # Insira o novo nó no início
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.count += 1

            # Verifique se a lista atingiu sua capacidade máxima
            if self.count > self.max_count:
                # Remova o último elemento
                self.tail = self.tail.prev
                self.tail.next = None
                self.count -= 1

            return 1

    def __str__(self):
        # Retorna uma representação de string da lista
        if self.head is None:
            return ''

        string = f'{self.head.data}'
        current = self.head.next
        while current:
            string = f'{string},{current.data}'
            current = current.next

        return string
