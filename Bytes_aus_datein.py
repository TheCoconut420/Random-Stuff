def bytestring(path, bytes):
    try:
        with open(path, 'rb') as f:
            return(f.read(bytes))
    except FileNotFoundError:
        print('File location not found!')
        bytestring(input('Enter file location: '), int(input('Enter number of bytes to read: ')))
    
print("\n")
print(bytestring(str(input("Enter the location of your file: ")), int(input('Enter number of bytes to read: '))))