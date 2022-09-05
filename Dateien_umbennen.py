import os


def rename(path, new_name):
        try:
            os.rename(path, new_name)
        except FileNotFoundError:
            print('File location not found!')
            rename(input('Enter file location: '), input('Enter new name: '))

rename(str(input("Enter the location of your file: ")), str(input('Enter new name: ')))