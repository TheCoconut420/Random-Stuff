import os


def find_file(path, file_name):
    for root, dirs, files in os.walk(path):
        if file_name in files:
            print(os.path.join(root, file_name))
            break

find_file(str(input("Enter the location of your file: ")), str(input('Enter file name: ')))