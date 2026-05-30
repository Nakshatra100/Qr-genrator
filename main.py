import qrcode
import os

url = input("enter url: ")
filename = input("enter filename to save as: ")

if not filename.endswith(".png"):
    filename = filename + ".png"

# This saves in the same folder as your Python file
save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

img = qrcode.make(url)
img.save(save_path)
print(f"QR code saved at: {save_path}")