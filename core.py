import csv
import sys, os ,pathlib
#sys.path.append(pathlib.Path(__file__).resolve().parents[1].as_posix())
from critical_path import utils

path = './test/test.csv'
save_path = './test/save.csv'
tasklist, start_list, unsorted_list = utils.get_tasklist(path)
sorted_list = utils.task_sort(tasklist,start_list,unsorted_list)
tasklist = utils.estimate_EF(tasklist, sorted_list)
EF = tasklist[sorted_list[-1]]['EF']
cp_list = utils.find_cp(tasklist, EF)
print('Early finish time is', EF)
utils.make_csv(tasklist, sorted_list, EF, cp_list, save_path)


