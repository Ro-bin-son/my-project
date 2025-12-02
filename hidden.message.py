from PIL import Image

img = Image.open("IMG_20250604_084602_413.jpg")
pixels = list(img.getdata())

bits = [p[0] & 1 for p in pixels[:8]]
msg = "".join(str(b) for b in bits)

print("Hidden bits:" , msg)
