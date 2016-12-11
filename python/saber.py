#!/usr/bin/python
import os
import sys
import csv
import json
from time import sleep
from datetime import datetime

ShowProgress = False
ConvertTime = False


def print_welcome():
    print("""
[*******************************************************************************************************]

                        -----FINDING DUPLICATE OH16/OH20/O2 EVENTS----

This script will find duplicate OH16, OH20 and O2 events by iterating through two files from
F:/Data/Source_Altitude/DoubleHumps/ directory. It accepts the .txt file that is created by using the
"findDoubleHumpOH.mat" files in Matlab. Files should be of the same year and different channels i.e
"DoubleHumpsOH16_2010.txt", "DoubleHumpsOH20_2010.txt" and "DoublehumpsO2_2010.txt". The script will then
compare the two and returnthe correlated events. You will be asked to input the path and file names to both
input files as well as a name to have the new file be saved as. It is recommended that the file is saved in
a .csv format to easily be used by Microsoft Excel.

[*******************************************************************************************************]""")


def print_primary_options():
    print("""\n[*] Options:\n
    [1] Auto Correlate
    [2] Manually Correlate
    [3] Help
    [99] Quit
    """)


def print_secondary_options():
    print("""\n[*] Options:\n
    [1] Find OH16 & OH20 correlations
    [2] Find OH16, OH20 and O2 correlations
    [3] Help
    [99] Quit
    """)


def print_sort_options():
    print("""\n[*] Options:\n
    [1] Sort all
    [2] Sort by years
    [3] Sort by months
    [4] Sort by seasons
    [5] Help
    [99] Quit
    """)

#
# Print iterations progress
#


def print_progress(iteration, total, prefix='', suffix='', decimals=1, barLength=100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    formatStr = "{0:." + str(decimals) + "f}"
    percents = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '*' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


def initialize():
    if file_exists('settings.json'):
        print("Exists")
    else:
        settings = {
            'setup': 'false',
            'savePath': '',
            'loadPath': '',
            'dataPath': ''
        }
        s = json.dumps(settings)
        with open('settings.json', 'w') as f:
            f.write(s)
            f.close()

    print("[*] Initialized")


def is_windows():
    if sys.platform == "win32":
        return True

#
# Because Windows will be Windows...
#


def smart_input(message):
    if is_windows():
        return input(message)
    else:
        return raw_input(message)


def filepath_exists(path):
    if os.path.exists(path):
        return True


def file_exists(filename):
    if os.path.isfile(filename):
        return True


#
#  Strip file contents
#

def strip_contents(filename):
    contents = []
    f = open(filename)
    csv_f = csv.reader(f)

    for rows in csv_f:
        row4 = rows[4].strip()
        row5 = rows[5].strip()
        contents.append(rows[1].strip() + "_" + rows[2].strip() + "_" + rows[3].strip() + "_" + row4 + "_" + row5 + "_" + rows[6].strip())
    f.close()
    return contents


def find_duplicates(obj01, obj02, start_message):
    duplicates = []
    count = 0
    i = 0
    t = len(obj01)
    print("[*] " + start_message)
    if ShowProgress:
        print_progress(i, t, prefix='Progress', suffix="Complete", barLength=50)
    for OH16_rows in obj01:
        for OH20_rows in obj02:
            if OH16_rows == OH20_rows:
                duplicates.append(OH16_rows)
                count += 1
        if ShowProgress:
            i += 1
            print_progress(i, t, prefix='Progress', suffix="Complete", barLength=50)
    print("[*] Number of correlations: " + str(count))
    sleep(1)
    print("[*] Processing data completed!")
    sleep(1)
    return duplicates

#
# Convert data to CSV formatted
#


def format_list(text_list):
    print("[*] Converting list to CSV format...")
    formatted = []
    i = 0
    t = len(text_list)
    title = False
    if ShowProgress:
        print_progress(i, t, prefix='Progress', suffix="Complete", barLength=50)

    for rows in text_list:
        if not title:
            formatted.append('Data, Time, Orbit, Event, LAT, LONG')
        formatted.append(rows.replace("_", ", "))
        title = True
        if ShowProgress:
            i += 1
            print_progress(i, t, prefix='Progress', suffix="Complete", barLength=50)
    print("[*] Formatted...")
    return formatted

#
# Save file
#


def save_to_file(name, text):
    print("[*] Saving " + name + " file...")
    file_write = open(name, "w+")
    for rows in text:
        file_write.write(rows + "\n")
    file_write.close()
    print("[*] File saved successfully: " + name)


def get_and_check_file():
    name = smart_input("Enter the file path for a file: ")
    while not file_exists(name):
        name = smart_input("[!] Could not find file. Enter the file path for a file: ")
    return name


def save_file_as():
    save_name = smart_input("[*] Enter the name the file will be saved as (\"It will be saved as .csv\"): ")
    return save_name


def cwd():
    os.getcwd()


def manage_data_directory(type):
    if type == "1620":
        if not filepath_exists("Correlations/OH16_20/CSV/"):
            os.makedirs("Correlations/OH16_20/CSV/")
        if not filepath_exists("Correlations/OH16_20/TXT/"):
            os.makedirs("Correlations/OH16_20/TXT/")
    elif type == "O2":
        if not filepath_exists("Correlations/OH16_20_O2/CSV/"):
            os.makedirs("Correlations/OH16_20_O2/CSV/")
        if not filepath_exists("Correlations/OH16_20/TXT/"):
            os.makedirs("Correlations/OH16_20_O2/TXT/")
    else:
        print "[!] Something went wrong.."

# Script begins
#welcome_message()
#OH16_filename = smart_input("Enter the file path for an OH16 file: ")
#while not file_exists(OH16_filename):
#    OH16_filename = smart_input("[!] - Could not find file. Enter the file path for an OH16 file: ")

#OH20_filename = smart_input("Enter the file path for an OH20 file: ")
#while not file_exists(OH20_filename):
#    OH20_filename = smart_input("[!] - Could not find file. Enter the file path for an OH20 file: ")
#
#O2_filename = smart_input("Enter the file path for an O2 file: ")
#while not file_exists(O2_filename):
#    O2_filename = smart_input("[!] - Could not find file. Enter the file path for an O2 file: ")

#save_name = smart_input("Enter the name the file will be saved as (\"It will be saved as .csv\"): ")
#progress = smart_input("Do you want to show the progress? y/n: ")

#if progress == 'y':
#    ShowProgress = True

#OH16 = truncate_contents(OH16_filename)
#OH20 = truncate_contents(OH20_filename)
#O2 = truncate_contents(O2_filename)
#oh1620 = find_oh1620(OH16, OH20)
#oho2 = find_OHO2(oh1620, O2)
#formatted_list = format_list(oho2)

#os.getcwd()

#if not filepath_exists("Correlations/OH16_20_O2/CSV/"):
#    os.makedirs("Correlations/OH16_20_O2/CSV/")

#if not filepath_exists("Correlations/OH16_20_O2/TXT/"):
#    os.makedirs("Correlations/OH16_20_O2/TXT/")

#save_list_to_file("Correlations/OH16_20_O2/CSV/" + save_name + ".csv", formatted_list)
#save_list_to_file("Correlations/OH16_20_O2/TXT/" + save_name + ".txt", formatted_list)
