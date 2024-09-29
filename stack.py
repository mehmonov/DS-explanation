class Stack:
    def __init__(self):
        self.items = []  # Stack elementlarini saqlash uchun ro'yxat

    def push(self, item):
        self.items.append(item)  # Elementni stack'ga qo'shish

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Stack'dan elementni olish
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Stack'dagi eng yuqori elementni ko'rish
        return None

    def is_empty(self):
        return len(self.items) == 0  # Stack bo'sh yoki yo'qligini tekshirish

    def size(self):
        return len(self.items)  # Stack'dagi elementlar soni

    def display(self):
        print(self.items)  # Stack'dagi barcha elementlarni ko'rsatish

# Stack yaratish va ma'lumot qo'shish
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

# Stack'dan elementlarni olish va ko'rsatish
print("Stack'dan olingan element:", stack.pop())
print("Stack'dagi eng yuqori element:", stack.peek())
print("Stack bo'shmi:", stack.is_empty())
print("Stack hajmi:", stack.size())

# Stack'dagi barcha elementlarni ko'rsatish
stack.display()