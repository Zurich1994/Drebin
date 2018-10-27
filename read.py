# coding = utf-8
import csv
import os
import shutil


def read_csv():
    with open('family.csv') as f:
        f_csv = csv.reader(f, delimiter=',')
        for row in f_csv:
            malware_family[row[0]] = row[1]



def create_family():
    with open('family.csv') as f:
        f_csv = csv.reader(f, delimiter=',')
        for row in f_csv:
            family_path = "E:\\Dataset\\Family\\" + row[1]
            if not os.path.exists(family_path):
                os.makedirs(family_path)


def read_malware():
    names = os.listdir('Malware')
    for name in names:
        fullpath = os.path.join("E:\\Dataset\\Malware", name)
        dirpath = "E:\\Dataset\\Family\\" + malware_family[name] + "\\" + name + ".apk"
        shutil.move(fullpath, dirpath)


if __name__ == '__main__':
    malware_family = {}
    read_csv()
    create_family()
    read_malware()
