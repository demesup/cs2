class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


class CircularBuffer:
    def __init__(self, size=1):
        self.size = size
        self.length = 0
        self.head = None
        self.tail = None

    def add(self, e):
        if self.is_full():
            return False

        node = Node(e)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1
        return True

    def take(self):
        if self.is_empty():
            return None

        to_return = self.head
        self.head = to_return.next
        self.length -= 1
        return to_return

    def is_full(self):
        return self.size == self.length

    def is_empty(self):
        return self.length == 0

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.cargo))
            current = current.next

        return f"[{', '.join(result)}]"


buffer = CircularBuffer(3)
print(buffer)

buffer.add(1)
print(f"Added 1: {buffer}")
buffer.add(2)
print(f"Added 2: {buffer}")
buffer.add(3)
print(f"Added 3: {buffer}")

print(f"Is full? {buffer.is_full()}\n")
print(buffer.take())  
print(f"Taken: {buffer}")
print(buffer.take())
print(f"Taken: {buffer}")

buffer.add('A')
print(f"Added A: {buffer}")

buffer.add('B')
buffer.add('C')
print(f"After trying to add B C {buffer}\n")
print(buffer.take())
print(f"Taken: {buffer}")
print(buffer.take())
print(f"Taken: {buffer}")
print(buffer.take())
print(buffer.take())
print(buffer.take())

