with open("jpg.tiff", "rb") as file:
    print("\n")
    f = file.read(300)
    l = f.splitlines()
    print(f.hex(" "))