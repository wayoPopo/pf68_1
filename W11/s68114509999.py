import os
from typing import List
from dotenv import load_dotenv
import re
import numpy as np
#ไลบรารีที่จำเป็น:
# pip install python-dotenv numpy


def read_first_line(fname = os.path.join(os.path.dirname(__file__),'settings.txt')) -> str:
    pass

def get_test_dir_from_env() -> str:
    pass

def read_and_join_lines(fname = os.path.join(os.path.dirname(__file__),'settings.txt') ) -> str:
    pass

def extract_numbers_from_file(filename: str) -> List[float]:
    pass

def calculate_average_from_file(filename: str) -> float:
    pass

def find_top_three_from_file(filename: str) -> List[float]:
    pass


def calculate_trimmed_mean_from_file(filename: str) -> float:
    pass


# --- โจทย์เสริมภาคสมัครใจ (Advanced) ---

def equations_to_matrix(filename: str) -> List[List[float]]:
    pass


def solve_system(matrix: List[List[float]]) -> List[float]:
    pass