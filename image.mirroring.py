from PIL import Image

original_image = "IMG_20250604_084602_413.jpg"
img = Image.open(original_image)

mirror_img = img.transpose(Image.FLIP_LEFT_RIGHT)
mirrored_image = "IMG_20250604_084602_413_mirror.jpg"
mirror_img.save(mirrored_image)
Image.open(mirrored_image).show()
