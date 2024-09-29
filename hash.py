class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Hash jadvalini yaratish

    def hash_function(self, key):
        return hash(key) % self.size  # Hash funksiyasi

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        # Key va value juftligini qo'shish
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def remove(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i, pair in enumerate(self.table[index]):
                if pair[0] == key:
                    del self.table[index][i]
                    return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")

# Hash jadvalini yaratish va ma'lumot qo'shish
ht = HashTable(10)
ht.insert("apple", 1)
ht.insert("banana", 2)
ht.insert("orange", 3)

# Hash jadvalidan ma'lumot olish va ko'rsatish
print("apple:", ht.get("apple"))
print("banana:", ht.get("banana"))
print("orange:", ht.get("orange"))

# Hash jadvalidan ma'lumotni o'chirish
ht.remove("banana")

# Hash jadvalini ko'rsatish
ht.display()