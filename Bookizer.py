import os
from os.path import isfile, join
from PIL import Image, ImageEnhance

threshold = 191  # range from 0 to 255

kioskPath = "./MyBookScreensFolder/"
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
files.sort(key=lambda f: os.path.getmtime(join(pathIn, f)))

# page zone + upscale and enhancing
images = [
    ImageEnhance.Contrast(Image.open(kioskPath + f).convert('RGB').crop((315, 103, 1603, 1008))).enhance(1).resize((2570, 1800), Image.LANCZOS)
    for f in files
]

print("Screens processed:")
print(files)

pdf_path = "Book.pdf"
    
images[0].save(
    pdf_path, "PDF" ,quality=100,resolution=100.0, save_all=True, append_images=images[1:]
)

print("Done.")