import os
import re
from typing import List
from dotenv import load_dotenv
import numpy as np

load_dotenv('../../W11/')

def read_first_line(fname:str) -> str:
    with open(fname, 'r', encoding='utf-8') as f:
        return f.readline()


def get_test_dir_from_env(fdir) -> str:
    envpath = os.path.join(fdir, '.env')
    load_dotenv(dotenv_path=envpath)  # โหลดค่าจาก .env เข้าสู่ environment
    return os.getenv("TEST_DIR")


def read_and_join_lines(fname:str) -> str:
    """
    ข้อ 3: อ่าน 2 บรรทัดแรกจาก 'settings.txt' แล้วนำมาต่อกันด้วย ','
    """
    with open(fname, 'r', encoding='utf-8') as f:
        line1 = f.readline().strip()
        line2 = f.readline().strip()
        return f"{line1},{line2}"


def extract_numbers_from_file(filename: str) -> List[float]:
    """
    ข้อ 4: อ่านไฟล์และคัดแยกเฉพาะตัวเลข (จำนวนเต็มหรือทศนิยม) ออกมาเป็น List[float]
    """
    numbers = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            # แทนที่ comma ด้วย space เพื่อให้มีตัวคั่นแบบเดียว
            content = content.replace(',', ' ')
            tokens = content.split()

            for token in tokens:
                try:
                    numbers.append(float(token))
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"Error: ไม่พบไฟล์ {filename}")
        return []

    return numbers


def calculate_average_from_file(filename: str) -> float:
    """
    ข้อ 5: อ่านไฟล์และหาค่าเฉลี่ยของตัวเลขทั้งหมดที่ปรากฏ
    """
    numbers = extract_numbers_from_file(filename)
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def find_top_three_from_file(filename: str) -> List[float]:
    """
    ข้อ 6: อ่านไฟล์และหาค่าสูงสุด 3 อันดับแรกของตัวเลข
    """
    numbers = extract_numbers_from_file(filename)
    # เรียงลำดับจากมากไปน้อย
    numbers.sort(reverse=True)
    # คืนค่า 3 ตัวแรก (slicing จะจัดการกรณีที่มีน้อยกว่า 3 ตัวให้เอง)
    return numbers[:3]


def calculate_trimmed_mean_from_file(filename: str) -> float:
    """
    ข้อ 7: หาค่าเฉลี่ยของตัวเลขตรงกลาง โดยไม่รวมค่าสูงสุดและต่ำสุด
    """
    numbers = extract_numbers_from_file(filename)
    if len(numbers) < 3:
        return 0.0

    return (sum(numbers) -max(numbers)-min(numbers)) / (len(numbers)-2)


# --- โจทย์เสริมภาคสมัครใจ (Advanced) ---

def equations_to_matrix(filename: str) -> List[List[float]]:
    """
    ข้อ 8.1: แปลงสมการจากไฟล์เป็น Augmented Matrix
    """
    matrix = []
    # Regular Expression เพื่อหาตัวเลขทั้งหมด (รวมทศนิยมและเครื่องหมายลบ)
    pattern = re.compile(r"[-+]?\d*\.\d+|[-+]?\d+")

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                # หาตัวเลขทั้งหมดในบรรทัด
                matches = pattern.findall(line)

                # แปลงค่าที่ได้เป็น float และสร้างเป็นแถวของ matrix
                if len(matches) == 4:  # ควรจะมี 4 ค่า (a, b, c, d)
                    row = [float(val) for val in matches]
                    matrix.append(row)
    except FileNotFoundError:
        print(f"Error: ไม่พบไฟล์ {filename}")
        return []

    return matrix


def solve_system(matrix: List[List[float]]) -> List[float]:
    """
    ข้อ 8.2: แก้ระบบสมการจาก Matrix ที่ได้ และคืนค่า [x, y, z]
    """
    if not matrix or len(matrix) != 3:
        return []

    # แปลง List of Lists เป็น NumPy array
    A = np.array(matrix)

    # แยกเมทริกซ์สัมประสิทธิ์ (coefficients) และเวกเตอร์ค่าคงที่ (constants)
    coefficients = A[:, :3]  # เอาทุกแถว, 3 คอลัมน์แรก (0, 1, 2)
    constants = A[:, 3]  # เอาทุกแถว, คอลัมน์สุดท้าย (3)

    try:
        # ใช้ numpy.linalg.solve เพื่อแก้สมการ
        solution = np.linalg.solve(coefficients, constants)
        # แปลงผลลัพธ์กลับเป็น list ของ float
        return solution.tolist()
    except np.linalg.LinAlgError:
        # กรณีที่หาคำตอบไม่ได้ (singular matrix)
        return []