import csv
import queue

def make_csv(tasklist, sorted_list, EF, cp_list, save_path):
    for cp_task in cp_list:
        tasklist[cp_task]['is_cp'] = 'x'

    with open(save_path, 'w', newline="", encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'task_name','time', 'ES', 'EF','is_cp']+list(range(1, int(EF)+1)))
        for task in sorted_list:
            do_day = [0] * int(EF)
            for i in range(tasklist[task]['ES'], tasklist[task]['EF']+1):
                do_day[i-1] = 1            
            writer.writerow([task,
                            tasklist[task]['name'],
                            tasklist[task]['time'],
                            tasklist[task]['ES'],
                            tasklist[task]['EF'],
                            tasklist[task]['is_cp']]
                            + do_day) 

def find_cp(tasklist, EF):
    cp_list = []
    q = queue.Queue()
    for id in tasklist:
        if tasklist[id]['EF'] == EF:
            q.put(id)
            cp_list.append(id)
    while not q.empty():
        id = q.get()
        for previous_id in tasklist[id]['predecessor']:
            if tasklist[previous_id]['EF'] == tasklist[id]['ES']-1:
                q.put(previous_id)
                cp_list.append(previous_id)
    
    return cp_list


def task_sort(tasklist,sorted_list,unsorted_list):
    limit = len(tasklist)
    for i in range(limit+1):
        tmp = []
        done_list = set(sorted_list)
        for id in unsorted_list:
            if len(set(tasklist[id]['predecessor'])-done_list) == 0:
                sorted_list.append(id)
                unsorted_list.remove(id)
        if len(unsorted_list) == 0:
            break
    else:
        print('WARNING:there are unsorted task!')

    return sorted_list

def estimate_EF(tasklist, sorted_list):
    for id in sorted_list:
        if tasklist[id]['EF'] != -1:
            continue
        for require_id in tasklist[id]['predecessor']:
            #tasklist[id]['ES'] = max(tasklist[id]['ES'], tasklist[require_id]['EF'])+1
            tasklist[id]['ES'] = max(tasklist[id]['ES'], tasklist[require_id]['EF'])
        tasklist[id]['ES'] = tasklist[id]['ES']+1
        tasklist[id]['EF'] = tasklist[id]['ES'] + tasklist[id]['time'] - 1
    return tasklist

def get_tasklist(path):
    tasklist = {}
    start_list = []
    unsorted_list = []
    with open(path, encoding='utf8') as f:
        reader = csv.reader(f)
        i = 0
        for row in reader:
            if i == 0:
                i = i + 1
                continue
            name = row[1]
            tasklist[i] = {}
            tasklist[i]['name'] = row[1]
            tasklist[i]['time'] = int(row[2])
            if row[3] == '':
                tasklist[i]['predecessor'] = []
                tasklist[i]['ES'] = 1
                tasklist[i]['EF'] = int(row[2])
                start_list.append(i)
            else:
                tasklist[i]['predecessor'] = list(map(int,row[3].split('.')))
                tasklist[i]['ES'] = -1
                tasklist[i]['EF'] = -1
                unsorted_list.append(i)
            tasklist[i]['LS'] = -1
            tasklist[i]['LF'] = -1
            tasklist[i]['is_cp'] = '' #1 is cp
            i = i + 1
    return tasklist, start_list, unsorted_list