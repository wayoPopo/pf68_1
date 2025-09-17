import os
import random
import string


def create_random_list(n: int) -> str:
    """
    สร้างลิสต์ที่มีความยาว n ซึ่งแต่ละสมาชิกเป็นค่าสุ่มจากประเภท
    int, float, boolean, หรือ string
    """
    if n <= 0:
        return []

    type_choices = ['int', 'float', 'bool', 'str']

    string_characters = string.ascii_letters + string.digits

    mixed_list = []
    for _ in range(n):
        chosen_type = random.choice(type_choices)
        if chosen_type == 'int':
            value = random.randint(-100, 100)
        elif chosen_type == 'float':
            value = round(random.uniform(-100.0, 100.0), 2)
        elif chosen_type == 'bool':
            value = random.choice([True, False])
        else:  # 'str'
            str_length = random.randint(3, 10)
            value = ''.join(random.choices(string_characters, k=str_length))
        mixed_list.append(value)
    ret = ''
    for value in mixed_list:
        ret += str(value)+" "

    return ret