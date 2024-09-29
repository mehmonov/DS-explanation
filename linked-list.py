class Node:
    def __init__(self, data):
        self.data = data  # Node ma'lumotlari
        self.next = None  # Keyingi Node'ga ishora

class LinkedList:
    def __init__(self):
        self.head = None  # Ro'yxatning boshini belgilash

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Linked list yaratish va ma'lumot qo'shish
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

# Linked listni ko'rsatish
ll.display()