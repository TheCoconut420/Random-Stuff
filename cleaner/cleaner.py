from webbrowser import get


hex_list = []
hex_list.append("25 50 44 46 2D")
print(hex_list[0])


def get_hex(file):
    with open(file, "rb") as file:
        print("\n")
        f = file.read(10)
        l = f.splitlines()
        hex = (f.hex(" "))
        print(hex)

get_hex(r"C:\Users\Stefan\Desktop\3_Hygiene_Belehrungsunterlagen-und-Erklaerung_08.pdf")