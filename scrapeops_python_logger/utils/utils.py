import time
import sys
import platform
import scrapeops_python_logger

from scrapeops_python_logger.utils.error_handling import exception_handler

def current_time():
    t = time.time()
    return int(round(t, 0))

@exception_handler
def get_args():
    arg_dict = {'raw_string': '', 'args': [], 'options': []}
    if sys.argv[0] == 'crawl' or sys.argv[0]  == 'runspider': 
        args = sys.argv[2:]
    else:
        args = sys.argv[1:]
    for index, arg in enumerate(args):
        arg_dict['raw_string'] += append_raw_string(arg)
        if arg.startswith('--'):
            arg_dict['options'].append(arg)
        if arg.startswith('-a'):
            try:                   
                if args[index + 1].startswith('-') is False and args[index + 1].startswith('--') is False: arg_dict['args'].append(args[index + 1])  
            except Exception:
                arg_dict['args'].append(arg)
    return arg_dict


@exception_handler
def get_python_version():
    verions_string = sys.version
    split_string = verions_string.split(' ')
    return split_string[0]

@exception_handler
def get_scrapeops_version():
    return scrapeops_python_logger.__version__

@exception_handler
def get_system_version():
    return platform.platform()

def append_raw_string(arg):
    if ' ' in arg:
         return '"{}"  '.format(arg)
    return "{}  ".format(arg)

def merge_dicts(x, y):
    z = x.copy()   
    z.update(y)
    return z




