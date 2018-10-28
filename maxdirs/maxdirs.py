import os
import sys
import datetime
import time

ab_path = os.path.abspath(__file__)
cur_dir = os.getcwd()
timestr = time.strftime("%Y%m%d-%H%M%S")
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def create_dir(new_dir_name=''):
    full_path = ab_path + "\\" + new_dir_name
    print("FULL CLIP PATH: ", full_path)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    return full_path


def get_items_in_dir(dir_loc, file_type=''):
    all_paths = []
    the_folder = dir_loc
    for file in os.listdir(the_folder):
        if file.endswith(file_type):
            the_item= file


    return all_paths