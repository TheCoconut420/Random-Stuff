with open(r"C:\Users\Stefan\Desktop\3_Hygiene_Belehrungsunterlagen-und-Erklaerung_08.pdf", "rb") as file:
    print("\n")
    f = file.read(308)
    l = f.splitlines()
    print(f.hex(" "))