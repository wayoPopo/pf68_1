import os
import sys
from s68114509999 import *
import glob
import numpy as np

module_path = os.path.join(os.path.dirname(__file__), '..\\resources\\W11\\')
print(module_path)
sys.path.append(module_path)
from resources.W11 import solutions as wayosaid
print(read_first_line())
print(wayosaid.get_test_dir_from_env(os.path.dirname(__file__)))
#project_dir = os.path.join(os.path.dirname(__file__), '..\\W11')
#print(os.path.join(os.path.dirname(__file__)))
print(get_test_dir_from_env())
#os.path.join(...) #คือการนำ path มาต่อกันอย่างถูกต้องตามแต่ละ OS

try:
    #dir_pathf = os.path.join(os.path.dirname(__file__),'.')
    searchf = os.path.join(os.path.dirname(__file__), 'data*.txt')
    flist = glob.glob(searchf)
    print(flist)
    for f in flist:
        print(f)
        print(read_first_line(f))
    #assert a.shape == b.shape, "@test_equations_to_matrix --> ขนาด augmented matrix ไม่ถูกต้อง"
    #print(a - b)
    #assert np.mean(np.abs(np.reshape(a, -1) - np.reshape(b,-1))) < 0.001, f"@test_equations_to_matrix --> ค่าผิดพลาด MAE มากกว่า 0.001 \ntest = {a}, \nexpected = {b} ,\n {np.abs(np.reshape(a, -1) - np.reshape(b, -1))}"
except Exception as e:
    print(e)