# s6811450123.py

def count_character_frequency(text: str) -> dict:
    """นับความถี่ของตัวอักษรแต่ละตัวในข้อความ (ไม่รวม space, case-insensitive)"""
    frequency = {}
    for char in text.lower():
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    return frequency

def find_common_elements(list1: list, list2: list) -> list:
    """หาตัวร่วมในลิสต์สองชุดและคืนค่าเป็นลิสต์ที่เรียงลำดับแล้ว"""
    return sorted(list(set(list1) & set(list2)))

def format_name(full_name: str) -> str:
    """จัดรูปแบบชื่อ-นามสกุลให้ขึ้นต้นด้วยตัวพิมพ์ใหญ่"""
    return full_name.title()

def fibonacci_sequence(n: int) -> list:
    """สร้างลำดับฟีโบนัชชี n ตัวแรก"""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    while len(sequence) < n:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence

def is_prime(number: int) -> bool:
    """ตรวจสอบว่าเป็นจำนวนเฉพาะหรือไม่"""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def calculate_total_sales(sales_data: list) -> float:
    """คำนวณยอดขายรวมจากลิสต์ของ Dictionary"""
    total = 0.0
    for item in sales_data:
        total += item.get('price', 0) * item.get('quantity', 0)
    return total

def find_longest_word(sentence: str) -> str:
    """หาคำที่ยาวที่สุดในประโยค"""
    words = sentence.split()
    if not words:
        return ""
    return max(words, key=len)

def invert_dictionary(d: dict) -> dict:
    """สลับค่า Key และ Value ใน Dictionary"""
    return {value: key for key, value in d.items()}

def caesar_cipher_encrypt(text: str, shift: int) -> str:
    """เข้ารหัสข้อความภาษาอังกฤษด้วย Caesar Cipher"""
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            result += shifted_char
        elif 'A' <= char <= 'Z':
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            result += shifted_char
        else:
            result += char
    return result

def bubble_sort(numbers: list) -> list:
    """เรียงลำดับตัวเลขในลิสต์จากน้อยไปมากด้วย Bubble Sort"""
    n = len(numbers)
    # ทำสำเนาของลิสต์เพื่อไม่ให้กระทบลิสต์เดิม
    nums_copy = numbers[:]
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if nums_copy[j] > nums_copy[j+1]:
                nums_copy[j], nums_copy[j+1] = nums_copy[j+1], nums_copy[j]
                swapped = True
        if not swapped:
            break
    return nums_copy