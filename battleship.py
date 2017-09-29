#!/usr/bin/env python
import os

def c_dir_list():
    message = "current directory contains next files:"
    c_dir_list = str(os.listdir())
    output = message + "\n" + c_dir_list
    print(output)
    return output

c_dir_list()
os.makedirs("temp_dir", mode=0o777, exist_ok=True)
print("new call after update")
c_dir_list()
print("testtesttest2")
