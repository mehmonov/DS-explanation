class Queue:
    def __init__(self):
        self.items = []  # Queue elementlarini saqlash uchun ro'yxat

    def enqueue(self, item):
        self.items.append(item)  # Elementni queue oxiriga qo'shish

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Queue boshidan elementni olish
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]  # Queue boshidagi elementni ko'rish
        return None

    def is_empty(self):
        return len(self.items) == 0  # Queue bo'sh yoki yo'qligini tekshirish

    def size(self):
        return len(self.items)  # Queue'dagi elementlar soni

    def display(self):
        print(self.items)  # Queue'dagi barcha elementlarni ko'rsatish

# Queue yaratish va ma'lumot qo'shish
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Queue'dan elementlarni olish va ko'rsatish
print("Queue'dan olingan element:", queue.dequeue())
print("Queue boshidagi element:", queue.peek())
print("Queue bo'shmi:", queue.is_empty())
print("Queue hajmi:", queue.size())

# Queue'dagi barcha elementlarni ko'rsatish
queue.display()