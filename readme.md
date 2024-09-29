# Data Structures Explanation

## Binary Tree 

### Tushuntirish:
**Binary Tree** - har bir tugun (node) ikki yo'nalishga (chap va o'ng) ega bo'lishi mumkin bo'lgan daraxt tuzilmasidir.

### Ishlash printsipi:
- Har bir tugun qiymatga ega va chap yo'nalishlar kichikroq qiymatlarni, o'ng yo'nalishlar esa katta qiymatlarni saqlaydi.

### Turlari:
- **Binary Search Tree (BST)**: Har bir tugun uchun chap yo'nalishlar kichikroq, o'ng yo'nalishlar katta qiymatga ega.
- **Balanced Binary Tree**: Tugunlar balansi saqlanadi (masalan, AVL daraxti, Red-Black daraxti).
- **Complete Binary Tree**: Har bir daraja to'liq to'ldirilgan yoki faqat oxirgi daraja qisman to'ldirilgan.

### Kod:
[Binary Tree Implementation](tree.py)

## Stack 

### Tushuntirish:
**Stack** - bu LIFO (Last In, First Out) prinsipiga asoslangan ma'lumotlar tuzilmasi.

### Ishlash printsipi:
- Eng oxirgi qo'shilgan element birinchi bo'lib olinadi.

### Turlari:
- **Array-based Stack**: Stack elementlari massivda saqlanadi.
- **Linked List-based Stack**: Stack elementlari bog'langan ro'yxatda saqlanadi.

### Kod:
[Stack Implementation](stack.py)

## Linked List 

### Tushuntirish:
**Linked List** - bu tugunlar zanjiri bo'lib, har bir tugun ma'lumot va keyingi tugunga ishorani saqlaydi.

### Ishlash prinsipi:
- Har bir tugun keyingi tugunga ishora qiladi, oxirgi tugun `None`ga ishora qiladi.

### Turlari:
- **Singly Linked List**: Har bir tugun faqat keyingi tugunga ishora qiladi.
- **Doubly Linked List**: Har bir tugun oldingi va keyingi tugunga ishora qiladi.
- **Circular Linked List**: Oxirgi tugun birinchi tugunga ishora qiladi.

### Kod:
[Linked List Implementation](linked-list.py)

## Queue (Navbat)

### Tushuntirish:
**Queue** - bu FIFO (First In, First Out) prinsipiga asoslangan ma'lumotlar tuzilmasi.

### Ishlash printsipi:
- Eng birinchi qo'shilgan element birinchi bo'lib olinadi.

### Turlari:
- **Array-based Queue**: Queue elementlari massivda saqlanadi.
- **Linked List-based Queue**: Queue elementlari bog'langan ro'yxatda saqlanadi.
- **Circular Queue**: Oxirgi element birinchi elementga ishora qiladi, bu orqali bo'sh joydan samarali foydalanish mumkin.

### Kod:
[Queue Implementation](queue.py)