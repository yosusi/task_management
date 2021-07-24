import csv
import sys, os ,pathlib
#sys.path.append(pathlib.Path(__file__).resolve().parents[1].as_posix())
from critical_path import utils

def analysis(load_path=None, save_path=None):
    tasklist, start_list, unsorted_list = utils.get_tasklist(load_path)
    sorted_list = utils.task_sort(tasklist,start_list,unsorted_list)
    print(sorted_list)
    tasklist = utils.estimate_EF(tasklist, sorted_list)
    EF = 0
    for i in sorted_list:
        EF = max(EF, tasklist[i]['EF'])
    cp_list = utils.find_cp(tasklist, EF)
    print('Early finish time is', EF)
    utils.make_csv(tasklist, sorted_list, EF, cp_list, save_path)
    print('analysis is done')
    

if __name__ == '__main__':
    load_path = './test/日本語テスト.csv'
    save_path = './test/日本語保存.csv'
    analysis(load_path, save_path)
