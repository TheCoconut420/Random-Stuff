import os


def differ(path):
    if os.path.isfile(path):
        print('True')
    else:
        print('False')
        differ(input('Enter file location: '))
differ(str(input("Enter the location of your file: ")))