from PIL import Image, ImageFilter
import os

before = Image.open("splaw.png")

after = before.filter(ImageFilter.BoxBlur(1))

output_folder = r"C:\Users\adolp\Desktop\Projetos Python"

output_path = os.path.join(output_folder, "splaw_blurred.png")
after.save(output_path)
