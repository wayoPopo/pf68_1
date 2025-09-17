# test_solutions.py
import sys
import glob
import pytest
import os
import random as rnd
import numpy as np

from s68114509999 import *

module_path = os.path.join(os.path.dirname(__file__), '..\\resources\\W11\\')
sys.path.append(module_path)
from resources.W11 import solutions as wayosaid
from resources.W11 import gen as wayogg

def test_read_first_line():
    assert read_first_line(os.path.join(os.path.dirname(__file__),'settings.txt')) == wayosaid.read_first_line(os.path.join(os.path.dirname(__file__),'settings.txt'))

def test_get_test_dir_from_env():
    assert get_test_dir_from_env() == wayosaid.get_test_dir_from_env(os.path.dirname(__file__))

def test_read_and_join_lines():
    assert read_and_join_lines(os.path.join(os.path.dirname(__file__),'settings.txt')) == wayosaid.read_and_join_lines(os.path.join(os.path.dirname(__file__),'settings.txt'))

def test_extract_numbers_from_file():
    for i in range(7):
        with open(os.path.join(os.path.dirname(__file__), f'data{i+4}.txt'), 'w') as f:
            f.writelines(wayogg.create_random_list(rnd.randint(10, 100)))
    dir_pathf = os.path.join(os.path.dirname(__file__),'.')
    searchf = os.path.join(dir_pathf, 'data*.txt')
    flist = glob.glob(searchf)
    for ff in flist:
        assert extract_numbers_from_file(ff) == wayosaid.extract_numbers_from_file(ff)

def test_calculate_average_from_file():
    for i in range(7):
        with open(os.path.join(os.path.dirname(__file__), f'data{i+4}.txt'), 'w') as f:
            f.writelines(wayogg.create_random_list(rnd.randint(10, 100)))
    dir_pathf = os.path.join(os.path.dirname(__file__),'.')
    searchf = os.path.join(dir_pathf, 'data*.txt')
    flist = glob.glob(searchf)
    for ff in flist:
        assert calculate_average_from_file(ff) == wayosaid.calculate_average_from_file(ff),'@test_calculate_average_from_file'

def test_find_top_three_from_file():
    for i in range(7):
        with open(os.path.join(os.path.dirname(__file__), f'data{i+4}.txt'), 'w') as f:
            f.writelines(wayogg.create_random_list(rnd.randint(10, 100)))
    dir_pathf = os.path.join(os.path.dirname(__file__),'.')
    searchf = os.path.join(dir_pathf, 'data*.txt')
    flist = glob.glob(searchf)
    #print(flist)
    for ff in flist:
        result = find_top_three_from_file(ff)
        expected = wayosaid.find_top_three_from_file(ff)
        inputV = wayosaid.read_first_line(ff)
        assert find_top_three_from_file(ff) == wayosaid.find_top_three_from_file(ff),f'@test_find_top_three_from_file :\n {inputV} \n {result} !=\n {expected}'


def test_calculate_trimmed_mean_from_file():
    for i in range(7):
        with open(os.path.join(os.path.dirname(__file__), f'data{i+4}.txt'), 'w') as f:
            f.writelines(wayogg.create_random_list(rnd.randint(10, 100)))
    dir_pathf = os.path.join(os.path.dirname(__file__),'.')
    searchf = os.path.join(dir_pathf, 'data*.txt')
    flist = glob.glob(searchf)
    for ff in flist:
        result = calculate_trimmed_mean_from_file(ff)
        expected = wayosaid.calculate_trimmed_mean_from_file(ff)
        inputV = wayosaid.read_and_join_lines(ff)
        #print(inputV)
        assert result == expected,f'@test_calculate_trimmed_mean_from_file:\n inputV={inputV} -->  output={result} : expected={expected}'

def test_equations_to_matrix():
    """ทดสอบฟังก์ชัน equations_to_matrix"""

    try:
        fname = os.path.join(os.path.dirname(__file__), 'testcase.txt')
        a = np.array(equations_to_matrix(fname),dtype=float)
        b = np.array(wayosaid.equations_to_matrix(fname),dtype=float)
        assert a.shape == b.shape, "@test_equations_to_matrix --> ขนาด augmented matrix ไม่ถูกต้อง"
        #print(a-b)
        avg = np.mean(np.abs(np.reshape(a,-1)-np.reshape(b,-1)))

        assert avg < 0.001, f"@test_equations_to_matrix --> ค่าผิดพลาด MAE มากกว่า 0.001, {avg}"
    except Exception as e:
        print(e)


def test_solve_system():
    try:
        fname = os.path.join(os.path.dirname(__file__), 'testcase.txt')
        a = np.array(solve_system(equations_to_matrix(fname)), dtype=float)
        b = np.array(solve_system(wayosaid.equations_to_matrix(fname)), dtype=float)
        assert a.shape == b.shape, "@test_solve_system --> ขนาด list ไม่ถูกต้อง"
        avg = np.mean(np.abs(a-b))
        assert avg < 0.001, f"@test_solve_system --> ค่าผิดพลาด MAE มากกว่า 0.001, {avg}"
    except Exception as e:
        print(e)