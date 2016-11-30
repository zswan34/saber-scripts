#!/usr/bin/python
import os.path
import sys
import csv
from time import sleep

OH16_CONTENTS = []  # OH16
OH20_CONTENTS = []  # OH20
ShowProgress = False


def welcome_message():
    print("""
[*******************************************************************************************************]
                        -----FINDING DUPLICATE OH16/OH20/O2 EVENTS----
This script will find duplicate OH16, OH20 and O2 events by iterating through two files from
F:/Data/Source_Altitude/DoubleHumps/ directory. It accepts the .txt file that is created by using the
"findDoubleHumpOH.mat files in Matlab." Files should be of the same year and different channels i.e
"DoubleHumpsOH16_2010.txt" and "DoubleHumpsOH20_2010.mat". The script will then compare the two and return
the correlated events. You will be asked to input the path and file names to both input files as well as
a name to have the new file be saved as. It is recommended that the file is saved in a .csv format to easily
be used by Microsoft Excel.
[*******************************************************************************************************]""")


# Print iterations progress
def printProgress(iteration, total, prefix='', suffix='', decimals=1, barLength=100):
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


def filepath_exists(path):
    if os.path.exists(path):
        return True


def file_exists(filename):
    if os.path.isfile(filename):
        return True


def trunicate_contents(filename):
    contents = []
    f = open(filename)
    csv_f = csv.reader(f)

    for rows in csv_f:
        row4 = rows[4].strip()
        row5 = rows[5].strip()
        contents.append(rows[1].strip() + "_" + rows[2].strip() + "_" + rows[3].strip() + "_" + row4 + "_" + row5)
    f.close()
    return contents


def trunicate_contents_O2(filename):
    contents = []
    f = open(filename)
    csv_f = csv.reader(f)

    for rows in csv_f:
        row5 = rows[5].strip()
        row6 = rows[6].strip()
        contents.append(rows[1].strip() + "_" + rows[2].strip() + "_" + rows[3].strip() + "_" + rows[4].strip() + "_" + row5 + "_" + row6)
    f.close()
    return contents


def find_oh1620(channel_01, channel_02):
    oh1620 = []

    i = 0
    t = len(channel_01)
    print("Finding OH16 and OH20 correlations...")
    if ShowProgress:
        printProgress(i, t, prefix='Progress', suffix="Complete", barLength=50)
    for OH16_rows in channel_01:
        for OH20_rows in channel_02:
            if OH16_rows == OH20_rows:
                oh1620.append(OH16_rows)
        if ShowProgress:
            i += 1
            printProgress(i, t, prefix='Progress', suffix="Complete", barLength=50)
    print("OH16 and OH20 correlations found.")
    sleep(3)
    print("Processing data completed!")
    sleep(1)
    return oh1620


def find_OHO2(OH, O2):
    oh1620O2 = []

    i = 0
    t = len(OH)
    print("Finding OH16, OH20 and O2 correlations...")
    if ShowProgress:
        printProgress(i, t, prefix='Progress', suffix="Complete", barLength=50)
    for OH_rows in OH:
        for O2_rows in O2:
            if OH_rows == O2_rows:
                oh1620O2.append(OH_rows)
        if ShowProgress:
            i += 1
            printProgress(i, t, prefix='Progress', suffix="Complete", barLength=50)
    print("OH16, OH20 and O2 correlations found.")
    sleep(3)

    print("Processing data completed!")
    sleep(1)
    return oh1620O2


def format_list(text_list):
    print("Converting list to CSV format...")
    formatted = []
    i = 0
    t = len(text_list)
    if ShowProgress:
        printProgress(i, t, prefix='Progress', suffix="Complete", barLength=50)

    for rows in text_list:
        formatted.append(rows.replace("_", ", "))
        if ShowProgress:
            i += 1
            printProgress(i, t, prefix='Progress', suffix="Complete", barLength=50)
    print("Formatted...")
    return formatted


def save_list_to_file(name, text_list):
    print("Saving " + name + " file...")
    file_write = open(name, "w+")
    for rows in text_list:
        file_write.write(rows + "\n")
    file_write.close()
    print("File saved successfully: " + name)


welcome_message()
OH16_filename = raw_input("Enter the filepath for an OH16 file: ")

while not file_exists:
    OH16_filename = raw_input("Enter the filepath to an OH16 file: ")

OH20_filename = raw_input("Enter the filepath for an OH20 file: ")

while not file_exists:
    OH20_filename = raw_input("Enter the filepath for an OH20 file: ")

save_name = raw_input("Enter the name the file will be saved as (\"It will be saved as .csv\"): ")
progress = raw_input("Do you want to show the progress? y/n: ")
if progress == 'y':
    ShowProgress = True

OH16 = trunicate_contents(OH16_filename)
OH20 = trunicate_contents(OH20_filename)
O2 = trunicate_contents(OH20_filename)

oh1620 = find_oh1620(OH16, OH20)
formatted_list = format_list(oh1620)

os.getcwd()

if not filepath_exists("Correlations/OH16_20/CSV/"):
    os.makedirs("Correlations/OH16_20/CSV/")

if not filepath_exists("Correlations/OH16_20/TXT/"):
    os.makedirs("Correlations/OH16_20/TXT/")

save_list_to_file("Correlations/OH16_20/CSV/" + save_name + ".csv", formatted_list)
save_list_to_file("Correlations/OH16_20/TXT/" + save_name + ".txt", formatted_list)
