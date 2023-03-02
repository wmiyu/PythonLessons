#!/bin/python3
# ************************************************************************** */
#
#                                                        :::      ::::::::  
#   less_2_5_CleanUp.py                                 :+:      :+:    :+:
#                                                    +:+ +:+         +:+    
#   By: wmiyu <wmiyu@student.21-school.ru>         +#+  +:+       +#+   
#                                                +#+#+#+#+#+   +#+        
#   Created: 15.02.2023 A.D.                          #+#    #+#       
#                                                    #+#   #+#+#+#+#  
#   Description: Clean UP old files tool
# ************************************************************************** */

import os, time, sys

FILES_AGE_IN_DAYS = 0
TOTAL_DELETED_FILE = 0
TOTAL_DELETED_SIZE = 0
TOTAL_DELETED_DIRS = 0


def delete_old_files(folder, age_time_in_days):
    """Delete files older X age_time_in_days DAYS"""
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder, topdown=False):
        for file in files:
            file_name = os.path.join(path, file)
            file_time = os.path.getmtime(file_name)
            print("Looking for file : ", file_name)
            if file_time < age_time_in_days:
                file_size = os.path.getsize(file_name)
                print("Deleting file : " + str(file_name))
                TOTAL_DELETED_FILE += 1
                TOTAL_DELETED_SIZE += file_size
                os.remove(file_name)
            else:
                print(" (!) File Too young to die...")


def delete_empty_dir(folder):
    global TOTAL_DELETED_DIRS
    for path, dirs, files in os.walk(folder, topdown=False):
        print("Looking for folder : ", path)
        if len(os.listdir(path)) == 0:
            print("Deleting EMPTY folder: " + str(path))
            TOTAL_DELETED_DIRS += 1
            os.rmdir(path)


# =================================== MAIN ================================
if len(sys.argv) < 2:
    print("Too few arguments. Usage to CLEAN UP dirs: cmd FILES_AGE_IN_DAYS <dir1> ... <dirX>")
    sys.exit(1)
try:
    FILES_AGE_IN_DAYS = int(sys.argv[1])
except Exception:
    print("Bad arguments. Usage to CLEAN UP dirs: cmd FILES_AGE_IN_DAYS <dir1> ... <dirX>")
    sys.exit(1)

arguments: [] = sys.argv[2:]
startTime = time.asctime()

nowTime = time.time()
ageTime = nowTime - 60*60*24*FILES_AGE_IN_DAYS

for arg in arguments:
    delete_old_files(arg, age_time_in_days=ageTime)
    delete_empty_dir(arg)

finishTime = time.asctime()

print("------------------------------------------------------------------")
print("JOB STARTED : ", str(startTime))
print(" (i) TOTAL_DELETED_FILE = " + str(TOTAL_DELETED_FILE))
print(" (i) TOTAL_DELETED_SIZE = " + str(int(TOTAL_DELETED_SIZE)) + " Bytes")
print(" (i) TOTAL_DELETED_DIRS = " + str(TOTAL_DELETED_DIRS))
print("JOB FINISHED : ", str(finishTime))
