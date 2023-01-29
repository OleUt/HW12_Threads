import concurrent.futures
import time
import math


def factorial_calculation(n):
    fct = math.factorial(n)
    print(f'factorial of {n} = {fct}\n')


values = [7, 8, 9]
tp_time, pp_time = 0, 0
optimal_method = 'not defined'

if __name__ == '__main__':
    print('ThreadPoolExecutor')
    tp_start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as tp_exe:
        tp_exe.submit(factorial_calculation, 13)
        tp_exe.submit(factorial_calculation, 12)
        tp_exe.submit(factorial_calculation, 11)
        tp_exe.map(factorial_calculation, values)
    tp_time = time.time() - tp_start_time

if __name__ == '__main__':
    print('ProcessPoolExecutor')
    pp_start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as pp_exe:
        pp_exe.submit(factorial_calculation, 13)
        pp_exe.submit(factorial_calculation, 12)
        pp_exe.submit(factorial_calculation, 11)
        pp_exe.map(factorial_calculation, values)
    pp_time = time.time() - pp_start_time

if tp_time < pp_time:
    optimal_method = 'ThreadPoolExecutor'
else:
    optimal_method = 'ProcessPoolExecutor'

if pp_time != 0 and tp_time != 0:
    print('ThreadPoolExecutor time=', tp_time)
    print('ProcessPoolExecutor time=', pp_time)
    print('optimal method: ', optimal_method)
