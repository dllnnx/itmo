from time import time
import obl_task, dop_task_1, dop_task_2, dop_task_3

def timer(func, n):
    st = time()
    for _ in range(n): func()
    return time() - st

for name, pars in  [('obl_task', obl_task), ('dop_task_1', dop_task_1), ('dop_task_2', dop_task_2), \
                    ('dop_task_3', dop_task_3)]:
    print(f'{name}: {timer(pars.main, 100)} s')

