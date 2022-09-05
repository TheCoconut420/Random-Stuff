import os
list = []


def find_file(path, file_name):
    for root, dirs, files in os.walk(path):
        if file_name in files:
            list.append(os.path.join(root, file_name))
            break
    for i in list:
        print(i)

find_file(str(input("Enter the location of your file: ")), str(input('Enter file name: ')))