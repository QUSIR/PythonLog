#coding: utf-8
import os
import time
import logging
is_debug=True

def make_dir(make_dir_path):
    path = make_dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def set_log():
    global logging
    project_name = "PythonLog"
    folder_format = time.strftime('%Y-%m', time.localtime(time.time()))
    log_file_name = project_name + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
    make_dir(folder_format)
    log_file_str = folder_format + os.sep + log_file_name
    logger = logging.getLogger()
    if is_debug == True:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.ERROR)
    logger_format = logging.Formatter(fmt='%(levelname)s:%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logger_fh = logging.FileHandler(log_file_str)
    logger_fh.setFormatter(logger_format)
    logger.addHandler(logger_fh)

def main():
    print("main run")
    set_log()
    logging.info('main run')

if __name__ == "__main__":
    main()