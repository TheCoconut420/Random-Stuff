import os
file_list = []

for root, dirs, files in os.walk(r"C:\Users\stefa\OneDrive\Dokumente\GitHub\Random-Stuff\cleaner"):
    for file in files:
        file_list.append(os.path.join(root, file))

class Cleaner:
    def __init__(self, file):
        self.file = file
        self.png = "89504E470D0A"
        self.gif = "474946383961"
        self.jpg = "FFD8FFE00010"

    def get_hex(self, file):
        with open(file, "rb") as file:
            f = file.read(6)
            self.hex = f.hex().upper()

    def check_hex(self):
        if self.hex == self.png:
            print("PNG")
        elif self.hex == self.gif:
            print("GIF")
        elif self.hex == self.jpg:
            print("JPG")

print("\n")
for i in file_list:
    c = Cleaner(i)
    c.get_hex(i)
    c.check_hex()